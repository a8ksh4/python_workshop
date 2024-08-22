#!/usr/bin/env python

import json
import os
import random
import re
import shutil
import string
import yaml

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


def readingFormat(file_path, file_format):
    '''data_4
    Write a function caled readingFormat that accepts a file path to a json
    or yaml formatted file and a string, either "json" or "yaml", and
    reads in the file as the corresponding type and resturns the resulting
    python data structure. 
    >>> f0 = _randStr()
    >>> json.dump(open(f0, 'w'), DATA_LDL)
    >>> DATA_LDL == readingFormat(f0, 'json')
    True
    >>> os.remove(f0)
    >>> f1 = _randStr()
    >>> open(f1, 'w').write(yaml.dump(DATA_LDL))
    >>> DATA_LDL == readingFormat(f1, 'yaml')
    True
    >>> os.remove(f1) 
    '''
    with open(file_path, 'r') as f:
        result_data = yaml.load(f.read())
    return result_data

def writingFormat(file_path, data_object, file_format='json'):
    '''data_5
    Write a function called writingFormat that accepts a file path, a
    python object and a string, either 'json' or 'yaml', and writes
    the data object to the given file path in the corresponding format.
    >>> f0 = _randStr()
    >>> writingFormat(f0, DATA_LDL, 'json')
    >>> DATA_LDL == json.load(open(f0, 'r'))
    True
    >>> os.path.exists(f0) and os.remove(f0)
    >>> writingFormat(f0, DATA_LDL, 'yaml')
    >>> DATA_LDL == yaml.load(open(f0, 'r').read())
    True
    >>> os.remove(f0)
    '''
    if file_format == 'json':
        json.dump(open(file_path, 'w'), data_object)
    elif file_format == 'yaml':
        open(file_path, 'w').write(yaml.dump(data_object))
    #return nothing
           
def somethingWithRegex(content, regex_str):
    '''data_6
    foo
    '''
    pass
    #return bool
           
class dbHandler(extends Object):
    '''Create a class called dbHndler that abstracts interaction with a
    sqlite database into a couple of methods.  On __init__, the path to
    the qslite db is given with the table name to interact with, and,
    optoinally, the headers to create the table with.  If the table does
    not already exist, headers are required or an exceptoin should be raised.
    '''
    def __init__(self, db_path, table_name, headers=None):
        # initialize db cursor
        #self.cursor = foobar
        self.table = table_name
    def writeLine(content):
        '''append a row onto the db table'''
        pass
    def readLines():
        '''return a list of dictoinaries continaing all rows in the table.
        '''
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #doctest.run_docstring_examples(parseArgs1, globals())
