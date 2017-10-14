import requests
import json
from re import findall

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
            
        results = self.run_solution(solution)

        print(results)
    
    def run_solution(self, solution):
    
        def loopcount(testname):
            try:
                loop = int(findall(r'_x(\d*)', testname)[0])
            except IndexError:
                loop = 1
            return loop
        
        
        local_namespace = locals()
        exec(self.data['setup'], local_namespace) 
        locals().update(local_namespace)        
        
        function_name = findall(r'def\s*(.*)\(', solution)[0]
        scope = {}
        unittests = self.data['unittests']      
        exec(solution, scope)
        function = scope[function_name]
        
        results = []
        for testname, values in unittests.items():
            arguments = []
            for argument in values:
                local_namespace = locals()
                exec('arguments += [{}]'.format(argument), local_namespace)
                locals().update(local_namespace)
            
            for _ in range(loopcount(testname)):
                results += [function(*arguments)]
        
        return results
    
if __name__ == '__main__':
    CobraClient(('127.0.0.1', '8000'))
    
    

    
    







