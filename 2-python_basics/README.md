* [Variables and Data Types](#variables-and-data-types)
  * [Integer, Float, Complex](#integer--float--complex)
  * [Strings](#strings)
    * Quoting, modifiers, matching, substrings, split, join
  * [Lists and Tuples](#lists-and-tuples)
  * [Sets](#sets)
  * [Dictionaries](#dictionaries)
* [Syntax and Namespace](#syntax-and-namespace)
  * [Loops](#loops)
    * for, for-else, while
  * [List Comprehensions](#list-comprehensions)
  * [Branching](#branching)
  * [Functions](#functions)
  * [Modules](#modules)
  * [Classes](#classes)
  * [Generators](#generators)

```
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
```
** Note that all examples are using python 2**  
Python 3 differences will be noted periodically  
  
# Variables and Data Types
## Integer, Float, complex
Python 2 keeps integers as integers until a float is introduced.  
Python 3 converts to float during division unless `//` is used instead of `/`.  
  
```python
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
```
Python has built in support for complex numbers.  
```python
In [7]: m = 2 + 3j

In [8]: 3j * m
Out[8]: (-9+6j)
```  
## Strings
*Press "Tab" to get auto-complete options for a data type in ipython.*  
```python  
In [9]: a = "The quick brown fox jumps over the lazy dog"

In [10]: a.
           a.capitalize a.endswith   a.isalnum    a.istitle    a.lstrip     a.rjust      a.splitlines a.translate
           a.center     a.expandtabs a.isalpha    a.isupper    a.partition  a.rpartition a.startswith a.upper  
           a.count      a.find       a.isdigit    a.join       a.replace    a.rsplit     a.strip      a.zfill  
           a.decode     a.format     a.islower    a.ljust      a.rfind      a.rstrip     a.swapcase            
           a.encode     a.index      a.isspace    a.lower      a.rindex     a.split      a.title
```
  
String Modifiers - these return a modified string, they do not change the string in place!  
* `strip`, `lstrip`, `rstrip` - remove whitespace from one or both ends of a string
* `upper`, `lower` - convert string to upper or lower case  
  
String Tests:  
* `islower`, `isupper` - return True if all characters in string are lower case or upper case
* `isalpha`, `isdigit`, `isalnum` - return true if all characaters are alphabetic, numeric, or both
* `isspace` - return true if string contains only whitespace  
  
**Quoting**  
*ipython (and the regular python repl) will echo the last value returned, even without a print statement.  In a script/program, though, you need to use print to show the value.*
  
Single quotes can contain un-escaped double quotes; double quotes can contain un-escaped single quotes; triple sets of single or double quotes can contain either. All of these can contain escaped qutoes.  
```python
In [12]: b = '''I can put's the single and "double" quotes inside tripple quotes.'''
In [13]: b.upper()
Out[13]: 'I CAN PUT\'S THE SINGLE AND "DOUBLE" QUOTES INSIDE TRIPPLE QUOTES.'

In [14]: print b
I can put's the single and "double" quotes inside tripple quotes.
In [15]: c = 'How\'s it going?'

In [16]: c
Out[16]: "How's it going?"
```

**Matching**  
```python
In [17]: 'fox' in a
Out[17]: True

In [18]: a.index('fox')
Out[18]: 16
```
  
*What kinds of things can we do with this?*  
```python
In [21]: for animal in ('cat', 'dog', 'mouse', 'fox'):
    ...:     location = a.index(animal) if animal in a else 'foobar'
    ...:     print animal, location
    ...:     
cat foobar
dog 40
mouse foobar
fox 16
```
  
**Substrings**  
*Hey, this works just like with lists!*  
  
```python
In [23]: a[:9]
Out[23]: 'The quick'

In [24]: a[20:]
Out[24]: 'jumps over the lazy dog'

In [25]: a[9:20]
Out[25]: ' brown fox '

In [26]: a[9:20:3]
Out[26]: ' o x'
```  
**Split and Join**  
Split works on whitespace, by default.  Join is a string operation, not a list operation, so we call it from a string that will join whatever we pass to the join commmand (a list or tuple).  

```python
In [30]: b = a.split()
    
In [31]: b
Out[31]: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    
In [32]: '_'.join(b)
Out[32]: 'The_quick_brown_fox_jumps_over_the_lazy_dog'

In [34]: ''.join(a.split())
Out[34]: 'Thequickbrownfoxjumpsoverthelazydog'
```  
Pass a character, or sequence of characters, to split to change the delimeter:  
```python
In [35]: c = 'one,two,3,five,_,foobar'
    
In [36]: c.split()
Out[36]: ['one,two,3,five,_,foobar']

In [37]: c.split(',')
Out[37]: ['one', 'two', '3', 'five', '_', 'foobar']
    
In [38]: c.split(',t')
Out[38]: ['one', 'wo,3,five,_,foobar']
```  
  
## Lists and Tuples  
  
## Sets
  
  
## Dictionaries
Dictionaries, `{key: val, ...}` are used for key value pairing. Most data types can be used for keys and any 
data type can be used for values.
* Keys cannot be lists, sets, dictoinaries, but they can be tuples, strings, numbers...  
* Values can be anything!  Nested dictionaries, lists, functions(!), or any object.  
  
**Creating dictionaries with values**  
```python
In [100]: x = {'key1': 'val1', 'key2': 'val2'}

In [101]: x.keys()
Out[101]: ['key2', 'key1']

In [102]: x.values()
Out[102]: ['val2', 'val1']

In [103]: x.items()
Out[103]: [('key2', 'val2'), ('key1', 'val1')]
```
  
**Creating empty dictionaries**  
```python
In [1]: y = {}

In [2]: y
Out[2]: {}

In [3]: y['foo'] = 'bar'

In [4]: z = dict()

In [5]: z
Out[5]: {}
```

**Creating dictionaries by typecasting - "dict(zip(list1, list2))"**  
You can use "dict()" to typecast a list of lists into a dictionary.  E.g:
```python
In [15]: dict( ((1, 'a'), (2, 'b'), (0, 'c'), (3, [])) )
Out[15]: {0: 'c', 1: 'a', 2: 'b', 3: []}
```
Simiarly, if you typecast a dictionary to a list or tuple, you'll get the reverse:
```python
In [18]: tuple({0: 'c', 1: 'a', 2: 'b', 3: []}.items())
Out[18]: ((0, 'c'), (1, 'a'), (2, 'b'), (3, []))

In [19]: list({0: 'c', 1: 'a', 2: 'b', 3: []}.items())
Out[19]: [(0, 'c'), (1, 'a'), (2, 'b'), (3, [])]
```
The important next step from this is building lists of key:value pairs that can be converted to 
a dictionary. Imagine that you have a list of things, and you iterate over those things
to collect some data into another list.  For every item in the first list, there is some data in the 
other list at the same location in the list.  

"zip" will pair up items in two lists for this. 

```python
In [6]: my_hosts = ('host1', 'host2', 'host3', 'host4')

In [7]: host_status = [getStatus(h) for h in my_hosts]

In [10]: host_status
Out[10]: ['up', 'up', 'down', 'up']

In [20]: zip(my_hosts, host_status)
Out[20]: [('host1', 'up'), ('host2', 'up'), ('host3', 'down'), ('host4', 'up')]

In [11]: status_by_host = dict(zip(my_hosts, host_status))

In [12]: status_by_host
Out[12]: {'host1': 'up', 'host2': 'up', 'host3': 'down', 'host4': 'up'}

In [13]: status_by_host['host1']
Out[13]: 'up'
```
  
**Inserting and modifying values**  
If the key already exists in the dictionary, it's value will be overwritten.  If the key doesn't exist already,
it will be inserted with the given value.
```python
some_dictionary[the_key] = the_value
```
  
**Referencing values**  
If you reference a key that doesn't exist in the dictionary, an exception will be raised, so it's typical to check
for keys before referencing them, unless you happen to be iterating on the dictionary or similar and know that
the keys will be there.  
```python
In [25]: if 'host5' in status_by_host:
    ...:     print status_by_host['host5']
    ...: else:
    ...:     print 'host5 not in dictionary'
    ...:     
host5 not in dictionary
```
  
**Removing keys/values**  
This is done w/ the pop method.  It happens to return the value associated with the key, so this can be used
to process items in a dict until they are gone... see the "while True" example below. 
```python
In [26]: status_by_host
Out[26]: {'host1': 'up', 'host2': 'up', 'host3': 'down', 'host4': 'up'}

In [30]: status_by_host.pop('host1')
Out[30]: 'up'

In [31]: status_by_host
Out[31]: {'host2': 'up', 'host3': 'down', 'host4': 'up'}
```
  
**Iterating on dictionaries**  
When treated as an iterator, a dictionary will provide all of its keys:
```python
In [35]: for key in status_by_host:
    ...:     print "key:", key, 'and value:', status_by_host[key]
    ...:     
key: host4 and value: up
key: host3 and value: down
key: host2 and value: up
```
  
Key and value can be provided as well to avoid having to look up the value each iteration of the loop:  
```python
In [36]: for key, val in status_by_host.items():
    ...:     print "key:", key, 'and value:', val
    ...:     
key: host4 and value: up
key: host3 and value: down
key: host2 and value: up
```
  
"pop" until gone:  
```python
In [32]: while status_by_host:
    ...:     foo = status_by_host.popitem()
    ...:     # do stuff with foo...
    ...:     print 'one item:', foo
one item: ('host4', 'up')
one item: ('host3', 'down')
one item: ('host2', 'up')

In [33]: print status_by_host
{}

```

# Syntax and Namespace

## Loops
**"for" loops**  
"for" loops can iterate over any python object with a "__iter__" method.  The __iter__ method basically says to return
a value from the object each time it is referenced.  
```python
In [38]: for x in range(5):
    ...:     print x
    ...:     
0
1
2
3
4

In [39]: for x in ('a', 'b', 'c'):
    ...:     print "foobar:", x
    ...:     
foobar: a
foobar: b
foobar: c

In [40]: stuff = ( ('a', 0), ('b', 1), ('c', 99) )

In [41]: for letter, total in stuff:
    ...:     print "there are {} of {}".format(total, letter)
    ...:     
there are 0 of a
there are 1 of b
there are 99 of c
```
  
**"while" loops**  
"while" loops repeat as long as a condtion is satisfied.
```python
In [40]: while True:
    ...:     print "this will repeate forever..."
    ...:
this will repeate forever...
this will repeate forever...
...
```
See the **Iterating on Dictionaries** section above for more examples!

**break and continue**
break exists the loop when it is called and continue skipps to the next iteration of the loop.  Some languages
have a feature to lep you break out from multiple nested loops... this is not so in python, excep using tracking variables
or using the for-else convention given below.  
```python
In [42]: for x in range(5):
    ...:     if x%3 == 0:
    ...:         print "found first num divisible by three: {}".format(x)
    ...:         break
    ...:     
found first num divisible by three: 0

In [44]: for x in range(5):
    ...:     if x%2:
    ...:         continue
    ...:     print "found num divisible by two: {}".format(x)
    ...:     
found num divisible by two: 0
found num divisible by two: 2
found num divisible by two: 4
```

**for-else**
If "break" is not called in any iteration of the loop, then "else" gets executed. This can be a little mind-warping,
but is good for some fun interactions between nested loops, and is useful when we want to make sure something happens
if, e.g., we don't encounter some condition during execution of our loop. 

```python
In [45]: cities = ['atlanta', 'palo cedro', 'podunk']

In [47]: def theFugativeIsIn(fugative, city):
    ...:     if (fugative == 'vince' and city == 'atlanta'):
    ...:         return True
    ...:     elif (fugative == 'mary' and city == "tallahassee"):
    ...:         return True
    ...:     else:
    ...:         return False
    ...:     

In [48]: fugative = 'vince'

In [49]: for city in cities:
    ...:     if theFugativeIsIn(fugative, city):
    ...:         print "Found the fugative in {}".format(city)
    ...:         break
    ...:     else:
    ...:         print "Fugative not found in {}".format(city)
    ...: else:
    ...:     print "Fugative not found in any cities!"
    ...:     print "Better try some different cities..."
    ...:     
Found the fugative in atlanta

In [50]: fugative = 'mary'

In [51]: for city in cities:
    ...:     if theFugativeIsIn(fugative, city):
    ...:         print "Found the fugative in {}".format(city)
    ...:         break
    ...:     else:
    ...:         print "Fugative not found in {}".format(city)
    ...: else:
    ...:     print "Fugative not found in any cities!"
    ...:     print "Better try some different cities..."
    ...:     
Fugative not found in atlanta
Fugative not found in palo cedro
Fugative not found in podunk
Fugative not found in any cities!
Better try some different cities...
```
  
**iteritems!**  

  
## List Comprehensions

## Branching

## Functions

## Modules

## Classes

## Generators
