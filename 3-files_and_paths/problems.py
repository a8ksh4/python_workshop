#Opening Files
## Read
def readIt(path_to_file):
    '''given a path to a file, read it's contents and return
    the contents as a string.
    >>> open('./testfile', 'w').write("Just an example file\nwith some stuff in \n it\n")
    
    >>> readIt('./testfile')
    'Just an example file\nwith some stuff in \n it\n'
    '''
    # put code here. 
    return contents


def readLines(path_to_file):
    '''given the path to a file, return it's contents as
    a list of strings, one string for each line in the file.
    The file has unix newline characters: '\n'
    >>> open('./testfile', 'w').write("Just an example file\nwith some stuff in \n it\n")
    
    >>> readIt('./testfile')
    ['Just an example file\n', 'with some stuff in \n', ' it\n']
    '''

def writeIt(path_to_file, contents):
    '''given a file path and a string to be written to the file,
    write contents to the file.
    >>> writeIt('./tsetfile', "Just an example file\nwith some stuff in \n it\n")
    >>> open('./testfile', 'r').read()
    'Just an example file\nwith some stuff in \n it\n'
    '''
    # code goes here.
    # no return statement on this one. 


def moveIt(source_path, destination_path):
    '''given the path to a file and a path to move the file to,
    move the file to the destination path.
    >>> os.path.isfile('./foobar2') and os.remove('./foobar2')
    >>> open('./foobar1', 'w')
    >>> moveIt('./foobar1', './foobar2')
    >>> os.path.isfile('./foobar2')
    True
    '''
    # code goes here. 

def listAlphaFiles():
    '''list files in the current working directory (don't call 
    os.chdir) and return a list of files (or directories or symlinks)
    that have alphabetic names (no numbers or symbols)
    >>> for name in ('aa', 'a1', 'a_', 'b2', '2b', 'bc'):
        open(name, 'w')
    >>> out = listAlphaFiles()
    >>> len(out) == 2 and 'aa' in out and 'bc' in out
    True
    '''
    #your code here
    return list_of_file_names
