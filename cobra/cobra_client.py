import requests
import json
from solution_checker import run_solution

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
        print('''\
{title}
{text}
{signature}
'''.format(**self.data))

        solution = ''
        user_input = None
              
        while user_input != '':
            user_input = input()
            solution += user_input + '\n'
            
        results = run_solution(solution, self.data)

        print(results)
    
if __name__ == '__main__':
    CobraClient(('127.0.0.1', '8000'))
    
    

    
    







