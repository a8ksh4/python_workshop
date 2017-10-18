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
```
**Setting the env PATH**
The PATH variable defines where the system looks for executables when you run a command. In the example below, 'which' is a unix command that says what the path to a command is... it searches each directory in the PATH environment variable and returns the first one that has the command. This is the path that the command would be executed from given the current PATH value.
```python
In [17]: os.environ['PATH']
Out[17]: '/p/foobar/bin:/p/foobar/anaconda:/usr/users/home0/thedude/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/bin/X11:/usr/X11R6/bin:/usr/lib/mit/bin:/usr/lib/mit/sbin:/usr/lib/qt3/bin:/opt/kde3/bin:/usr/local/bin:/usr/common/script:.'

In [18]: import subprocess as sp

In [19]: sp.check_output(['which', 'python'])
Out[19]: '/p/foobar/anaconda/python\n'

In [20]: os.environ['PATH'] = '/bin:/usr/bin:/sbin:/usr/sbin'

In [21]: sp.check_output(['which', 'python'])
Out[21]: '/usr/bin/python\n'
```

**os.getuid, setuid, getgid, setgid**
TBD
```python
foo
```

# sys module and sys.args
# argparse module
# nis and nodes
# platform
# subprocess
