from util.utility import load_yml
from util.solution_checker import Solution
import colorama as cr

cr.init()

def get_question_labels(yml_file):
    data = load_yml(yml_file)
    return list(data.keys())
    
def print_question_data(yml_file, question_label):
    question = load_yml(yml_file)[question_label]
    
    for key, value in question.items():
        try:
            question[key] = value.decode('utf-8')
        except AttributeError:
            pass    
            
    print('''\
{h1}----==========={question_label}===========----
{h2}imports (modules loaded before all tests)------------------------------------:
{p}{imports}
{h2}setup (script ran before all unit tests)-------------------------------------:
{p}{setup}
{h2}teardown (script ran after all unit tests)-----------------------------------:
{p}{teardown}
{h2}pretest (script ran before each unit test)-----------------------------------:
{p}{pretest}
{h2}posttest (script ran after each unit test)-----------------------------------:
{p}{posttest}
{h2}soulition (server accepted solution to question)-----------------------------:
{p}{solution}
{h2}text (text description of question)------------------------------------------:
{p}{text}
{h2}tags (tags to categorize question)-------------------------------------------:
{p}{tags}
{h2}unittests (parameters passed to soultion)------------------------------------:'''.format(
        h1=cr.Fore.CYAN + cr.Back.MAGENTA,
        h2=cr.Fore.WHITE + cr.Back.BLUE,
        p=cr.Style.RESET_ALL,
        question_label=question_label,
        **question))
    print_unti_tests(yml_file, question_label)
    print('''\
{h5}RESULTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:
{results}'''.format(h5=cr.Fore.RED + cr.Back.WHITE, results=check_solution(yml_file, question_label)))

def print_unti_tests(yml_file, question_label):
    try:
        unittests = load_yml(yml_file)[question_label]['unittests']
    except KeyError:
        unittests = {}
    for label, parameters in sorted(unittests.items()):
        print('{h3}{label}:{reset}'.format(
            h3=cr.Style.BRIGHT + cr.Fore.YELLOW + cr.Back.BLUE,
            label=label, reset=cr.Style.RESET_ALL))
        for index, parameter in enumerate(parameters, 1):
            print('{h4}parameter{index}{reset}'.format(
                h4=cr.Fore.YELLOW, index=index, reset=cr.Style.RESET_ALL))
            print(parameter)
            
def check_solution(yml_file, question_label):
    question = load_yml(yml_file)[question_label]
    master_results = Solution(question)
    master_results.run_solution()
    return master_results.test_results