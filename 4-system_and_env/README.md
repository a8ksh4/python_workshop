# Index:
* [OS and Environ](#os-module-and-environ)
* [sys module and sys.args](#sys-module-and-sys-args)
* [argparse module](#argparse-module)
* [setuid and setgid](#setuid-and-setgid)
* [nis and nodes](#nis-and-nodes)
* [platform module](#platform-module)
* [subprocess module](#subprocess-module)
  
  
https://docs.python.org/2/library/filesys.html  
  
# os module and environ
More os module things that weren't covered in teh files and paths content. What you see set will vary depending on your OS and more...

**os.environ**
Dictionary with all environment variables set when python process was launched. Modify them and any subprocesses will see the changes.
```python
In [6]: for key, val in os.environ.items():
   ...:     print key, ':', val
   ...:     
FVWM_USERDIR : /usr/users/home0/thedude
GROUP : users
REMOTEHOST : 10.121.208.53
MINICOM : -c on
SSH2_TTY : /dev/pts/195
CSHEDIT : emacs
HOSTTYPE : x86_64
...
In [7]: os.environ['MACHTYPE']
Out[7]: 'x86_64-suse-linux'
In [9]: os.environ['foo'] = 'bar'

In [10]: os.environ['foo']
Out[10]: 'bar'

In [30]: os.getenv('foo')
Out[30]: 'bar'

```
**Setting the env PATH**
The PATH variable defines where the system looks for executables when you run a command. In the example below, 'which' is a unix command that says what the path to a command is... it searches each directory in the PATH environment variable and returns the first one that has the command. This is the path that the command would be executed from given the current PATH value.
```python
In [17]: os.environ['PATH']
Out[17]: '/p/foobar/bin:/p/foobar/anaconda:/usr/users/home0/thedude/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/bin/X11:/usr/X11R6/bin:/usr/lib/mit/bin:/usr/lib/mit/sbin:/usr/lib/qt3/bin:/opt/kde3/bin:/usr/local/bin:/usr/common/script:.'

In [18]: import subprocess as sp

In [19]: sp.check_output(['which', 'python'])
Out[19]: '/p/foobar/anaconda/python\n'

In [20]: os.environ['PATH'] = os.pathsep.join(('/bin', '/usr/bin', '/sbin', '/usr/sbin'))

In [21]: sp.check_output(['which', 'python'])
Out[21]: '/usr/bin/python\n'
```
**os.pathsep** - separater used for the PATH varialbe on the system where python is running. 
```python
In [31]: os.pathsep
Out[31]: ':'
```
**os.getuid, setuid, getgid, setgid**
TBD
```python
foo
```

# sys module
Sys has a lot of low-level functionality with info about the running python interpreter, basic environmental stuff, and architecture specific stuff.  It's mostly out of our scope, but a couple of it's modules are important for general usage!  
  
**sys.argv** - list of arguments provided by the user when the python program was executed. 
The first item in this list is always the name of the running program. 
```
myhost:~> cat ~/bin/argtest.py
#!/usr/bin/env python
import sys
print sys.argv

myhost:~> ~/bin/argtest.py first "second stuff" third --fourth "six seven 8"
['/usr/users/home0/drnorris/bin/argtest.py', 'first', 'second stuff', 'third', '--fourth', 'six seven 8']
myhost:~> 
```

**sys.exit**
Call this to exit the program at any point. Give it an exit status to indicate whether or not errors were encountered when the program ran. Zero "0" exit status means success, and non-zero means there was a failure.  This is somewhat in contrast to truth-ness in programming where zero is usually False and non-zero evaluates to True.  
```
myhost:~> cat ~/bin/exittest.py 
#!/usr/bin/env python
import sys
if sys.argv[1] == 'success':
    sys.exit(0)
elif sys.argv[1] == 'failure':
    sys.exit(1)
myhost:~> if ~/bin/exittest.py success; then echo "got 0 exit status for success"; else echo "got non-zero exit status indicating failure"; fi
got 0 exit status for success

myhost:~> if ~/bin/exittest.py failure; then echo "got 0 exit status for success"; else echo "got non-zero exit status indicating failure"; fi
got non-zero exit status indicating failure

myhost:~> 
```
  
**sys.platform** - basic info about what type of system we're running on
```python
In [24]: sys.platform
Out[24]: 'linux2'
```
| System              | platform value |
|---------------------|----------------|
| Linux (2.x and 3.x) |	'linux2'       |
| Windows	            | 'win32'        |
| Windows/Cygwin	    |'cygwin'        |
| Mac OS X	          |'darwin'        |  
*and more...*  
  
**sys.getwindowsversion** - try this on windows...
  
**sys.maxint** - largest possible integer value on this system
```python
In [25]: sys.maxint
Out[25]: 9223372036854775807
```
**sys.floatinfo** - info about floating point representation on this system
```python
In [33]: sys.float_info
Out[33]: sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
```
**sys.getrecursionlimit** - how many function calls deep can your program go? 
```python
In [27]: sys.getrecursionlimit()
Out[27]: 1000
```

# argparse module
# nis and nodes
# platform
# subprocess
