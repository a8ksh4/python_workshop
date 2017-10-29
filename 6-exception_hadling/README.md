INDEX:


# Strategy
We always want our code to fail gracefully. Two strategies for deialing with errors in python are:
* Check requirements before execution
  * Possible to introduce race conditions.
  * Did we think of all possible issues?
  * You can't predict everything... 
* Use Try-Except blocks
  * _Can_ be slower than the alternative w/o try block.  This isn't generally a good reason. 
  * Takes some research/experimentation to figure out which errors to look for. 
  * Improve code readability
  
**References**
* https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/
* 

# Handling Exceptions
  
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
* "**try**" - this is that bit of code that we expect may fail.  
* "**except**" - what to do when it fails.  Note that we can have multiple except blocks 
  that each handle a different exception with different actions
* "**raise**" - this re-raises the caught exception, which would be caught again by 
  whatever called our current function/context.  You can raise a different exception
  than was caught, if needed. 
* "**else**" - this is run if an exception is NOT raised. 
* "**finally**" - this always gets run at the end of the try block, except if we call raise from 
  somewhere above and leave our current context. 
  
## Multiple Exceptions
Any partucular command you call can raise a variety of exceptions to indicate what flavor of problem that it ran into.
What you actually chose to handle depends on the problem at hand. You may simply want to catch "Exception" because you
really only care to know that there was a problem, and not what the problem was.  
  
**Handling Each Exception Explicitly:**
This is self explanitory, right?  You can see why this might be useful?  ;)
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

**Handling Multiple Exceptions togethr:**
If you'll perform the same action for multiple exceptions, you can lump them together.  
```python
my_cmd = ['/bin/ls', '-ld', '/asdf']
try:
    output = sp.check_output(my_cmd)
    print("OUTPUT WAS:", output)
except (FileNotFoundError, PermissionError, KeyboardInterrupt):
    print("Blame the user!")
```

## Typecasting
```python
def print_object(some_object):
    # Check if the object is printable...
    try:
        printable = str(some_object)
    except TypeError:
        print("unprintable object")
    else:
        print(printable)
```

## General Exceptions
```python
def somethingWithDivision(a, b):
  return a / b

spam = 0
try: 
    somethingWithDivision(1, spam)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except NameError:
    print("spam variable was never defined!")
except TypeError:
    print("object referred to by spam was not an int or float")
```
    
# Raising Exceptions
You can always raise "**Exception**", optoinally with an included message. 
```python
In [18]: def doTheThing(thing, sudo=False):
    ...:     if not sudo:
    ...:         raise Exception("Make it yourself!")
    ...:     thing()
    ...:     

In [19]: def constructSammich():
    ...:     print("making a sammich")
    ...:     

In [20]: doTheThing(constructSammich, True)
making a sammich

In [21]: doTheThing(constructSammich)
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
<ipython-input-21-ad1feb7d9c76> in <module>()
----> 1 doTheThing(constructSammich)

<ipython-input-18-a02152bd30ee> in doTheThing(thing, sudo)
      1 def doTheThing(thing, sudo=False):
      2     if not sudo:
----> 3         raise Exception("Make it yourself!")
      4     thing()
      5 

Exception: Make it yourself!
```

## Built-In Exceptions
https://docs.python.org/3/library/exceptions.html  
All exceptions extend the "BaseExceptoin" class.  
  
**Base Classes**  
These all extend BaseException, and are what all other exceptions usually are built on. 
* Exception
* ArithmeticError
* BufferError
* LookupError
  
**Concrete Exceptois**
* AssertionError
* AttributeError
* EOFError
* FloatingPointError
* GeneratorExit
* ImportError
* ModuleNotFondError
* IndexError
* KeyError
* KeyboardInterrupt
* MemoryError
* NameError
* NotImplementedError
* OSError
* ...

## User-defined Exceptions
https://docs.python.org/3.3/tutorial/errors.html#user-defined-exceptions
