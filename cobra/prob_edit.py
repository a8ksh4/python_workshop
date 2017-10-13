#!/usr/bin/env python

import os
import yaml

EDITOR='/usr/bin/vi'

def getProbFiles():
    return ['some_probs.yml',]

def readProbsFile(problem_file):
    return yaml.load(open(problem_file, 'r'))

def promptMenu(title, options, defaults=None):
    if not defaults:
        defaults = (('n', 'next'),
                    ('p', 'previous'),
                    ('q', 'quit/return'))
    valid_choices = [str(n) for n in range(len(options))]
    valid_choices += [n for n, o in defaults]

    print "\n --- {} ---".format(title)
    for n, option in enumerate(options):
        print "  {} {}".format(n, option)
    print ""
    for n, option in defaults:
        print "  {} {}".format(n, option)
    print ""

    for guess in (1, 2, 3):
        answer = str(input("Select: "))
        if answer not in valid_choices:
            print "Invalid.  Optoins are:", valid_choices
            continue
        break
    else:
        return None
    return answer


def interactiveMenu(prob_sets):
    prob_set_name = None
    prob_set = None
    prob_id = None
    while True:
        os.system('clear')

        # Chose a problem file
        if not prob_set_name:
            defaults = (('q', 'quit/return'), )
            title = "Choose a problem file:"
            choice = promptMenu(title, prob_sets.keys(), defaults)
            print "CHOICE Was:", choice
            if choice == None:
                break
            elif choice.isdigit():
                prob_set_name = prob_sets.keys()[int(choice)]
                prob_set = prob_sets[prob_set_name]
            elif choice == 'q':
                print "Quitting this fine program!"
                break

        # Chose a problem
        elif not prob_id:
            defaults = (('c', 'create new problem'),
                        ('n', 'next problem file'),
                        ('p', 'previous problem file'),
                        ('q', 'quit/return'))
            title = "Choose a problem to work on from '{}':".format(
                                                        prob_set_name)
            prob_files = ['a', 'b', 'c']
            choice = promptMenu(title, prob_files, defaults)
            if choice.isdigit():
                pass
            elif choice == 'c':
                pass
            elif choice == 'n':
                pass
            elif choice == 'p':
                pass
            elif choice == 'q':
                prob_set_name = None
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
                                                        prob_set_name)
            choice = promptMenu(title, prob_files, defaults)
            if choice.isdigit():
                pass
            elif choice == 'c':
                pass
            elif choice == 'n':

def mainFunc():
    prob_files = getProbFiles()
    prob_sets = {}
    for p_file in prob_files:
        prob_sets[p_file] = readProbsFile(p_file)

    interactiveMenu(prob_sets)


if __name__ == "__main__":
    mainFunc()
