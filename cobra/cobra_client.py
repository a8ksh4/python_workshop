import requests
import json
from solution_checker import SolutionStats, SolutionExec
from prompt_toolkit.shortcuts import create_eventloop
from ptpython.python_input import PythonInput, PythonCommandLineInterface
from ptpython.repl import run_config
from utility import cls, hash_results

class CobraClient():
    def __init__(self, server_socket):
        self.server_socket = server_socket
        self.data = self.get_question()
        self.get_user_input()
            
    def get_question(self):
        question = requests.get('http://{0}:{1}/getquestion'.format(*self.server_socket))
        data = json.loads(question.text)
        return data

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
        
        results = SolutionExec(self.data, solution.text)
        stats = SolutionStats(solution.text)
        results.run_solution()
        print(results.time_to_execute)
        print(results.tests_results)
        print(stats.linecount)
        print(stats.charcount)
        print(stats.violations)
        print(stats.violationcount)
        print(results.test)
        
if __name__ == '__main__':
    CobraClient(('127.0.0.1', '8000'))
    
    

    
    







