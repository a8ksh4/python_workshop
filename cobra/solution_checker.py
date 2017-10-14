from re import findall

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
    # run each test and save results
    for test in test_list:
        arguments = map(lambda argument: eval(argument), test)  # converts the yml test case string into the solution arguments
        results.append(function(*arguments))    # the actual test is run here
    return results
    
def signature_check():
    # do later, we should probably have signatures match diriectly to avoid exceptions and overwriting namespaces
    pass
    
def run_solution(solution, data):
    '''Main function, takes a text solution and yml data, and combines the two for execution'''
    # we need to make imports global so they can be used inside of unit tests
    # we will also run our setup scripts here since we want those imports in the setup namespace
    import_items = findall(r'import\s+(.*)', data['imports'])[0]  
    exec('global {import_items}\n{imports}\n{setup}'.format(import_items=import_items, **data))

    # now we will get the function name (solution_name) used by the solution
    # this solution is exec'd to the function variable
    # then the function is pulled out of the exec namespace
    solution_name = findall(r'def\s+(.*)\(', solution)[0]
    exec_script = '{solution}\nfunction = {solution_name}'.format(solution=solution, solution_name=solution_name)
    scope = {}
    exec(exec_script, scope)
    function = scope['function']
    
    # now that we have the function in our namespace we can run it against our unittests
    results = run_tests(function, data['unittests'])
    # and finally we will run our teardown scripts
    exec('{teardown}'.format(**data))

    return results