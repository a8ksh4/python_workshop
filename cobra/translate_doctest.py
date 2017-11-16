#!/usr/bin/env python

import sys

#def getFolders(base_path):
#    for item in os.path.list(base_path):
#        ipath = "{}/{}".format(base_path, item)
#        if os.path.isdir():
#            pass


def pull_probs(fpath):
    lines = open(fpath).read().split('\n')

    PRE = []
    probs = {}

    loc = 'PRE'
    for line in lines:
        if line.startswith('#'):
            continue
        elif line.startswith('if __name__ =='):
            break
        elif line.startswith('dev _'):
            loc = line.split()[1].split('(')[0]
            probs[loc] == []
            probs[loc].append(line)
        elif loc == 'PRE':
            PRE.append(line)
        elif line.startswith('    return') or line.startswith('    #return'):
            probs[loc].append(line)
            loc = 'skip'
        elif loc == 'skip'
            pass
        else:
            probs[loc].append(line)
    return PRE, probs


def grokProb(prob_lines, pre):
    '''takes the text from the entire function definition of a problem
    and solution and converts it into a dictoinary with all of the
    parts needed to make a yml representation of it for the tool'''
    assert(prob_lines[1].startswith("    '''"))
    assert(len(prob_lines) > 8)

    # everything in pre gets executed in the library code block
    prob = {'imports': '\n'.join(pre) }
    prob['signature'] = '{} -> {}'.format(prob_lines[0], prob_lines[-1])
    #prob['name'] = definition.split()[1].split('(')[0]
    prob['title'] = prob_lines[1].split("'")[3].strip()
   
    loc = 'text' 
    for line in prob_lines[2:]:
        if line.strip().startswith('>>>'):
            loc == 'posttest'
        elif line.strip() in ("'''", '"""'):
            loc == 'solution'
            continue

        if loc not in prob:
            prob[loc] == []
        prob[loc].append(line)

    # adapt test code around self.test_results
    test = [ n.strip() for n in prob['posttest'] + [None,] ]
    prob['posttest'] = []
    for n, line in enumerate(test[:-1]):
        nline = test[n+1]
        if nline = 'True':
            line = 'self.test_results.append({})'.format(line))
        prob['posttest'].append(line)

    for loc in ('text', 'solution', 'posttest'):
        prob[loc] = '\n'.join(prob[loc])
        prob[loc] = prob[loc].substitute('{}', '{{}}')

    # add any missing fields needed for the yml format...
    prob['unittests'] = 'skip'
    prob['tags'] = ''
    prob['setup'] = ''
    prob['pretest'] = ''

    return prob


def translate(pre, probs):

if __name__ == '__main__':
    doctest_file = sys.argv[1]
    yml_file = sys.argv[2]

    PRE, probs = pull_probs(doctest_file)

    yml_data = translate(PRE, probs)

    open(yml_file, 'w').write(yml_data)
