#!/usr/bin/env python

import argparse
import os
import random
import re
import shutil
import string
import subprocess as sp
import sys

DATA_C = '''name,age,favorite_color
dan,90,green
fred,11,yellow
amy,22.2,orange'''


DATA_LD = [{'directive': 'install', 'name': 'module1'},
           {'directive': 'remove', 'name': 'module2'},
           {'directive': 'tbd', 'name': 'foobar'}]

DATA_LDL = [ {'content': [{'desc': 'foo', 'name': 'prob1'},
                          {'desc': 'foo2', 'name': 'prob2'}],
              'module': 'python basics'},
             {'content': [{'desc': 'foo3', 'name': 'prob 1'}],
              'module': 'python advanced'} ]

def _texp(func, item, cond=True):
    if not cond:
        return item
    try:
        return func(item)
    except:
        return item

def _csvToAr(data, num=False):
    rows = [r.strip().split(',') for r in data.split('\n') if r.strip()]
    rows = [ [_texp(float, c, num) for c in r] for r in rows ]
    rows = [ [_texp(int, c, (isinstance(c, float) and c%1==0))
                    for c in r] for r in rows ]
    return rows

def _arToCsv(data):
    rows = [','.join([str(c) for c in r if r]) for r in data]
    return '\n'.join(rows)

def _csvToDic(data):
    rows = data.split('\n')
    rows = [r.split(',') for r in rows if r.strip()]
    keys = rows.pop(0)
    return [dict(zip(keys, r)) for r in rows]

def _dicToCsv(data):
    keys = data[0].keys()
    rows = [','.join([r[k] for k in keys]) for r in data]
    return '\n'.join(rows)

def _randStr(str_len=10):
    return ''.join(random.choices(string.ascii_uppercase, k=str_len))


def csvFileToArray(csv_path):
    '''data_1
    Write a function called csvFileToArray that reads in csv data from a
    given path and converts it to an array (list of lists).  Convert all
    strings to upper case and convert any numbers to int or float as
    appropraite.
    >>> f0 = _randStr()
    >>> len(DATA_C) == open(f0, 'w').write(DATA_C)
    True
    >>> out = csvFileToArray(f0)
    >>> _csvToAr(DATA_C.upper(), True) == out
    True
    >>> os.remove(f0)
    '''
    new_array = []
    with open(csv_path, 'r') as f:
        for r in f.readlines():
            row = []
            for col in r.strip().upper().split(','):
                try:
                    col = float(col)
                except:
                    pass
                else:
                    if col%1==0:
                        col = int(col)
                row.append(col)
            new_array.append(row)
    return new_array


def arrayToCSVFile(csv_path, data):
    '''data_2
    Write a function called arrayToCSVFile that takes a list of lists,
    converts them to comma separated strings, and writes the strings, one
    per line, to the given path.
    >>> f0 = _randStr()
    >>> arrayToCSVFile(f0, _csvToAr(DATA_C))
    >>> DATA_C == open(f0, 'r').read().strip()
    True
    >>> os.path.exists(f0) and os.remove(f0)
    '''
    with open(csv_path, 'w') as f:
        for row in data:
            row = [str(c) for c in row]
            row = ','.join(row)
            f.write('{}\n'.format(row))
    #return nothing


def dictToCSVFile(csv_path, data):
    '''data_3
    Write a function called dictToCSV that takes a list of dictionaries,
    each contining the same keys, into csv.  Put the keys in the first line
    as headers for the csv data.
    >>> f0 = _randStr()
    >>> dictToCSVFile(f0, _csvToDic(DATA_C))
    >>> out = open(f0, 'r').read()
    >>> _csvToDic(DATA_C) == _csvToDic(out)
    True
    >>> os.path.exists(f0) and os.remove(f0)
    '''
    keys = data[0].keys()
    with open(csv_path, 'w') as f:
        f.write('{}\n'.format(','.join(keys)))
        for row in data:
            row = [str(row[k]) for k in keys]
            f.write('{}\n'.format(','.join(row)))
    #return nothing






if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #doctest.run_docstring_examples(parseArgs1, globals())
