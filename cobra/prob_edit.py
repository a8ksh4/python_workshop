#!/usr/bin/env python 
# Python2 compatibility:
#from __future__ import print_function
#from future.builtins import input

# Other imports:
import copy
import filecmp
from glob import glob
#import operator
from operator import itemgetter
import os
import shutil
import subprocess as sp
#import tempfile
from tempfile import mkstemp
import time
import traceback
import yaml
import cobra_client as cc


EDITOR='/usr/bin/vi'
EXCLUDE_FILES = ['session.yml',]
ESSENTIAL_KEYS = ('imports', 'posttest', 'pretest', 'setup', 'signature',
                  'solution', 'tags', 'teardown', 'text', 'unittests')

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def editTempFile(content, ref_header=None):
    '''put "content" into a temp file and open it with the system editor.
    if ref_header is defined, put that at the top of the file for reference.
    a marker line follows, and the content is placed below that for editing.
    Return the updated content.'''

    marker = "\n### do not edit anything above this line ###\n"
    _, fname = mkstemp()
    with open(fname, 'w') as f:
        if ref_header != None:
            f.write(ref_header)
            f.write(marker)
            if not content.startswith('\n'):
                f.write('\n')
        f.write(content)

    vi_cmd = (EDITOR, fname)
    sp.call(vi_cmd, shell=False)

    with open(fname, 'r') as f:
        new_content = f.read()

    if ref_header != None:
        marker_loc = new_content.find(marker)
        if marker_loc < 0:
            print('Marker line not found... Aborting!')
            print('Will re-open the editor, please copy your stuff externally.')
            input("enter to continue...")
            time.sleep(2)
            with open(fname, 'a') as f:
                f.write('\n### SAVE THIS CONTENT EXTERNALLY, FATAL ERROR ###\n')
                f.write('\n### SAVE THIS CONTENT EXTERNALLY, FATAL ERROR ###\n')
                f.write('\n### SAVE THIS CONTENT EXTERNALLY, FATAL ERROR ###\n')
                f.write('\n### SAVE THIS CONTENT EXTERNALLY, FATAL ERROR ###\n')
            sp.call(vi_cmd, shell=False)
            return content
        #offset to end of marker line
        marker_loc += len(marker)
        new_content = new_content[marker_loc:]

    #for guess in (1, 2, 3):
    #    answer = input("Save changes? [y]/n: ")
    #    if answer in ("", "y", "n"):
    #        if answer == "n":
    #            new_content = content
    #        break
    #    print("Responses accepted: 'y', 'n', or implicit y ''")
    #else:
    #    print("Aborting!")
    #    time.sleep(2)
    #    new_content = content
    return new_content


def mergeEditYml(problem, keys_to_edit, ref_header=None):
    '''The idea here is to generate a string with yaml data for all
    of the "keys_to_edit" from the problem data.  Then pas it to the
    editTempFile function for user edit with VI, and then return 
    the modified data.
    '''
    content = {}
    for key in keys_to_edit:
        content[key] = problem[key]
    new_content = yaml.dump(content, default_flow_style=False)
    new_content = editTempFile(new_content, ref_header)
    try:
        print("Success loading yaml content...")
        new_content = yaml.load(new_content)
    except:
        new_content = content
    for key in keys_to_edit:
        if key not in new_content:
            print("Keys missing in returned text:", key, "from", keys_to_edit)
            print("Aborting...")
            time.sleep(2)
            break
    else:
        print("All good...")
        return new_content
    return content


def getProbsFiles():
    all_files = glob('*.yml')
    out_files = []
    for f in all_files:
        for x in EXCLUDE_FILES:
            if x in f:
                break
        else:
            out_files.append(f)
    return out_files


def testUpdateYmlFormat(probs_dict):
    '''This checks if the yml is the old format (with uuid, etc).  if it
    is, then it is convrted to the new format and returned.'''
    out = {}
    for key, val in probs_dict.items():
        if 'title' in val:
            key = val.pop('title')
        if 'uuid' in val:
            val.pop('uuid')
        for k in ('pretest', 'posttest', 'tags', 
                  'imports', 'setup', 'teardown'):
            if k not in val:
                val[k] = ''
        out[key] = val
    return out
    


def readProbsFile(problem_file):
    '''This is called for each file containing course problems.  Returns
    a list of problems (dicts)'''
    probs_dict = yaml.load(open(problem_file, 'r'))
    probs_dict = testUpdateYmlFormat(probs_dict)

    return probs_dict


def writeProbsFile(problem_file, probs_dict):
    '''Takes a list of problem dicts and converts them to a dict of dicts
    using the title as the primary key and writes them as yaml to the
    problem_file'''
    # translate back into dict for storage
    #probs_dict = {}
    #for prob in probs_list:
    #    probs_dict[prob['title']] = prob
    with open(problem_file, 'w') as f:
        f.write(yaml.dump(probs_dict, default_flow_style=False))


def promptMenu(title, options, defaults=None):
    '''This is mianly what the user interacts with.  It puts up a list of
    optoins and queries for a response from the user.
    "options" is a list of options that will be assigned numbers to chose
    from.  "defaults" is a list of (key, description) items
    that the user can choose from.'''
    if not defaults:
        defaults = (('n', 'next'),
                    ('p', 'previous'),
                    ('q', 'quit/return'))
    valid_choices = [str(n) for n in range(len(options))]
    valid_choices += [n for n, o in defaults]

    print("\n --- {} ---".format(title))
    for n, option in enumerate(options):
        print("  {} {}".format(n, option))
    print("")
    for n, option in defaults:
        print("  {} {}".format(n, option))
    print("")

    for guess in (1, 2, 3):
        answer = input("Select: ")
        if answer not in valid_choices:
            print("Invalid.  Optoins are:", valid_choices)
            continue
        break
    else:
        return None
    return answer


def backupProbsFile(probs_file_name):
    # Make a backup copy of the problems file
    if not os.path.isdir('./backups'):
        os.mkdir('./backups')
    epoch_seconds = int(time.time())
    shutil.copy( probs_file_name, 
                 "./backups/{}_{}".format(probs_file_name,
                                          epoch_seconds) )
    assert( filecmp.cmp(
                probs_file_name,
                "./backups/{}_{}".format(probs_file_name,
                                         epoch_seconds) ) )


def dPos(a_dict, key=None, index=None):
    '''If key is set, return the index of the key; if index is set, return
    the key at the given index.'''
    d_list = list(a_dict.keys())
    if key != None:
        index = d_list.index(key)
        return index
    elif index != None:
        key = d_list[index]
        return key


def dMove(a_dict, key, offset):
    '''Return re-ordered dictionary with key move by given offset.
    Do nothing if key not in dictionary. Limit offset to ends of dict.'''
    if key in a_dict:
        index = dPos(a_dict, key)
        foo = list(a_dict.items())
        new_index = min(max(0, index + offset), len(foo)-1)
        tmp = foo.pop(index)
        foo.insert(new_index, tmp)
        foo = dict(foo)
    else:
        foo = a_dict
    return foo


def interactiveMenu(probs_dicts):
    '''This is the meat of the tool.  All of the code that make things
    happen at each screen is included here.  Trying to keep cross-contamination
    between variables in here to a minimum w/o having to break out seperate
    functions for each screen.'''
    probs_file_name = None
    probs_dict = None
    prob_title = None
    while True:
        cls()
        print("probs_file_name:", probs_file_name)
        print("prob_title:", prob_title)

        # Each time menu is updated, write changes to disk
        if not probs_file_name == None:
            writeProbsFile(probs_file_name, probs_dict)

        ######################
        # Chose a problem file
        ######################
        if probs_file_name == None:
            defaults = (('q', 'quit/return'), )
            title = "Choose a problem file:"
            choice = promptMenu(title, probs_dicts.keys(), defaults)
            print("Choice was:", (choice,))
            #time.sleep(2)

            if choice == None:
                break
            elif choice.isdigit():
                #probs_file_name = probs_dicts.keys()[int(choice)]
                probs_file_name = dPos(probs_dicts, index=int(choice))
                probs_dict = probs_dicts[probs_file_name]
                backupProbsFile(probs_file_name)
            elif choice == 'q':
                print("Quitting this fine program!")
                break

        ######################
        # Chose a problem
        ######################
        elif prob_title == None:
            defaults = ( ('q', 'quit/return'), )
            title = "Choose a problem to work on from '{}':".format(
                                                        probs_file_name)
            probs_titles = [(k, v['signature']) for k, v in probs_dict.items()]
            choice = promptMenu(title, probs_titles, defaults)
            print("Choice was:", (choice,))
            #time.sleep(2)

            if choice == None:
                break
            elif choice.isdigit():
                prob_title = dPos(probs_dict, index=int(choice))
                #prob_title = probs_dict.keys()[int(choice)]
            elif choice == 'q':
                probs_file_name = None
                continue

        ######################
        # Problem edit menu
        ######################
        else:
            prob_dict = probs_dict[prob_title]
            prob_index = dPos(probs_dict, prob_title)

            defaults = (('e', 'edit all relevant fields'),
                        ('c', 'copy the problem'),
                        ('r', 'run the problem'),
                        ('-', ''),
                        ('t', 'edit title'),
                        ('x', 'edit text description'),
                        ('g', 'edit signature'),
                        ('s', 'edit solution'),
                        ('u', 'edit unit test'),
                        ('d', 'edit teardown'),
                        ('+', 'move up in order'),
                        ('-', 'move down in order'),
                        ('[', 'previous problem'),
                        (']', 'next problem'),
                        ('q', 'quit/return'))
            title = ( "Prob Selected:  index: {}\n"
                      "  title: {}\n"
                      "  signature: {}\n"
                      "  text: \n"
                      "{}".format( prob_index, prob_title,
                                   prob_dict['signature'],
                                   prob_dict['text'] ) )
            choice = promptMenu(title, [], defaults)
            print("Choice was:", (choice,))
            #time.sleep(2)
            if choice.isdigit():
                pass

            # Edit problem title
            elif choice == 't':
                old_title = prob_title
                while True:
                    prob_title = input("New Title: ")
                    if prob_title in probs_dict:
                        print("duplicate title!, try again.")
                        continue
                    break
                probs_dict[prob_title] = probs_dict.pop(old_title)

            # Edit problem signature
            elif choice == 'g':
                prob_dict['signature'] = input("New Signature: ")

            # Edit text description
            elif choice == 'x':
                prob_dict['text'] = editTempFile(prob_dict['text'])
            
            elif choice == 's':
                prob_dict['solution'] = editTempFile( prob_dict['solution'],
                                                      prob_dict['text'] )

            # Edit unit tests
            elif choice == 'u':
                edit_keys = ('unittests', 'imports', 'setup', 'teardown')
                content = mergeEditYml(prob_dict, edit_keys, prob_dict['text'])
                for key in edit_keys:
                    prob_dict[key] = content[key]

            # Edit unit test teardown
            elif choice == 'd':
                prob_dict['teardown'] = editTempFile( prob_dict['teardown'],
                                                      prob_dict['text'] )

            # Edit all relevant fields
            elif choice == 'e':
                edit_keys = ('text', 'signature', 'solution', 'tags',
                             'unittests', 'imports', 'setup', 'teardown')
                content = mergeEditYml(prob_dict, edit_keys)
                for key in edit_keys:
                    prob_dict[key] = content[key]

            # Copy the current problem
            elif choice == 'c':
                old_title = prob_title
                old_dict = prob_dict

                digit = 0
                while True:
                    prob_title = '{} copy {}'.format(old_title, digit)
                    if prob_title in probs_dict:
                        digit += 1
                        continue
                    break
                prob_dict = {}
                for key in ESSENTIAL_KEYS:
                    prob_dict[key] = copy.deepcopy(old_dict[key])
                probs_dict[prob_title] = prob_dict

            # Run the problem:
            elif choice == 'r':
                from ptpython.repl import run_config
                question_data = prob_dict
                question_data['seed'] = 0
                eventloop = cc.create_eventloop()
                ptpython_input = cc.PythonInput()
                run_config(ptpython_input,
                           config_file='util/ptpython_config.py')
                print("answer.text:  ", question_data['solution'])
                print("------------- running ------------")
                answer = cc.Solution(question_data, question_data['solution'])
                try:
                    answer.run_solution(True)
                    print("------------- RESULS: ------------")
                    print("solution: ", answer.test_results)
                    print("a.violations:", answer.violations)
                    print("a.violcount:", answer.violationcount)
                    print("teardown:", answer._teardown)
                    #import code
                    #code.InteractiveConsole(locals=locals()).interact()
                except Exception as e:
                    print("Exception in run: {}".format(e))
                    traceback.print_stack()

                input("Enter to continue...")

            # Change ordering, etc...
            elif choice == '+':
                probs_dict = dMove(probs_dict, prob_title, 1)
            elif choice == '-':
                probs_dict = dMove(probs_dict, prob_title, -1)
            elif choice == '[':
                prob_index = max(0, prob_index-1)
                prob_title = dPos(probs_dict, index=prob_index)
            elif choice == ']':
                prob_index = min(len(probs_dict)-1, prob_index+1)
                prob_title = dPos(probs_dict, index=prob_index)

            elif choice == 'q':
                prob_title = None
                prob_dit = None

def mainFunc():
    probs_files = sorted(getProbsFiles())
    print(probs_files)
    probs_dicts = {}
    for p_file in sorted(probs_files):
        probs_dicts[p_file] = readProbsFile(p_file)

    interactiveMenu(probs_dicts)


if __name__ == "__main__":
    mainFunc()
