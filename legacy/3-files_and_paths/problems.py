#!/usr/bin/env python

global os
import os
global random
import random
global re
import re
global shutil
import shutil
global string
import string

def _randStr(str_len=10):
    return ''.join(random.choices(string.ascii_uppercase, k=str_len))

def moveAFile(src_path, dst_path):
    '''os_basics_1
    Write a function called moveAFile that accepts a source file path and a
    dest file path and moves the file to the destination.
    >>> f0 = './{}'.format(_randStr())
    >>> f1 = './{}'.format(_randStr())
    >>> content = 'asdf'
    >>> len(content) == open(f0, 'w').write(content)
    True
    >>> moveAFile(f0, f1)
    >>> content == (os.path.isfile(f1) and open(f1, 'r').read())
    True
    >>> os.path.isfile(f1) and os.remove(f1) or True
    True
    >>> not (os.path.isfile(f0) and os.remove(f0))
    True
    '''
    shutil.move(src_path, dst_path)
    # return nothing


def cdAndWrite(dir_path, file_name, content):
    '''os_basics_2
    Write a function called cdAndWrite that changes directory to the given
    path, then edits a file and writes the given content to it. Return the
    size of the file in bytes! 
    >>> f0 = './{}'.format(_randStr())
    >>> d0 = './{}'.format(_randStr())
    >>> os.mkdir(d0)
    >>> cwd = os.path.realpath('.')
    >>> content = 'asdf'
    >>> len(content) == cdAndWrite(d0, f0, content)
    True
    >>> './' + os.path.realpath('.').split('/')[-1] == d0
    True
    >>> content == (os.path.isfile(f0) and open(f0, 'r').read())
    True
    >>> os.path.isfile(f0) and os.remove(f0)
    >>> os.chdir(cwd)
    >>> os.path.isdir(d0) and os.rmdir(d0)
    '''
    os.chdir(dir_path)
    open(file_name, 'w').write(content)
    return os.stat(file_name).st_size


def listDirFilter(dir_path, regex_filter):
    '''os_basics_3
    Write a function called listDirFilter that accepts a directory path and a
    regex filter.  It retuns a list of files at the directory path whos names
    match the given regex.  Return only the file names, not their complete
    path. 
    >>> e0 = _randStr()
    >>> e1 = _randStr()
    >>> files = {e0: set(), e1: set()}
    >>> for e in (e0, e1):
    ...     for n in range(5):
    ...         f = "{}.{}".format(n, e)
    ...         files[e].add(f)
    ...         open(f, 'w').close()
    >>> reg_filter = '(./){0,1}[0-9].' + e0
    >>> files[e0] == set(listDirFilter('./', reg_filter))
    True
    >>> for f in list(files[e0]) + list(files[e1]):
    ...     os.remove(f)
    '''
    files_list = []
    for name in os.listdir(dir_path):
        if re.match(regex_filter, name):
            files_list.append(name) 
    return files_list


def createTmpDir(dir_name):
    '''os_basics_4
    Write a function called createTmpDir that accepts a directory name and
    creates it in /tmp.  Set the permissions so that only the directory owner
    can read/write/execute it. Return the complete path to the directory.  
    Bonus: Can you do this in a way that avoids a race condition security
    vulnerability? 
    >>> d0 = ''.join(random.choices(string.ascii_uppercase, k=4))
    >>> p0 = '/tmp/{}'.format(d0)
    >>> out = createTmpDir(d0)
    >>> out == p0
    True
    >>> os.path.isdir(p0) and os.rmdir(p0)
    '''
    #os.umask(0077)
    dir_path = '/tmp/{}'.format(dir_name)
    os.mkdir(dir_path)
    return dir_path


def realPath(dir_name):
    '''os_basics_5
    Write a function called realPath that accepts a path, checks if it has
    any symlinks in it, and returns the actual path (wihout symlinks) to the
    file or directory the original path pointed to. 
    >>> cwd = os.path.realpath('.')
    >>> cwd == realPath('.')
    True
    '''
    real_path = os.path.realpath(dir_name)
    return real_path


#def filePaths(dir_path, files_list):
#    '''os_basics_6
#    Write a function called filePaths that accepts a directory path and a
#    list of files. It returns a list of full paths to those files. 
#    For example, if dir_path is '/tmp/' and files list is ['./foobar.txt',
#    'diddun.txt'], the output would be ['/tmp/foobar.txt', '/tmp/diddun.txt'].
#    '''
#    return files_paths


def readFileToString(file_path):
    '''readwrite_1
    Write a function called readFileToString that accepts a path, opens the
    path, and returns the contents of the file as a string value. You can
    assume that you'll have access to the file, it won't be binary data, you
    don't need to do anything to the given path to open it.  
    >>> f0 = './{}'.format(_randStr())
    >>> c0 = '{}\\n{}\\n'.format(_randStr(), _randStr())
    >>> len(c0) == open(f0, 'w').write(c0)
    True
    >>> c0 == readFileToString(f0)
    True
    >>> os.remove(f0)
    '''
    with open(file_path, 'r') as f:
        contents = f.read()
    return contents


def readLinesFromFile(file_path):
    '''readwrite_2
    Write a function called readLinesFromFiles that accepts a path, reads the
    contents, and returns a list of stings for each line in the file. Do not
    include newline characters in the returned strings.
    >>> f0 = './{}'.format(_randStr())
    >>> c0 = "{}\\n{}\\n".format(_randStr(), _randStr())
    >>> len(c0) == open(f0, 'w').write(c0)
    True
    >>> c0.split('\\n') == readLinesFromFile(f0)
    True
    >>> os.remove(f0)
    '''
    contents = []
    with open(file_path, 'r') as f:
        for line in f.read().split('\n'):
            contents.append(line)
    return contents


def appendLineToFile(file_path, content):
    '''readwrite_3
    Write a function called appendLineToFile that accepts a path and a string,
    and writes the string to the end of the file (without modifying the
    existing contents in the file).
    >>> f0 = './{}'.format(_randStr())
    >>> c0 = "{}\\n{}\\n".format(_randStr(), _randStr())
    >>> c1 = _randStr()
    >>> len(c0) == open(f0, 'w').write(c0)
    True
    >>> appendLineToFile(f0, c1)
    >>> c0 + c1 == open(f0, 'r').read()
    True
    >>> os.remove(f0)
    '''
    with open(file_path, 'a') as f:
        f.write(content)
    #return nothing


def truncateWriteFile(file_path, content):
    '''readwrite_4
    Write a function called truncateWriteFile that accepts a path and a
    string, and writes the string to the file, truncating (overwriting) any
    existing content in the file. 
    >>> f0 = './{}'.format(_randStr())
    >>> c0 = "{}\\n{}\\n".format(_randStr(), _randStr())
    >>> c1 = _randStr()
    >>> len(c0) == open(f0, 'w').write(c0)
    True
    >>> truncateWriteFile(f0, c1)
    >>> c1 == open(f0, 'r').read()
    True
    >>> os.remove(f0)
    '''
    with open(file_path, 'w') as f:
        f.write(content)
    #return nothing


def rewriteInLower(source_path, dest_path):
    '''readwrite_5
    Write a function called rewriteInLower that accepts a source and
    destination path.  It reads in the source path, converts the contents to
    all lower case, and writes them to the destination path. 
    >>> f0 = './{}'.format(_randStr())
    >>> f1 = './{}'.format(_randStr())
    >>> c0 = "!{}\\n{}13\\n! #@\\n".format(_randStr(), _randStr()).upper()
    >>> len(c0) == open(f0, 'w').write(c0)
    True
    >>> rewriteInLower(f0, f1)
    >>> os.path.isfile(f0) and os.path.isfile(f1)
    True
    >>> c0.lower() == open(f1, 'r').read()
    True
    >>> os.remove(f0)
    >>> os.remove(f1)
    '''
    with open(source_path, 'r') as f:
        contents = f.read().lower()
    with open(dest_path, 'w') as f:
        f.write(contents)
    #return nothing


if __name__ == '__main__':
    import doctest
    doctest.testmod()
