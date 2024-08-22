#!/usr/bin/env python

import argparse
import os
import random
import re
import shutil
import string
import subprocess as sp
import sys

def _randStr(str_len=10):
    return ''.join(random.choices(string.ascii_uppercase, k=str_len))

def getEnvironVariable(var_name):
    '''os_env_1
    Write a function called getEnvironVariable that accepts a string name of
    an env varible and returns the value of that variable or returns None
    if it isn't set in the env. 

    >>> v0 = _randStr()
    >>> v1 = _randStr()
    >>> c0 = _randStr()
    >>> os.environ[v0] = c0
    >>> c0 == getEnvironVariable(v0)
    True
    >>> None == getEnvironVariable(v1)
    True
    >>> c0 == os.environ.pop(v0)
    True
    '''
    if var_name in os.environ:
        return os.environ[var_name]
    else:
        return None


def setEnvironVariable(var_name, content):
    '''os_env_2
    Write a function called setEnvironVariable that accepts a string name of
    an env varible and and a value and sets the environment variable with
    that value.

    >>> v0 = _randStr()
    >>> c0 = _randStr()
    >>> setEnvironVariable(v0, c0)
    >>> c0 == os.environ[v0]
    True
    >>> c0 == os.environ.pop(v0)
    True
    '''
    os.environ[var_name] = content


def editEnvPath(new_paths, prepend=False, append=False):
    '''os_env_3
    Given one or more new paths in a tuple, "new_paths", and either append
    or prepend being True; either append or prepend the new paths to the
    environment PATH varialbe.  If prepend and append are both either False
    or True, then make no changes to the environment PATH. 

    >>> cur_path = os.environ['PATH']
    >>> p0 = "/{}/{}".format(_randStr(), _randStr())
    >>> p1 = "/{}/{}".format(_randStr(), _randStr())
    >>> p2 = "/{}/{}".format(_randStr(), _randStr())
    >>> np = [p0, p1, p2]
    >>> nps = os.path.pathsep.join(np)
    >>> tpl = "{}{}{}"
    >>> editEnvPath(np, prepend=True)
    >>> os.environ['PATH'] == tpl.format(nps, os.path.pathsep, cur_path)
    True
    >>> os.environ['PATH'] = cur_path
    >>> editEnvPath(np, append=True)
    >>> os.environ['PATH'] == tpl.format(cur_path, os.path.pathsep, nps)
    True
    >>> os.environ['PATH'] = cur_path
    >>> editEnvPath(np)
    >>> os.environ['PATH'] == cur_path
    True
    >>> os.environ['PATH'] = cur_path
    >>> editEnvPath(np, append=True, prepend=True)
    >>> os.environ['PATH'] == cur_path
    True
    '''
    cur_paths = os.environ['PATH'].split(os.path.pathsep)
    if prepend == append:
        updated_paths = cur_paths
    elif prepend:
        updated_paths = new_paths + cur_paths
    elif append:
        updated_paths = cur_paths + new_paths
    os.environ['PATH'] = os.path.pathsep.join(updated_paths)

def _dirName():
    my_arg_path = sys.argv[0]
    my_realpath = os.path.realpath(my_arg_path)
    my_realpath = my_realpath.split('/')
    my_name = my_realpath[-1]
    my_dir = '/'.join(my_realpath[:-1])
    return (my_dir, my_name)

def getScriptLocName():
    '''sys_basics_1
    Use sys.argv to get and return both the path to the script that's running
    and the file name of the script together in a tuple. 

    >>> sdir, sname = getScriptLocName()
    >>> udir, uname = _dirName()
    >>> sdir == udir
    True
    >>> sname == uname
    True
    '''
    my_arg_path = sys.argv[0]
    my_realpath = os.path.realpath(my_arg_path)
    my_realpath = my_realpath.split('/')
    my_name = my_realpath[-1]
    my_dir = '/'.join(my_realpath[:-1])
    return (my_dir, my_name)


def checkDebugArg():
    '''sys_args_1
    Write a function called checkDebugArg that will check the arguments that
    the script was run with (look at sys.argv) to see if there is a '-d' or
    '--debug' argument given.  If so, return True, else return False.

    >>> cur_argv = sys.argv
    >>> sys.argv = [cur_argv[0], ]
    >>> checkDebugArg()
    False
    >>> sys.argv = [cur_argv[0], 'foo', '-d', 'bar']
    >>> checkDebugArg()
    True
    >>> sys.argv = [cur_argv[0], 'foo', '--debug', 'bar']
    >>> checkDebugArg()
    True
    >>> sys.argv = [cur_argv[0], 'foo', 'd', 'debug']
    >>> checkDebugArg()
    False
    >>> sys.argv = cur_argv
    '''
    if '-d' in sys.argv or '--debug' in sys.argv:
        return True
    else:
        return False


def parseArgs1():
    '''sys_args_1
    Write a function called parseArgs1 that will check the arguments that the
    script was run with (look at sys.argv) and build a dictionary describing
    the given arguments that match this format:
      $ my_script.py [--num_tries <num>] [--user_name <name>] [--fail_message
                                                                    <message>]
    The args may be given in any order and all of them are optoinal, but if
    given, the corresponding value must be there. If an arg, like
    --num_tries, is followed by a value starting with '--', then it is assumed
    that what follows is another arg, not a value, so this would be an error.
    If an unknown arg is given, this is also an error. If any error is
    encountered, return None rather than the dictionary. 

    Return a dictionary like {'num_tries': ..., 'user_name': ..., 
    'fail_message': ...} with either given values for each argument, or None
    if the arg was not given.
    >>> old = list(sys.argv)
    >>> sys.argv += ['--num_tries', '2']
    >>> foo = {'num_tries': '2', 'user_name': None, 'fail_message': None}
    >>> bar = parseArgs1()
    >>> foo == bar
    True
    >>> sys.argv += ['--user_name', 'dan tehman']
    >>> foo['user_name'] = 'dan tehman'
    >>> bar = parseArgs1()
    >>> foo == bar
    True
    >>> sys.argv += ['--fail_message', 'oh the horror']
    >>> foo['fail_message'] = 'oh the horror'
    >>> bar = parseArgs1()
    >>> foo == bar
    True
    >>> sys.argv += ['--invalid', 'oh no']
    >>> bar = parseArgs1()
    >>> bar == None
    True
    >>> sys.argv = old
    '''
    out = {'num_tries': None, 'user_name': None, 'fail_message': None}
    if len(sys.argv) == 1:
        return out
    elif len(sys.argv)%2 != 1:
        return None
    keys = [sys.argv[n] for n in range(1, len(sys.argv), 2)]
    vals = [sys.argv[n] for n in range(2, len(sys.argv), 2)]
    for key, val in zip(keys, vals):
        if key not in ('--num_tries', '--user_name', '--fail_message'):
            return None
        if val.startswith('--'):
            return None
        key = key[2:]
        out[key] = val
    return out


def parseArgs2():
    '''sys_args_2
    Same requirements as the parseArgs1 problem, except implement it using the
    argparse module.  Put your function in it's own script to test; check out
    the --help output, for fun. 

    argparse returns a "Namespace" that behaves like a dictionary.  This is
    all that needs to be returned. 

    For example, if the user gives the arguments "--num_tries 2", the function
    should return:
        Namespace(fail_message=None, num_tries=2, user_name=None)

    >>> old = list(sys.argv)
    >>> sys.argv += ['--num_tries', '2']
    >>> foo = argparse.Namespace()
    >>> foo.fail_message = None
    >>> foo.user_name = None
    >>> foo.num_tries = 2
    >>> bar = parseArgs2()
    >>> foo == bar
    True
    >>> sys.argv += ['--user_name', 'dan tehman']
    >>> foo.user_name = 'dan tehman'
    >>> bar = parseArgs2()
    >>> foo == bar
    True
    >>> sys.argv += ['--fail_message', 'oh the horror']
    >>> foo.fail_message = 'oh the horror'
    >>> bar = parseArgs2()
    >>> foo == bar
    True
    >>> sys.argv = list(old)
    >>> sys.argv += ['--invalid', 'oh no']
    >>> old_stderr = sys.stderr
    >>> sys.stderr = open('/dev/null', 'w')
    >>> parseArgs2()
    Traceback (most recent call last):
      ...
    SystemExit: 2
    >>> sys.stderr.close()
    >>> sys.stderr = old_stderr
    >>> sys.argv = old

    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_tries', help="how many tries",
                        type=int, action='store')
    parser.add_argument('--user_name', help="name of user",
                        type=str, action='store')
    parser.add_argument('--fail_message', help="message for failure",
                        type=str, action='store')
    args = parser.parse_args()
    return args


def runGetOutputShell(command):
    '''subprocess_1
    Write a function called runGetOuputShell that will use the subprocess
    module (imported as "sp" for you) to run a given command and return
    its ouptut as a string. Assume that the command will be given as a string
    and set shell=True when you run it. 
    >>> out = runGetOutputShell('/usr/bin/whoami').decode("utf-8").strip()
    >>> os.getlogin() == out
    True
    '''
    return sp.check_output(command, shell=True)


def runGetOutput(command):
    '''subprocess_2
    Write a function called runGetOutput that uses the subprocess module
    (imported for you as "sp") to run a given command formatted as a list
    (how you should do this normally) and return its output as a string.
    Aka, do not specify "shell=..." in your sp call.
    >>> out = runGetOutputShell(['/usr/bin/whoami',]).decode("utf-8").strip()
    >>> os.getlogin() == out
    True
    '''
    return sp.check_output(command)


def runGetStatus(command):
    '''subprocess_3
    Write a function called runGetStatus that uses the subprocess module
    (imported for you as "sp") to run a given command (formatted as a list)
    and return True if the command's exit status is 0 or False otherwise. 
    >>> runGetStatus(['/bin/true',])
    True
    >>> runGetStatus(['/bin/false',])
    False
    '''
    return 0 == sp.call(command)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #doctest.run_docstring_examples(parseArgs1, globals())
