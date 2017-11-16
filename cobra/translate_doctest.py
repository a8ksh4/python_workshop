#!/usr/bin/env python

import sys
import yaml

#def getFolders(base_path):
#    for item in os.path.list(base_path):
#        ipath = "{}/{}".format(base_path, item)
#        if os.path.isdir():
#            pass


def pull_probs(fpath):
    lines = open(fpath).read().split('\n')

    probs = {'PRE': []}

    loc = 'PRE'
    for line in lines[1:]:
        if line.startswith('if __name__ =='):
            break
        elif loc != 'PRE' and not line.strip():
            continue
        elif line.startswith('def ') and not line.startswith('def _'):
            loc = line.split()[1].split('(')[0]
            probs[loc] = []
        print(loc, line)
        probs[loc].append(line)

    pre = probs.pop('PRE')
    return pre, probs


def grokProb(pre, prob_lines):
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
            loc = 'posttest'
        elif line.strip() in ("'''", '"""'):
            loc = 'solution'
            prob[loc] = [prob['signature'].split(' -> ')[0], ]
            continue

        # initialize any missing keys
        if loc not in prob:
            prob[loc] = []

        # cleanup specific data
        if loc in ('text', ):
            line = line.strip()
        elif loc == 'posttest':
            if line.startswith('    >>> '):
                line = line[8:]
            else:
                line = line[4:]

        print(prob['title'], loc, line)
        prob[loc].append(line)

    # adapt test code around self.test_results
    test = [ n.strip()[4:] if n.startswith('    >>> ') else n.strip()
                     for n in prob['posttest'] ] + [None,]

    # generate post test starting with function definition line
    prob['posttest'] = []
    skipone = False
    for n, line in enumerate(test[:-1]):
        if skipone:
            skipone = False
            continue
        nline = test[n+1]
        if nline == 'True':
            line = 'self.test_results.append({})'.format(line)
            skipone = True
        prob['posttest'].append(line)

    for loc in ('text', 'solution', 'posttest'):
        prob[loc] = '\n'.join(prob[loc])
        prob[loc] = prob[loc].replace('{}', '{{}}')

    # add any missing fields needed for the yml format...
    prob['unittests'] = {}
    prob['tags'] = ''
    prob['setup'] = ''
    prob['pretest'] = ''
    prob['teardown'] = ''

    return prob


def translate(pre, probs):
    out = {}
    for key, prob in probs.items():
        out[key] = grokProb(pre, prob)
    return yaml.dump(out, default_flow_style=False)

if __name__ == '__main__':
    doctest_file = sys.argv[1]
    yml_file = sys.argv[2]
    print("DOCTEST FILE:", doctest_file)
    print("YML FILE:", yml_file)

    PRE, probs = pull_probs(doctest_file)
    print("PRE:")
    print(PRE)
    print("PROBS keys:", probs.keys())

    yml_data = translate(PRE, probs)

    open(yml_file, 'w').write(yml_data)
