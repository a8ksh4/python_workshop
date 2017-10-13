[Opening Files](#Opening-Files)  
[ToC]  
  
* auto-getn TOC:
{:toc}
  
https://docs.python.org/2/library/filesys.html

# Opening Files
**Reading a file**
```python
In [31]: f = open('foo.yaml', 'r')

In [36]: print f.read()
- module: "python basics"
  content:
  - name: "prob1"
    desc: "foo"
  - name: "prob2"
    desc: "foo2"
- module: "python advanced"
  content:
  - name: "prob 1"
    desc: "foo3"

In [37]: f.close()
```
The "with" convention is more pythonic than opening and closing files as above.  This will ensure that files are only open in the context that they need to be and that they are closed.  Leaving files open is poor form... 
```python
In [38]: with open('blah.csv', 'r') as f:
   ....:     print f.read()
   ....:     
l0c0,l0c1,l0c2
l1c0,l1c1,l1c2
l2c0,l2c1,l2c2

In [39]: 
```  
**Modes**
* r - Open file for reading  
* w - Open file for writing; puts cursor at start of file (truncates file).  
* a - Open file for writing with cursor at end of file (appends file).  
* + - Open file for reading and writing.  
  
**Writing to a file**
```python
In [39]: animals = ('dog', 'moose', 'squirrel', 'cow')

In [40]: with open('the_animals.txt', 'w') as f:
   ....:     for animal in animals:
   ....:         f.write(animal + '\n')
   ....:         

In [42]: print open('the_animals.txt', 'r').readlines()
['dog\n', 'moose\n', 'squirrel\n', 'cow\n']

In [43]: print open('the_animals.txt', 'r').read()
dog
moose
squirrel
cow
```
And with append:
```python
In [44]: with open('the_animals.txt', 'a') as f:
   ....:     for city in ('sac', 'lax', 'slc', 'nyc'):
   ....:         f.write(city + '\n')
   ....:         

In [45]: print open('the_animals.txt', 'r').read()
dog
moose
squirrel
cow
sac
lax
slc
nyc
```

**Create empty file or truncate file**
```python
In [47]: open('newfile.out', 'w').close()
```

# shutil module - High-level file operations
https://docs.python.org/2/library/shutil.html

**Move a file**
```python
import shutil
src_path = '/tmp/my_file.foo'
dst_path = '/opt/my_file.bar'
shutils.move(src_path, dst_path)
```

**Copy a file**
```python
shutils.copy(src_path, dst_path)
```

# os module
One of the core modules needed for any sysadmin to interact with the local environment and filesystem!  This stuff is frequenly done with system calls and really shouldn't be.  Your code will be much more reliable and maintainable if you os the proper modules and calls for this kind of stuff.  
  
## Basic Operations
* **os.getcwd** - get the current working directory  
* **os.chdir** - change directory  
* **os.listdir** - list contents of a directory. os.walk is more comprehensive alternative to this.  
* **os.mkdir** - create a directory  
* **os.remove** - remove a file  
```python
In [66]: os.getcwd()
Out[66]: '/tmp'

In [67]: os.chdir('/tmp/foobar')

In [68]: os.getcwd()
Out[68]: '/tmp/foobar'

In [108]: os.listdir('.')
Out[108]: ['afile.txt']

In [109]: os.mkdir('new_directory')

In [110]: os.remove('afile.txt')

In [111]: os.listdir('.')
Out[111]: ['new_directory']

In [112]: 
In [108]: os.listdir('.')
Out[108]: ['afile.txt']

In [109]: os.mkdir('new_directory')

In [110]: os.remove('afile.txt')

In [111]: os.listdir('.')
Out[111]: ['new_directory']
```
* **os.rmdir** - remove a directory
* **os.symlnik** - create a symlink
* **os.umask** - set the umask: set permissions that are removed from newly created filesystem objects
* **os.walk**

## Permissions and stat

**os.chroot** - change root directory to some path:  E.g. make your script think that a temporary working directory is the root directory ('/').  **This needs testing/verification for an example**  
**os.chown** - change file/dir ownership  
**os.chmod** - change file/dir permissions.  
**os.stat** - get filesystem data for some path  
  
*There are a bunch of useful os._ commands... to be discussed later.  Do dir(os), or type os and press \<tab\> in your ipython terminal*  
  
  
If a path does not exist, an "OSError" exception is raised:  
```python
try:
    os.chdir(path)
except OSError:
    print "path does not exist: {}".format(path)
```

## os.path
**os.path.join**  
os.path.join(path, *paths)  
  
**os.path.realpath** - Real path of a file - traverse symlinks and find where it really is.  
```python
In [57]: p = '/home/thedude/Games/'

In [58]: os.path.realpath(p)
Out[58]: '/media/md0/thedude-extra/Games'
```
**os.path.basename** - name of file at end of a given path
**os.path.dirname** - all of a given path except for the file name at the end

**Real path of running script**
I use this all the time since my scripts are usually run from other directories and I can't count on the current working directory to be the same as the directory my script is in.  So get the script directory and then append it to access any other content/utilities that are in subdirectories, etc.  

```
desktop:~/git/python_class$ cat script_paths_example.py 
#!/usr/bin/env python

import doctest
import os

MY_PATH = os.path.realpath(__file__)
MY_FILENAME = os.path.basename(MY_PATH)
MY_DIR = os.path.dirname(MY_PATH)

if __name__ == '__main__':
    print "My path is:", MY_PATH
    print "My filename is:", MY_FILENAME
    
desktop:~/git/python_class$ ./script_paths_example.py 
My path is: /home/thedude/git/python_class/script_path_example.py
My filename is: script_path_example.py
My dir is: /home/thedude/git/python_class
desktop:~/git/python_class$ 

```

**Tests**
`os.path.isfile(my_path)` - True if it path is a file
`os.path.isdir(my_path)` - True if path is a directory
`os.path.islink(my_path)` - True if path is a symlink
`os.path.ismount(my_path)` - True if path is a mount point

```python
def cdToSymlinkDir(sym_path):
    '''given a symlink path to a file or directory,
    identify the real path to that object and cd
    to it. Raise exception if given pth is not a symlink'''
    if not os.path.islink(sym_path):
        raise IOError('symlink expected: {}'.format(sym_path))
    target_file = os.path.realpath(sym_path)
    target_dir = os.path.dirname(target_file)
    os.path.cd(target_dir)
    return target_file
```

create/destroy
shutil
shutil.copyfile(src, dst)
shutil.movefile(src, dst)


filecmp
os
os.chdir
os.path.isfile
os.path.isdir
os.makedirs
os.path.exists
os.access
    if not ( os.access('/tmp', os.R_OK) and
             os.access('/tmp', os.W_OK) and
             os.access('/tmp', os.X_OK)):
        raise IOError("/tmp permissions err!")
os.chown(os.path.join(root, momo), make_uid, -1)
CWF = os.path.realpath(__file__)
CWD = os.path.dirname(CWF)

**os.tmpfile** - return a temporary file object





permissions

