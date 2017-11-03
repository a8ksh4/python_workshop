#!/usr/bin/env python

import requests
import json
from util.solution_checker import Solution
from prompt_toolkit.shortcuts import create_eventloop
from ptpython.python_input import PythonInput, PythonCommandLineInterface
from ptpython.repl import run_config
from util.utility import cls, hash_results, encode_message, decode_message, load_yml, save_yml
from getpass import getpass

class CobraClient():
    def __init__(self, server_socket):
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

    def create_new_user(self):
        username = input('Enter a username: ')
        password = getpass('Enter a password: ')
        req = requests.post('http://{0}:{1}/newuser'.format(*self.server_socket),
                                    json={'username':username, 'password':encode_message(password)},
                                    headers=self.headers)
        self.username = username
        self.sessionid = decode_message(req.text)
        
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
        print('{lesson}\n{title}\n{text}\n{signature}\n'.format(lesson=lesson, title=question_label, **question_data))
        
        eventloop = create_eventloop()
        ptpython_input = PythonInput()
        run_config(ptpython_input, config_file='util/ptpython_config.py')
        try:
            cli = PythonCommandLineInterface(python_input=ptpython_input, eventloop=eventloop)
            solution = cli.run()
        finally:
            eventloop.close()
        #try:
        results = Solution(question_data, solution.text)
        results.run_solution()
        #except:
        #    return False

        print('{:f}'.format(results.time_to_execute))
        print(results.test_results)
        print(results.linecount)
        print(results.charcount)
        print(results.violations)
        print(results.violationcount)
        print('======================================================================')
        
        req = requests.post('http://{0}:{1}/submitsolution'.format(*self.server_socket),
                                    json={'username': self.username, 'lesson': lesson, 'question_label': question_label,
                                          'solution': results.solution, 'results': results.test_results},
                                    headers=self.headers)
        
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
        self.solve_question('python_basics', 'basic_math_1')
        #self.solve_question('python_basics', 'basic_math_2')
        #self.solve_question('python_basics', 'basic_math_3')
        #self.solve_question('python_basics', 'basic_math_4')
        #self.solve_question('python_basics', 'basic_math_5')
        #self.solve_question('python_basics', 'basic_math_6')
        #self.solve_question('python_basics', 'strings_1')
        #self.solve_question('python_basics', 'strings_2')
        #self.solve_question('python_basics', 'strings_3')
        #self.solve_question('python_basics', 'strings_4')
        #self.solve_question('python_basics', 'strings_5')
        #self.solve_question('python_basics', 'strings_6')
        #self.solve_question('python_basics', 'strings_7')
        #self.solve_question('python_basics', 'strings_8')
        #self.solve_question('python_basics', 'branching_1')
        #self.solve_question('python_basics', 'branching_2')
        #self.solve_question('python_basics', 'branching_3')
        #self.solve_question('python_basics', 'lists_1')
        #self.solve_question('python_basics', 'lists_2')
        #self.solve_question('python_basics', 'sets_1')
        #self.solve_question('python_basics', 'sets_2')
        #self.solve_question('python_basics', 'sets_3')
        #self.solve_question('python_basics', 'sets_4')
        #self.solve_question('python_basics', 'dictionaries_1')
        #self.solve_question('python_basics', 'dictionaries_2')
        #self.solve_question('python_basics', 'dictionaries_3')
        #self.solve_question('python_basics', 'dictionaries_4')
        #self.solve_question('python_basics', 'dictionaries_5')
        #self.solve_question('python_basics', 'dictionaries_6')
        #self.solve_question('python_basics', 'dictionaries_7')
        
if __name__ == '__main__':
    CobraClient(('127.0.0.1', '8000'))
    
    

    
    







