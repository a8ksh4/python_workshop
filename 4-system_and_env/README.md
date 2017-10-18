# Index:
* [os module](#os-module)
  * os.environ
  * os.environ\['PATH'\], os.pathsep
* [sys module](#sys-module)
  * sys.argv
  * sys.exit
  * misc stuff
* [argparse module](#argparse-module)
* [nis module](#nis-module)
* [platform module](#platform-module)
* [subprocess module](#subprocess-module)
  * [shell or no shell](#shell-or-no-shell)
  * [sp.check_output](#sp-check-output)
  * [sp.check_call](#sp-check-call)
  * [sp.Popen](#sp-popen)
    * Popen.poll()
    * Popen.wait()
    * Popen.communicate()
    * Popen.terminate()
    * Popen.kill()
    * stdin, stdout, stderr...
    * Popen.returncode
   
  
  
https://docs.python.org/2/library/filesys.html  
  
# os module
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
  
stuff goes here  
  
# nis module
NIS is Network Information Service - sort of an extensin of the local system passwd, group, netgroup, etc files that are used for tracking users, groups, and other system information.  NIS is a distributed service for this content that's still used in industry today... The usage is pretty simple:
```python
In [36]: import nis

In [37]: nis.match('thedude', 'passwd')
Out[37]: 'thedude:passwordhash:1000:15:just.the.dude:/usr/users/home0/thedude:/bin/bash'

In [38]: nis.match('users', 'group')
Out[38]: 'users::15:thedude,andothers
```
# platform module
Sort of the python equivelant of the uname command.  Also has pointeres to some important libraries that python needs.  
```python
In [53]: import platform

In [54]: platform.uname()
Out[54]: 
('Linux',
 'fmyec0200',
 '3.0.101-107-default',
 '#1 SMP Thu Jun 22 14:37:55 UTC 2017 (414ea9f)',
 'x86_64',
 'x86_64')

In [55]: platform.processor()
Out[55]: 'x86_64'

In [56]: platform.platform()
Out[56]: 'Linux-3.0.101-107-default-x86_64-with-SuSE-11-x86_64'

In [57]: platform.machine()
Out[57]: 'x86_64'

In [58]: platform.system()
Out[58]: 'Linux'

In [59]: platform.release()
Out[59]: '3.0.101-107-default'
```
  
# subprocess module
This is a big one!  This has everything you need (probably) to make system calls from python and execute any random commands needed when your program runs.  
  
It's easy to abuse subprocess - don't use it for thigns that you should be using libraries for, like editing files, permissions, etc.  
  
https://docs.python.org/2/library/subprocess.html#replacing-older-functions-with-the-subprocess-module  
  
## shell or no shell?
  
## sp.check_output
**Use this as a simple way to capture output from a command. **
```python
In [62]: output = sp.check_output(['ls', '-ld', '.'])

In [63]: print output
drwxr-sr-x 53 thedude users 16384 Oct 18 08:56 .

In [64]: 
```
If you pass it an invalid command, it will raise an exception!  This will cause your production code to crash, so you have to either validate your commands before running them, including permiossions to run them, or call them from a try block.
```
In [64]: output = sp.check_output(['zls', '-ld', '.'])
---------------------------------------------------------------------------
OSError                                   Traceback (most recent call last)
<ipython-input-64-7a025d6680d7> in <module>()
----> 1 output = sp.check_output(['zls', '-ld', '.'])
...

OSError: [Errno 2] No such file or directory

In [65]: 
```
The same thing happens if the command you run returns a non-zero exit status!
```python
In [66]: sp.check_output(['false'])
---------------------------------------------------------------------------
CalledProcessError                        Traceback (most recent call last)
<ipython-input-66-ffd39565651e> in <module>()
----> 1 sp.check_output(['false'])
...
CalledProcessError: Command '['false']' returned non-zero exit status 1

In [67]: 

```
Notice the differnet exceptoins raised?  
```python
In [68]: try:
    ...:     sp.check_output(['false'])
    ...: except sp.CalledProcessError, e:
    ...:     print "the command returned non-zer exit status for failure"
    ...: except OSError, e:
    ...:     print "the command was not found or not accessible"
    ...:     
the command returned non-zer exit status for failure

In [69]: 
```
