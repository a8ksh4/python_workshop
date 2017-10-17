from re import findall
from timeit import default_timer
from sys import executable
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile
from os import remove

def loopcount(testname):
    '''Checks for _x in test names and returns the number following'''
    try:
        loop = int(findall(r'_x(\d*)', testname)[0])
    except IndexError:
        loop = 1
    return loop
    
def run_tests(function, unittests):
    '''Runs the solution against all unit tests'''
    results = []
    test_list = []
    # first implement any text case multipliers, extends the total number of tests
    for testname, values in sorted(unittests.items()):
        for _ in range(loopcount(testname)):
            test_list.append(values)   
    # run each test and save results, and time taken
    start_time = default_timer()
    try:
        for test in test_list:
            arguments = map(lambda argument: eval(argument), test)  # converts the yml test case string into the solution arguments
            results.append(function(*arguments))    # the actual test is run here
    except Exception as e:
        print('{}: {}'.format(type(e).__name__, e))
    time_to_execute = default_timer() - start_time
    return results, time_to_execute
    
def signature_check():
    # do later, we should probably have signatures match diriectly to avoid exceptions and overwriting namespaces
    pass
    
def check_codestyle(solution):
    '''Checks the solution for pep8 standards'''
    solution_file = NamedTemporaryFile(delete=False, encoding='utf-8', mode='w', suffix='.py')
    solution_file.write(solution)
    solution_file.close()
    flake = Popen([executable, '-m', 'flake8', '--disable-noqa', '--ignore=W292', solution_file.name], stdout=PIPE, stdin=PIPE)
    out, error = flake.communicate()
    remove(solution_file.name)
    print(out.decode('utf-8'))
    
def run_solution(solution, data):
    '''Main function, takes a text solution and yml data, and combines the two for execution'''
    # these two lines let meta information get passed into the setup and teardown scripts.
    # it's mostly so you can send a dynamic seed
    data['setup'] = data['setup'].format(**data)
    data['teardown'] = data['teardown'].format(**data)
    
    # we need to make imports global so they can be used inside of unit tests
    # we will also run our setup scripts here since we want those imports in the setup namespace
    import_items = findall(r'import\s+(.*)', data['imports'])[0]
    exec('global {import_items}\n{imports}\n{setup}'.format(import_items=import_items, **data))

    # now we will get the function name (solution_name) used by the solution
    # this solution is exec'd to the function variable
    # then the function is pulled out of the exec namespace
    #solution_name = findall(r'def\s+(.*)\(', solution)[0]
    exec_script = '{}'.format(solution)
    scope = {}
    try:
        exec(exec_script, scope)
    except Exception as e:
        print('{}: {}'.format(type(e).__name__, e))
        exec('{teardown}'.format(**data))
        return None
        
    scope.pop('__builtins__')
    function = [value for value in scope.values()][0]
    
    # now that we have the function in our namespace we can run it against our unittests
    results, time_to_execute = run_tests(function, data['unittests'])
    # and finally we will run our teardown scripts
    exec('{teardown}'.format(**data))
    check_codestyle(solution)
    return results, time_to_execute