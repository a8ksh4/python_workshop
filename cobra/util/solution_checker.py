from re import findall
from timeit import default_timer
from sys import executable
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile
from os import remove
    
class Solution():
    def __init__(self, data, solution=None):
        if solution:
            self.solution = solution
        else:
            try:
                self.solution = data['solution'].decode('utf-8')
            except AttributeError:
                self.solution = data['solution']
        self._imports = data['imports']
        # these .formats let meta information get passed into the setup and teardown scripts.        
        # it's mostly so you can send a dynamic seed      
        self._setup = data['setup'].format(**data)
        self._teardown = data['teardown'].format(**data)
        self._pretest = data['pretest'].format(**data)
        self._posttest = data['posttest'].format(**data)
        self._unittests = data['unittests']
        self._function = None
        self.exception_raised = False
        self.test_results = []
        self.time_to_execute = 0
        self.linecount, self.charcount = self.get_counts()
        self.violations = self.check_codestyle()
        if self.violations == '':
            self.violationcount = 0
        else:
            self.violationcount = len(self.violations.split('\n'))

    def check_codestyle(self):
        '''Checks the solution for pep8 standards'''
        solution_file = NamedTemporaryFile(delete=False, encoding='utf-8', mode='w', suffix='.py')
        solution_file.write(self.solution)
        solution_file.close()
        flake = Popen([executable, '-m', 'flake8',
                    '--format=row %(row)d, col %(col)d: %(text)s',
                    '--disable-noqa', '--max-line-length=150', '--ignore=W292,E731', solution_file.name],
                    stdout=PIPE, stderr=PIPE)
        out, error = flake.communicate()
        if error:
            print(error.decode('utf8'))
        remove(solution_file.name)
        return out.decode('utf-8').strip()
        
    def get_counts(self):
        linecount = len(self.solution.split('\n'))
        charcount = len(self.solution)
        return linecount, charcount    
        
    def run_solution(self):
        '''Takes a text solution and yml data, and combines the two for execution'''    
        # we need to make imports global so they can be used inside of unit tests
        # we will also run our setup scripts here since we want those imports in the setup namespace        
        scope = {}
        try:
            exec(self.solution, scope)
        except Exception as e:
            print('{}: {}'.format(type(e).__name__, e))       
            exception_raised = True
            return None
        #scope.pop('__builtins__')
        #self._function = [value for value in scope.values() if value != '__builtins__'][0]
        for value in scope.values():
            if isinstance(value, dict):
                continue
            else:
                self._function = value
        # now that we have the function in our namespace we can run it against our unittests
        self._run_tests()
        # and finally we will run our teardown scripts

    def _run_tests(self):
        '''Runs the solution against all unit tests'''
        test_list = []
        
        exec(self._imports)    
        exec(self._setup)        
        
        # first implement any text case multipliers, extends the total number of tests
        try:
            for testname, values in sorted(self._unittests.items()):
                for _ in range(self._loopcount(testname)):
                    test_list.append(values)    
        except AttributeError:
            pass
        
        # run through all the unit tests if they exist
        if test_list:
            for test in test_list:
                exec(self._pretest) # pretest script
                arguments = []
                for argument in test:
                    #print(type(argument))
                    arguments += [eval(str(argument))]
                    #arguments.append(argument)
                #arguments = map(lambda argument: eval(argument, locals), test) # converts the yml test case string into the solution arguments
                self._run_test(arguments)
                exec(self._posttest) # posttest script  
        # if there are no unit tests we just run the function once
        else:
            exec(self._pretest) # pretest script
            self._run_test([])
            exec(self._posttest) # posttest script  
        exec(self._teardown)

    def _loopcount(self, testname):
        '''Checks for _x in test names and returns the number following'''
        try:
            loop = int(findall(r'_x(\d*)', testname)[0])
        except IndexError:
            loop = 1
        return loop
            
    def _run_test(self, arguments):
        ''' run test and save results, and time taken '''
        start_time = default_timer()
        try:
            #print(arguments)
            #print(self._function)
            result = self._function(*arguments)    # the actual test is run here
        except Exception as e:
            print('{}: {}'.format(type(e).__name__, e))
            result = None
            exception_raised = True
        finally:            
            time_to_execute = default_timer() - start_time
        self.test_results.append(result)
        self.time_to_execute += time_to_execute
