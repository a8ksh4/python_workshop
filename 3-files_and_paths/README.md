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

## os.path
**Paths**
os.path.join(path, *paths)

**Real path of a file (e.g. traverse symlinks and find where it really is**
```python
In [57]: p = '/home/drnorris/Games/'

In [58]: os.path.realpath(p)
Out[58]: '/media/md0/drnorris-extra/Games'
```

**Real path of running script**
```
desktop:~/git/python_class$ cat realpath_example.py 
#!/usr/bin/env python
import os

MY_PATH = os.path.realpath(__file__)

if __name__ == '__main__':
    print "My path is:", MY_PATH

desktop:~/git/python_class$ ./realpath_example.py 
My path is: /home/thedude/git/python_class/realpath_example.py
desktop:~/git/python_class$
```

**Tests**
os.path.isfile(path) - True if it path is a file
os.path.isdir(path) - True if path is a directory
os.path.islink(path) - True if path is a symlink
os.path.ismount(path) - True if path is a mount point

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






permissions

