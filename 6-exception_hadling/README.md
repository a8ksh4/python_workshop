INDEX:


# Strategy
We always want our code to fail gracefully. Two strategies for deialing with errors in python are:
* Check requirements before execution
  * Possible to introduce race conditions.
  * Did we think of all possible issues?
  * You can't predict everything... 
* Use Try-Except blocks
  * Runtime for code in blocks is 2x normal. 
  * Takes some research/experimentation to figure out which errors to look for. 

# Examples
  
## Basic Syntax
```python
try:
    do_some_stuff()
except:
    rollback()
    raise
else:
    commit()
finally:
    cleanup()
```
* "try" - this is that bit of code that we expect may fail.  
* "except" - what to do when it fails.  Note that we can have multiple except blocks 
  that each handle a different exception with different actions
* "raise" - this re-raises the caught exception, which would be caught again by 
  whatever called our current function/context.  You can raise a different exception
  than was caught, if needed. 
* "else" - this is run if an exception is not raised. 
* "finally" - this always gets run at the end of the try block, except if we call raise from 
  somewhere above and leave our current context. 
  
## Multiple Exceptions
Any partucular command you call can raise a variety of exceptions to indicate what flavor of problem that it ran into.
What you actually chose to handle depends on the problem at hand. You may simply want to catch "Exception" because you
really only care to know that there was a problem, and not what the problem was.  
  
```python
my_cmd = ['/bin/ls', '-ld', '/asdf']
try:
    output = sp.check_output(my_cmd)
    print("OUTPUT WAS:", output)
except sp.CalledProcessError as e:
    print("command had non-zero exit status: {}".format(e.returncode))
    print("MESSAGE WAS:", e)
except FileNotFoundError as e:
    print("Path to command incorrect")
    print("MESSAGE WAS:", e)
except PermissionError as e:
    print("No Execute permissions on command")
    print("MESSAGE WAS:", e)
except KeyboardInterrupt:
    print("User pressed ctrl+c")
except Exception as e:
    print("Catch-all for anything else... {}".format(e))
```
