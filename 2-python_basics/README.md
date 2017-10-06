    In [1]: import this
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

    In [2]:

** Note that all examples are using python 2**  
Python 3 differences will be noted periodically  
  
## Variables and Data Types
### Integer, Float, complex
Python 2 keeps integers as integers until a float is introduced.  
Python 3 converts to float during division unless `//` is used instead of `/`.  
  
    In [1]: x = 1

    In [2]: x / 2
    Out[2]: 0

    In [3]: x % 2
    Out[3]: 1

    In [4]: x = 1.0

    In [5]: x / 2
    Out[5]: 0.5

    In [6]: x % 2
    Out[6]: 1.0

Python has built in support for complex numbers.  
    In [7]: m = 2 + 3j
    
    In [8]: 3j * m
    Out[8]: (-9+6j)
  
### Strings
*Press "Tab" to get auto-complete options for a data type in ipython.*  
  
    In [9]: a = "The quick brown fox jumps over the lazy dog"

    In [10]: a.
               a.capitalize a.endswith   a.isalnum    a.istitle    a.lstrip     a.rjust      a.splitlines a.translate
               a.center     a.expandtabs a.isalpha    a.isupper    a.partition  a.rpartition a.startswith a.upper  
               a.count      a.find       a.isdigit    a.join       a.replace    a.rsplit     a.strip      a.zfill  
               a.decode     a.format     a.islower    a.ljust      a.rfind      a.rstrip     a.swapcase            
               a.encode     a.index      a.isspace    a.lower      a.rindex     a.split      a.title
  
**Quoting**  
*ipython (and the regular python repl) will echo the last value returned, even without a print statement.  In a script/program, though, you need to use print to show the value.*
  
Single quotes can contain un-escaped double quotes; double quotes can contain un-escaped single quotes; triple sets of single or double quotes can contain either. All of these can contain escaped qutoes. 
   In [12]: b = '''I can put's the single and "double" quotes inside tripple quotes.'''

    In [13]: b.upper()
    Out[13]: 'I CAN PUT\'S THE SINGLE AND "DOUBLE" QUOTES INSIDE TRIPPLE QUOTES.'

    In [14]: print b
    I can put's the single and "double" quotes inside tripple quotes.
    In [15]: c = 'How\'s it going?'
    
    In [16]: c
    Out[16]: "How's it going?"
  
**Matching**  
    In [17]: 'fox' in a
    Out[17]: True
    
    In [18]: a.index('fox')
    Out[18]: 16
  
*What kinds of things can we do with this?*  
    In [21]: for animal in ('cat', 'dog', 'mouse', 'fox'):
        ...:     location = a.index(animal) if animal in a else 'foobar'
        ...:     print animal, location
        ...:     
    cat foobar
    dog 40
    mouse foobar
    fox 16  
  
**Substrings**  
  
**Split and Join**  


 Syntax
Loops
Lists
Functions
Generators
Classes
Etc!
