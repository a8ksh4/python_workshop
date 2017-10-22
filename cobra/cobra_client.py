import requests
import json
from solution_checker import Solution
from prompt_toolkit.shortcuts import create_eventloop
from ptpython.python_input import PythonInput, PythonCommandLineInterface
from ptpython.repl import run_config
from utility import cls, hash_results, encode_message
from getpass import getpass

class CobraClient():
    def __init__(self, server_socket):
        self.server_socket = server_socket
        self.data = self.get_question()
        #self.get_user_input()
        self.create_new_user()
            
    def get_question(self):
        question = requests.get('http://{0}:{1}/getquestion'.format(*self.server_socket))      
        data = json.loads(question.text)
        return data

    def create_new_user(self):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        username = input('Enter a username: ')
        password = getpass('Enter a password: ')
        create_user = requests.post('http://{0}:{1}/newuser'.format(*self.server_socket),
                                    json={'username':username, 'password':encode_message(password)},
                                    headers=headers)
        print(create_user.text)
        
        
        
    def get_user_input(self):
        cls()
        print('{title}\n{text}\n{signature}\n'.format(**self.data))

        eventloop = create_eventloop()
        ptpython_input = PythonInput()
        run_config(ptpython_input, config_file='ptpython_config.py')
        
        try:
            cli = PythonCommandLineInterface(python_input=ptpython_input, eventloop=eventloop)
            solution = cli.run()
        finally:
            eventloop.close()
        
        results = Solution(self.data, solution.text)
        results.run_solution()
        print('{:f}'.format(results.time_to_execute))
        print(results.tests_results)
        print(results.linecount)
        print(results.charcount)
        print(results.violations)
        print(results.violationcount)
        
if __name__ == '__main__':
    CobraClient(('127.0.0.1', '8000'))
    
    

    
    







