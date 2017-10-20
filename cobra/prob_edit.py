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
import uuid
import yaml


EDITOR='/usr/bin/vi'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def generateUUID():
    return str(uuid.uuid1())


def editTempFile(content, ref_header=None):
    '''put "content" into a temp file and open it with the system editor.
    if ref_header is defined, put that at the top of the file for reference.
    a marker line follows, and the content is placed below that for editing.
    Return the updated content.'''

    marker = "\n### do not edit anything above this line ###\n\n"
    _, fname = mkstemp()
    with open(fname, 'w') as f:
        if ref_header != None:
            f.write(ref_header)
            f.write(marker)
        f.write(content)

    vi_cmd = (EDITOR, fname)
    sp.call(vi_cmd, shell=False)

    with open(fname, 'r') as f:
        new_content = f.read()

    if ref_header != None:
        marker_loc = new_content.find(marker)
        if marker_loc < 0:
            print('Marker line not found... Aborting!')
            time.sleep(2)
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
    return glob('*.yml')


def readProbsFile(problem_file):
    '''This is called for each file containing course problems.  Returns
    a list of problems (dicts)'''
    probs_dict = yaml.load(open(problem_file, 'r'))
    # translate to list for more simple interaction
    probs_list = []
    for uuid, prob in probs_dict.items():
        prob['uuid'] = uuid
        probs_list.append(prob)
        for key in ('uuid', 'title', 'tier'):
            print(probs_list[-1][key])
    for prob in probs_list:
        print(prob.keys())
    probs_list = sorted(probs_list,
                        key=itemgetter('tier', 'title', 'uuid'))
    #probs_list = sorted(probs_list,
    #                    key=itemgetter('uuid', 'title', 'tier'))
    return probs_list


def writeProbsFile(problem_file, probs_list):
    '''Takes a list of problem dicts and converts them to a dict of dicts
    using the uuid as the primary key and writes them as yaml to the
    problem_file'''
    # translate back into dict for storage
    probs_dict = {}
    for prob in probs_list:
        probs_dict[prob['uuid']] = prob
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


def interactiveMenu(probs_lists):
    '''this is the meat of the tool.  All of the code that make things
    happen at each screen is included here.  Trying to keep cross-contamination
    between variables in here to a minimum w/o having to break out seperate
    functions for each screen.'''
    probs_file_name = None
    probs_list = None
    prob_index = None
    prob_selected = None
    while True:
        cls()
        print("probs_file_name:", probs_file_name)
        print("prob_index:", prob_index)

        # Each time menu is updated, write changes to disk
        if not probs_file_name == None:
            writeProbsFile(probs_file_name, probs_list)

        ######################
        # Chose a problem file
        ######################
        if probs_file_name == None:
            defaults = (('q', 'quit/return'), )
            title = "Choose a problem file:"
            choice = promptMenu(title, probs_lists.keys(), defaults)
            print("Choice was:", (choice,))
            #time.sleep(2)
            if choice == None:
                break
            elif choice.isdigit():
                probs_file_name = list(probs_lists.keys())[int(choice)]
                probs_list = probs_lists[probs_file_name]

                # Make a backup copy of the problems file
                epoch_seconds = int(time.time())
                shutil.copy(probs_file_name, "{}_{}".format(probs_file_name,
                                                         epoch_seconds))
                assert( filecmp.cmp(
                            probs_file_name,
                            "{}_{}".format(probs_file_name, epoch_seconds) )
                )

            elif choice == 'q':
                print("Quitting this fine program!")
                break

        ######################
        # Chose a problem
        ######################
        elif prob_index == None:
            defaults = (('c', 'create new problem'),
                        ('n', 'next problem file'),
                        ('p', 'previous problem file'),
                        ('q', 'quit/return'))
            title = "Choose a problem to work on from '{}':".format(
                                                        probs_file_name)
            probs_titles = [(p['tier'],p['title'],p['signature']) 
                                                        for p in probs_list]
            choice = promptMenu(title, probs_titles, defaults)
            print("Choice was:", (choice,))
            #time.sleep(2)
            if choice == None:
                break
            elif choice.isdigit():
                prob_index = int(choice)
            elif choice == 'c':
                pass
            elif choice == 'n':
                pass
            elif choice == 'p':
                pass
            elif choice == 'q':
                probs_file_name = None
                continue

        ######################
        # Problem edit menu
        ######################
        else:
            prob_selected = probs_list[prob_index]

            defaults = (
                        ('e', 'edit all relevant fields'),
                        ('c', 'copy the problem'),
                        ('r', 'run the problem'),
                        ('-', ''),
                        ('t', 'edit title'),
                        ('x', 'edit text description'),
                        ('g', 'edit signature'),
                        ('s', 'edit solution'),
                        ('u', 'edit unit test'),
                        ('+', 'increase tier'),
                        ('-', 'decrease tier'),
                        ('[', 'previous problem'),
                        (']', 'next problem'),
                        ('q', 'quit/return'))
            title = ( "Prob Selected:  tier: {}\n"
                      "  title: {}\n"
                      "  signature: {}\n"
                      "  text: \n"
                      "{}".format( prob_selected['tier'],
                                   prob_selected['title'],
                                   prob_selected['signature'],
                                   prob_selected['text'] ) )
            choice = promptMenu(title, [], defaults)
            print("Choice was:", (choice,))
            #time.sleep(2)
            if choice.isdigit():
                pass

            # Edit problem title
            elif choice == 't':
                prob_selected['title'] = input("New Title: ")

            # Edit problem signature
            elif choice == 'g':
                prob_selected['signature'] = input("New Signature: ")

            # Edit text description
            elif choice == 'x':
                prob_selected['text'] = editTempFile(prob_selected['text'])
            
            elif choice == 's':
                prob_selected['solution'] = editTempFile(
                                                prob_selected['solution'],
                                                prob_selected['text'] )

            # Edit unit tests
            elif choice == 'u':
                edit_keys = ('unittests', 'imports', 'setup', 'teardown')
                content = mergeEditYml(prob_selected, edit_keys)
                for key in edit_keys:
                    prob_selected[key] = content[key]

            # Edit all relevant fields
            elif choice == 'e':
                edit_keys = ('uuid', 'title', 'text', 'signature',
                             'solution', 'tier', 'tags',
                             'unittests', 'imports', 'setup', 'teardown')
                content = mergeEditYml(prob_selected, edit_keys)
                for key in edit_keys:
                    prob_selected[key] = content[key]

            # Copy the current problem
            elif choice == 'c':
                probs_list.insert(prob_index+1, copy.deepcopy(prob_selected))
                prob_index += 1
                prob_selected = probs_list[prob_index]
                prob_selected['title'] = prob_selected['title'] + ' copy'
                prob_selected['uuid'] = generateUUID()
                prob_selected['history'] = {}
                prob_selected['ratings'] = {'challenging': 0,
                                            'interesting': 0,
                                            'useful': 0}
            elif choice == '+':
                prob_selected['tier'] += 1
            elif choice == '-':
                prob_selected['tier'] -= 1
            elif choice == '[':
                if prob_index > 0:
                    prob_index -= 1
            elif choice == ']':
                if prob_index < len(probs_list) - 1:
                    prob_index += 1

            elif choice == 'q':
                prob_index = None
                prob_selected = None

def mainFunc():
    probs_files = getProbsFiles()
    probs_lists = {}
    for p_file in probs_files:
        probs_lists[p_file] = readProbsFile(p_file)

    interactiveMenu(probs_lists)


if __name__ == "__main__":
    mainFunc()
