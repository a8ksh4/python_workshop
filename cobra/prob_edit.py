#!/usr/bin/env python

# Python2 compatibility:
from __future__ import print_function
from future.builtins import input

# Other imports:
from glob import glob
import operator
import os
import shutil
import yaml


EDITOR='/usr/bin/vi'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def getProbsFiles():
    return glob('*.yml')

def readProbsFile(problem_file):
    probs_dict = yaml.load(open(problem_file, 'r'))
    # translate to list for more simple interaction
    probs_list = []
    for uuid, prob in probs_dict.items():
        prob['uuid'] = uuid
        probs_list.append(prob)
    probs_list = sorted(probs_list, operator.attrgetter('uuid'))
    probs_list = sorted(probs_list, operator.attrgetter('title'))
    probs_list = sorted(probs_list, operator.attrgetter('tier'))
    return probs_list

def writeProbsFile(problem_file, probs_list):
    epoch_seconds = int(time.time())
    shutil.copy(problem_file, "{}_{}".format(problem_file, epoch_seconds))
    # translate back into dict for storage
    probs_dict = {}
    for prob in probs_list:
        probs_dict[prob['uuid']] = prob
    open(problem_file, 'w').write(yaml.dump(probs_dict))

def promptMenu(title, options, defaults=None):
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
        answer = str(input("Select: "))
        if answer not in valid_choices:
            print("Invalid.  Optoins are:", valid_choices)
            continue
        break
    else:
        return None
    return answer


def interactiveMenu(probs_lists):
    probs_list_name = None
    probs_list = None
    prob_id = None
    while True:
        cls()

        # Chose a problem file
        if not probs_list_name:
            defaults = (('q', 'quit/return'), )
            title = "Choose a problem file:"
            choice = promptMenu(title, probs_lists.keys(), defaults)
            print("CHOICE Was:", choice)
            if choice == None:
                break
            elif choice.isdigit():
                probs_list_name = list(probs_lists.keys())[int(choice)]
                probs_list = probs_lists[probs_list_name]
            elif choice == 'q':
                print("Quitting this fine program!")
                break

        # Chose a problem
        elif not prob_id:
            defaults = (('c', 'create new problem'),
                        ('n', 'next problem file'),
                        ('p', 'previous problem file'),
                        ('+', 'increase tier'),
                        ('-', 'decrease tier'),
                        ('q', 'quit/return'))
            title = "Choose a problem to work on from '{}':".format(
                                                        probs_list_name)
            probs_titles = [(p['tier'],p['title']) for p in probs_list]
            choice = promptMenu(title, probs_titles, defaults)
            if choice.isdigit():
                pass
            elif choice == 'c':
                pass
            elif choice == 'n':
                pass
            elif choice == 'p':
                pass
            elif choice == 'q':
                probs_list_name = None
                continue

        # Problem edit menu
        else:
            defaults = (('t', 'edit title'),
                        ('b', 'edit body (problem text)'),
                        ('s', 'edit solution'),
                        ('u', 'edit unit test'),
                        ('r', 'run the problem'),
                        ('q', 'quit/return'))
            title = "Choose a problem to work on from '{}':".format(
                                                        probs_list_name)
            choice = promptMenu(title, probs_files, defaults)
            if choice.isdigit():
                pass
            elif choice == 'c':
                pass
            elif choice == 'n':
                pass

def mainFunc():
    probs_files = getProbsFiles()
    probs_lists = {}
    for p_file in probs_files:
        probs_lists[p_file] = readProbsFile(p_file)

    interactiveMenu(probs_lists)


if __name__ == "__main__":
    mainFunc()
