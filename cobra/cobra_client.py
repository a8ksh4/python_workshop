import requests
import json
from util.solution_checker import Solution
from prompt_toolkit.shortcuts import create_eventloop
from ptpython.python_input import PythonInput, PythonCommandLineInterface
from ptpython.repl import run_config
from util.utility import cls, hash_results, encode_message, decode_message, load_yml, save_yml
from getpass import getpass
import colorama as cr
from time import sleep


class CobraClient():
    def __init__(self, server_socket):
        cr.init()
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        self.username = None
        self.sessionid = None
        self.server_socket = server_socket
        self.run()
            
    def get_lessons(self):
        req = requests.get('http://{0}:{1}/getlessons'.format(*self.server_socket))
        return json.loads(req.text)
            
    def get_questions(self, lesson):
        req = requests.post('http://{0}:{1}/getquestions'.format(*self.server_socket),
                                    json={'lesson':lesson},
                                    headers=self.headers)
        return son.loads(req.text)
    
    def get_question(self, lesson, question_label):
        req = requests.post('http://{0}:{1}/getquestion'.format(*self.server_socket),
                                    json={'lesson': lesson, 'question_label': question_label, 'username': self.username},
                                    headers=self.headers)
        return json.loads(req.text)
        
    def get_next_question(self):
        req = requests.post('http://{0}:{1}/getnextquestion'.format(*self.server_socket),
                                    json={'username': self.username},
                                    headers=self.headers)
        return json.loads(req.text)

    def create_new_user(self):
        username = input('Enter a username: ')
        password = getpass('Enter a password: ')
        req = requests.post('http://{0}:{1}/newuser'.format(*self.server_socket),
                                    json={'username':username, 'password':encode_message(password)},
                                    headers=self.headers)
        self.username = username
        self.sessionid = decode_message(req.text)
        sleep(1)
        
    def login(self, continue_session=False):
        if continue_session:
            username, sessionid =  list(load_yml('clientdata/session.yml').items())[0]
            password = '0'
        else:
            username = input('Enter a username: ')
            password = getpass('Enter password: ')
            sessionid = '0'
        req = requests.post('http://{0}:{1}/login'.format(*self.server_socket),
                                    json={'username':username, 'password':encode_message(password), 'sessionid': encode_message(sessionid)},
                                    headers=self.headers)
        self.username = username
        save_yml('clientdata/session.yml', {self.username: req.text})
        self.session_id = decode_message(req.text)
        
    def solve_question(self, lesson, question_label):
        question_data = self.get_question(lesson, question_label)
        run_question_loop = True
        while run_question_loop:
            print('{}======================================================================'.format(cr.Style.RESET_ALL))
            print('{lesson_color}{lesson}\n{title_color}{title}\n{text_color}{text}\n{signature_color}{signature}{reset}\n'.format(
                lesson=lesson, title=question_label, 
                lesson_color=cr.Back.BLUE + cr.Fore.YELLOW, title_color=cr.Back.BLUE + cr.Fore.WHITE,
                text_color=cr.Back.BLACK + cr.Fore.CYAN, signature_color=cr.Back.BLACK + cr.Fore.MAGENTA,
                reset=cr.Style.RESET_ALL,
                **question_data))
            
            eventloop = create_eventloop()
            ptpython_input = PythonInput()
            run_config(ptpython_input, config_file='util/ptpython_config.py')
            try:
                cli = PythonCommandLineInterface(python_input=ptpython_input, eventloop=eventloop)
                solution = cli.run()
            finally:
                eventloop.close()
            try:
                print('Running the following parameters into your function:')
                for parameter in question_data['unittests'].values():
                    print('({}'.format(cr.Fore.YELLOW), end='')
                    print(', '.join(map(lambda item: str(item), parameter)), end='')
                    print('{})'.format(cr.Style.RESET_ALL))
                results = Solution(question_data, solution.text)
                results.run_solution()
            except Exception as e:
                print('{}An exception occred while running your code: {}{}'.format(cr.Fore.RED, e, cr.Style.RESET_ALL))
                continue

            print('Time to execute: {}{:f}{}'.format(cr.Fore.GREEN, results.time_to_execute, cr.Style.RESET_ALL))
            print('Unit Test results: {}{}{}'.format(cr.Fore.GREEN, results.test_results, cr.Style.RESET_ALL))
            print('Line count: {}{}{}'.format(cr.Fore.GREEN, results.linecount, cr.Style.RESET_ALL))
            print('Character count: {}{}{}'.format(cr.Fore.GREEN, results.charcount, cr.Style.RESET_ALL))
            print('Format style violations: {}{}{}'.format(cr.Fore.RED, results.violationcount, cr.Style.RESET_ALL))
            print('Violation details:\n{}{}{}'.format(cr.Fore.RED, results.violations, cr.Style.RESET_ALL))
            
            stats = {   'runtime': results.time_to_execute,
                        'linecount': results.linecount, 
                        'charcount': results.charcount, 
                        'violations': results.violationcount}
            
            req = requests.post('http://{0}:{1}/submitsolution'.format(*self.server_socket),
                                        json={'username': self.username, 'lesson': lesson, 'question_label': question_label,
                                              'solution': results.solution, 'results': hash_results(results.test_results), 'stats': stats},
                                        headers=self.headers)
            if req.text == '"fail"':
                input('Your solution did not match the server results. Please try again')
                continue
            else:
                run_question_loop = False
    
    def history_menu(self):
        req = requests.post('http://{0}:{1}/getcompleted'.format(*self.server_socket),
                                json={'username': self.username},
                                headers=self.headers)
        completed = json.loads(req.text)

        while True:
            for index, item in enumerate(completed, 1):
                print('{}) {}: {}'.format(index, item[0], item[1]))
            print('0) Back')
            try:
                selection = int(input('Select a question to view it\'s submissions: '))
                if selection == 0:
                    break
                item = dict(enumerate(completed, 1))[selection]
                self.print_history(item[0], item[1])
            except KeyError:
                pass
            except ValueError:
                pass

    def print_history(self, lesson, question_label):
        req = requests.post('http://{0}:{1}/gethistory'.format(*self.server_socket),
                                json={'username': self.username, 'lesson': lesson, 'question_label': question_label},
                                headers=self.headers)
        history = json.loads(req.text)    
        for name, info in history.items():
            print('{}{}:{}'.format(cr.Back.MAGENTA + cr.Fore.CYAN, name, cr.Style.RESET_ALL))
            print('SOLUTION:')
            print('{}{}{}'.format(cr.Fore.CYAN, info['solution'], cr.Style.RESET_ALL))
            print('RUNTIME:')
            print('{}{}{}'.format(cr.Fore.GREEN, info['stats']['runtime'], cr.Style.RESET_ALL))
            print('LINES:')
            print('{}{}{}'.format(cr.Fore.GREEN, info['stats']['linecount'], cr.Style.RESET_ALL))
            print('CHARACTERS:')
            print('{}{}{}'.format(cr.Fore.GREEN, info['stats']['charcount'], cr.Style.RESET_ALL))
            print('VIOLATIONS:')
            print('{}{}{}'.format(cr.Fore.RED, info['stats']['violations'], cr.Style.RESET_ALL))
            
        
    def run(self):
        cls()
        selection = input('1) login\n2) create account\n3) continue last session\n> ')
        if selection == '1':
            self.login()
        elif selection == '2':
            self.create_new_user()
        elif selection == '3':
            self.login(continue_session=True)
        else:
            pass
        sleep(.25)
        run_main_loop = True
        while run_main_loop:
            while True:
                print('1) Get next question')
                print('2) Review qestion solutions')
                try:
                    selection = int(input('Select an option: '))
                    if selection == 2:
                        self.history_menu()
                    if selection == 1:
                        break
                except KeyError:
                    pass
                except ValueError:
                    pass
            
            lesson, question_label = self.get_next_question()
            if lesson == None and question_label == None:
                run_main_loop = False
            else:
                self.solve_question(lesson, question_label)
            
if __name__ == '__main__':
    CobraClient(('127.0.0.1', '8000'))
    
    

    
    







