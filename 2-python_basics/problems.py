#!/usr/bin/env python

global os
import os
global random
import random
global re
import re
global shutil
import shutil
global string
import string
global sys
import sys

def _randStr(str_len=10):
    return ''.join(random.choices(string.ascii_uppercase, k=str_len))

def _stdRdr(func, args, path):
    orig = sys.stdout
    with open(path, 'w') as sys.stdout:
        func(*args)
    sys.stdout = orig

def addThem(a, b):
    '''basic_math_1
    Write a function called addThem that accepts two numbers and returns
    their sum.
    >>> 2 == addThem(1, 1)
    True
    >>> 1 == addThem(-5.1, 6.1)
    True
    '''
    the_sum = a + b
    return the_sum


def remainder(a, b):
    '''basic_math_2
    Write a function called remainder that accepts two numbers, a and b,
    and returns the remainder of a / b. 
    >>> 4 == remainder(9, 5)
    True
    '''
    the_remainder = a % b
    return the_remainder


def toInt(a_float):
    '''basic_math_3
    Write a function called toInt that accepts an interger or floating point
    number and returns it as an integer.  E.g. 3.3 becomes 3.
    >>> 3 == toInt(3.9)
    True
    '''
    an_integer = int(a_float)
    return an_integer


def divideThemInt(a, b):
    '''basic_math_4
    Write a function called divideThemIOnt that performs integer division
    on two given integers, a divided by b, and return the output as an integer.
    >>> 2 == divideThemInt(4.4, 2)
    True
    >>> 2 == divideThemInt(5, 2)
    True
    '''
    integer_result = int(a//b)
    return integer_result


def convertCToF(temp_in_c):
    '''basic_math_5
    Write a function called convertCToF that accepts a temperature in
    centigrade and returns the equivelant temperature in Farenheight.

    The equation for this is: (f = c/5 + 32/9)
    >>> 20/5.0 + 32.0/9.0 == convertCToF(20)
    True
    >>> -10/5.0 + 32.0/9.0 == convertCToF(-10)
    True
    '''
    temp_in_f = temp_in_c/5.0 + 32.0/9.0
    return temp_in_f


def getTruthiness(obj):
    '''branching_1
    Write a function called getTruthiness that is given an object and, if
    that object evaluates to True, returns the string "tequilla", or otherwise
    returns the string "margarita".
    >>> "margarita" == getTruthiness([])
    True
    >>> "tequilla" == getTruthiness((1,))
    True
    >>> "margarita" == getTruthiness(0)
    True
    '''
    if obj:
        resulting_word = "tequilla"
    else:
        resulting_word = "margarita"
    return resulting_word


def twosTruthiness(obj0, obj1, obj2, obj3):
    '''branching_2
    Write a function called twosTruthiness that is given four boolean values.
    if any two of the four are True, then return "twos".  If any three of them
    are True, then return "threes", if less than two or four of them are True,
    then return "foobar"
    >>> twosTruthiness([], [], [], [])
    'foobar'
    >>> twosTruthiness([], [], [1,], [])
    'foobar'
    >>> twosTruthiness([], [], [1,], [1,])
    'twos'
    >>> twosTruthiness([1,], [], [1,], [1,])
    'threes'
    >>> twosTruthiness([1,], [1,], [1,], [1,])
    'foobar'
    '''
    items = (obj0, obj1, obj2, obj3)
    count = len([o for o in items if o])
    if count == 2:
        resulting_word = "twos"
    elif count == 3:
        resulting_word = "threes"
    else:
        resulting_word = "foobar"
    return resulting_word


def carmenFound(cities):
    '''branching_3
    Create a function called carmenFound that is given a dictionary with a
    list of city names as keys, each associated with a boolean value
    indicating whether or not Carmen is in the city.  Return the name of the
    city Carmen is found in!

    The cities dictionary will look like: {'city_a': False, 'city_b'...}

    >>> 'atlanta' == carmenFound({'atlanta': True, 'memphis': False})
    True
    >>> 'memphis' == carmenFound({'atlanta': False, 'memphis': True})
    True
    '''
    for city in cities:
        if cities[city] == True:
            return city


def pocketContent(inventory):
    '''dictionaries_1
    Write a function called pocketContents that accepts an inventory
    dictiionary and adds a "pocket" to the inventory that contains a 
    ['seashell',].

    For example the inventory might look like this:
    {'gold': 400, 'pouch': ['flint', 'twine', 'gemston']}

    And the returned inventory would look like:
    {'gold': 400, 'pouch': ['flint', 'twine'], 'pocket': ['seashell']}
    >>> i = {'gold': 90, 'po': ['fl', 'te', 'gon']}
    >>> r = {'gold': 90, 'po': ['fl', 'te', 'gon'], 'pocket': ['seashell']}
    >>> r == pocketContent(i)
    True
    '''
    inventory['pocket'] = ['seashell']
    return inventory


def myPricesDict():
    '''dictoinaries_2
    Write a function called myPricesDict that puts the following items and
    prices into a dictionary and returns it:
        "bananna": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    >>> answer = {'bananna': 4, 'apple': 2, 'orange': 1.5, 'pear': 3}
    >>> answer == myPricesDict()
    True
    '''
    prices_dict = {'bananna': 4, 'apple': 2, 'orange': 1.5, 'pear': 3}
    return prices_dict


def mergeToDict(keys, values):
    '''dictoinaries_3
    Write a function called mergeToDict that accepts a list of keys and a
    corresponding list ov values and returns a dictionary that has each
    key and value associated.

    For example, if the keys were ('color', 'flavor', 'texture') and the values
    were ('red', 'sour', and 'rough'), the dictionary would look like:
    {'color': 'red', 'flavor': 'sour', 'texture': 'rough'}
    >>> keys = [1, 2, 3, 4]
    >>> vals = [5, 6, 7, 8]
    >>> {1: 5, 2: 6, 3: 7, 4: 8} == mergeToDict(keys, vals)
    True
    '''
    merged_dict = dict(zip(keys, values))
    return merged_dict


def getDictKeys(a_dictionary):
    '''dictionaries_4
    Write a function called getDictKeys that is given a dictionary and returns
    the keys in the dictionary as a list. 
    >>> [1, 2, 3, 4] == getDictKeys({1: 5, 2: 6, 3: 7, 4: 8})
    True
    '''
    keys = list(a_dictionary.keys())
    return keys


def checkKeyExists(a_dictionary, the_key):
    '''dictionaries_5
    Write a function called checkKeyExists that is given a dictionary and a
    key and returns True if the key exists in the dictionary or False if it
    does not.
    >>> checkKeyExists({'a': 0, 'b': 1}, 'a')
    True
    >>> not checkKeyExists({'a': 0, 'b': 1}, 'z')
    True
    >>> not checkKeyExists({'a': 0, 'b': 1}, 1)
    True
    >>> not checkKeyExists({'a': 0, 'b': 1}, 0)
    True
    '''
    exists_bool = the_key in a_dictionary
    return exists_bool


def checkKeysExist(a_dictionary, some_keys):
    '''dictionaries_6
    Write a function called checkKeysExist that is given a dictionary and a
    list of keys to look for in teh dictionary.  The function returns a new
    dictionary containing each key in the provided list with an associated
    boolean value indicating whether or not the key from the list was found
    in the given dictionary.    

    As an example, if given {'a': 0, 'b': 1} and ['a', 'c'] for keys, the
    output would be {'a': True, 'c': False}.
    >>> ans = {'z': True, 'c': False}
    >>> ans.items() == checkKeysExist((('z',0), ('b', 1)), ('z', 'c')).items()
    True
    >>> (len(checkKeysExist({'z': 0, 'b': 1}, ['f',]).keys()) == 1)
    True
    '''
    if isinstance(a_dictionary, tuple):
        a_dictionary = dict(a_dictionary)
    out = {}
    for key in some_keys:
        out[key] = key in a_dictionary
    return out


def printGivenKeys(a_dictionary, some_keys):
    '''dictionaries_7
    Write a function called printGivenKeys that is given a dictionary and a
    list of keys to look for in teh dictionary.  For each item in the list,
    the function prints the item and the value associated with it in the
    provided dictionary.  If the item is not in the dictionary, None is used
    for the value. The sequence of the list should be preserve when printing.

    As an example, if given {'a': 0, 'b': 1} and ['c', 'a'] for keys, it would 
    print:
    c, None
    a, 0
    >>> p0 = './{}'.format(_randStr())
    >>> _stdRdr(printGivenKeys, ({'a': 0, 'b': 1}, ()), p0)
    >>> '' == open(p0, 'r').read()
    True
    >>> _stdRdr(printGivenKeys, ({'a': 0, 'b': 1}, ('z', 'y','a')), p0)
    >>> 'z, None\\ny, None\\na, 0\\n' == open(p0, 'r').read()
    True
    >>> os.remove(p0)
    '''
    for key in some_keys:
        if key in a_dictionary:
            print("{}, {}".format(key, a_dictionary[key]))
        else:
            print("{}, {}".format(key, None))
    #return nothing


def sumAllItems(some_nums):
    '''lists_1
    Write a function called sumAllItems that accepts a list or tuple of
    numbers, summs them, and returns the sum.  If the list is empty, return
    None, rather than zero. 
    >>> 0.0000001 > 10.1 - sumAllItems([2, 4, 20, 4.1, -20])
    True
    >>> 0 == sumAllItems((-1, 1))
    True
    >>> None == sumAllItems(())
    True
    >>> None == sumAllItems([])
    True
    '''
    if len(some_nums) == 0:
        the_sum = None
    else:
        the_sum = sum(some_nums)
    return the_sum


def smallestOfList(some_nums, absolute_val=False):
    '''lists_2
    Write a function called smallestOfList that accepts a list or tuple of
    numbers and returns the smallest number found in the list.
    
    However, if absolute value is set to True, it should return the number that
    has the smallest absolute value.

    If two numbers in the list both have an absolute value that is the
    smallest and the same, the first one encounterd should be returned.
    >>> -5 == smallestOfList((1, 2, 3, 4, -5))
    True
    >>> 1 == smallestOfList((1, 2, 3, 4, -5), True)
    True
    >>> 1 == smallestOfList((2, 1, -1, 3, 4, -5), True)
    True
    >>> 1 == smallestOfList((-2, 1, -1, 3, 4, -5), True)
    True
    '''
    smallest = None
    small_loc = None
    for n, num in enumerate(some_nums):
        num = abs(num) if absolute_val else num
        if smallest == None or num < smallest:
            smallest = num
            small_loc = n
    smallest = some_nums[small_loc]
    return smallest


def convTupleUnique(some_items):
    '''sets_1
    Write a function called convTupleUnique(list) that accepts a list of
    objects and returns a tuple (not a list) with only the unique items from
    the list.  Order of the returned list is not important.
    >>> items = (9, 1, 1, 9, 2, 3, 4, 4, 5)
    >>> res = convTupleUnique(items)
    >>> sorted(res) == sorted(set(items))
    True
    '''
    unique_tuple = tuple(set(some_items))
    return unique_tuple


def convTupleUniqueOrder(some_items):
    '''sets_2
    Write a function called convTupleUniqueOrder(list) that accepts a list of
    objects and returns a tuple (not a list) with only the unique items from
    the list. Order of the returned tuple IS important. Order from the
    original list should be preserved; the first time an object is observed
    in the given list, it is in the returned tuple, and subsequent occurences
    are ignored. 
    >>> items = (1, 1, 2, 3, 4, 4, 5) 
    >>> res = convTupleUniqueOrder(items)
    >>> (1, 2, 3, 4, 5) == res
    True
    '''
    out = []
    for item in some_items:
        if item in out:
            continue
        out.append(item)
    return tuple(out)


def createSet(obj1=None, obj2=None, obj3=None, obj4=None, obj5=None):
    '''sets_3
    Write a function called createSet that accepts up to five objects, adds
    them into a set, and returns a set of those objects. Hint: "set" is a
    data type.  Do not add any of the objects fo the set if the object is
    equal to the None object.
    >>> set((1, 2, 3)) == createSet(obj2=1, obj3=2, obj4=3, obj5=3)
    True
    >>> set((1, 2, 3)) == createSet(obj2=1, obj3=2, obj5=3)
    True
    >>> set() == createSet(None, None, None)
    True
    >>> set() == createSet()
    True
    '''
    new_set = set()
    for obj in (obj1, obj2, obj3, obj4, obj5):
        if obj != None:
            new_set.add(obj)
    return new_set


def removeFromSet(a_set, an_item):
    '''sets_4
    Write a function called removeFromSet that accepts a set and an item. 
    If the item exists in the set, then it is removed.  The resulting set
    is converted to a tuple and returned.
    >>> foo = (1, 2, 3, 4, 5, 6)
    >>> new = removeFromSet(set(foo), 6)
    >>> sorted((1, 2, 3, 4, 5)) == sorted(new)
    True
    >>> new = removeFromSet(set(foo), 7)
    >>> sorted(new) == sorted(foo)
    True
    '''
    if an_item in a_set:
        a_set.remove(an_item)
    return tuple(a_set)


def returnWithQuotes():
    '''strings_1
    Write a function called returnWithQuotes that takes no arguments and,
    when called, returns the following text (no whitespace on the ends),
    but with all quotes shown included in the string:

        'It's modulus, "%", not division, "/", or escaping "\"!'
    >>> foo = """'It's modulus, "%", not division, "/", or escaping "\"!'"""
    >>> out = returnWithQuotes()
    >>> foo == out
    True
    '''
    quotes = """'It's modulus, "%", not division, "/", or escaping "\"!'"""
    return quotes


def strUpper(a_string):
    '''strings_2
    Write a function called "strUpper" that takes a string as an argument
    and returns the string without any whitespace on the ends and all upper
    case.
    >>> foo = "   asfd"
    >>> foo.upper().strip() == strUpper(foo)
    True
    >>> foo = "123%asf d "
    >>> foo.upper().strip() == strUpper(foo)
    True
    >>> foo = "ASDF"
    >>> foo == strUpper(foo)
    True
    >>> foo = ""
    >>> foo == strUpper(foo)
    True
    >>> foo = "   \\n"
    >>> foo.strip() == strUpper(foo)
    True
    '''
    upper_stripped = a_string.upper().strip()
    return upper_stripped


def firstHalfLower(a_string):
    '''strings_3
    Write a function called "firstHalfLower" that takes a string as an
    argument and returns the first half of the string, all lower case. When
    calculating how many characters of the string to return, round down:
    An 11 character string would result in 5 characters being returned.
    >>> foo = "asdF12345"
    >>> out = firstHalfLower(foo)
    >>> foo[:len(foo)//2].lower() == out
    True
    >>> "" == firstHalfLower("A")
    True
    >>> foo = "aS1dF2"
    >>> out = firstHalfLower(foo)
    >>> foo[:len(foo)//2].lower() == out
    True
    '''
    length = int(len(a_string) / 2)
    result = a_string[:length].lower()
    return result


def justEvenChars(a_string):
    '''strings_4
    Write a function called "justEvenChars" that takes a string as an
    argument and returns only even numbered characters from the string. If
    the string is "coolio", the result would be "coi", treating the zeroth
    characte as even (0%2==0).
    
    >>> 'zBD ' == justEvenChars('zABCDS ')
    True
    >>> '13579' == justEvenChars('123456789')
    True
    >>> ' o!Ti sco ' == justEvenChars(' ro3! T2is is cool ')
    True
    '''
    even_num_chars = a_string[::2]
    return even_num_chars


def reverseOrder(a_string):
    '''strings_5
    Write a function called "reverseOrder" that takes a string as an
    argument and returns another string with all of the whitespace
    delimetered words in the reverse order, not taking any special
    consideration for number/symbols.  KISS.  If the string, " one1 tw_o
    thREE four!" is passed in, "four! thREE tw_0 one1" would be returned. 
    Strip any whitespace from the ends of the given string.
    >>> out = reverseOrder('ro3! T2is is cool')
    >>> 'cool is T2is ro3!' == out
    True
    >>> out = reverseOrder(' ABCDS')
    >>> 'ABCDS' == out
    True
    >>> out = reverseOrder('123456789 asdf ASDF 4 _ 123 nine? \"\"')
    >>> '\"\" nine? 123 _ 4 ASDF asdf 123456789' == out
    True
    '''
    switched = a_string.strip()
    switched = switched.split()
    switched = switched[::-1]
    switched = " ".join(switched)
    return switched


def listToCSV(words_list):
    '''strings_6
    Write a function called "listToCSV" that takes a list of strings and
    combines them into a single string with all words separated by a
    comma: ",".  For example, ["one", 'two', 'three'] becomes "one,two,three".
    >>> out = listToCSV(['one', ' ', 'two', '', 'three', ''])
    >>> out == "one, ,two,,three,"
    True
    >>> out = listToCSV(['1', ',', ':', 'fiftyfive'])
    >>> out == '1,,,:,fiftyfive'
    True
    '''
    csv_string = ','.join(words_list)
    return csv_string


def undToShortCSV(und_sep_words):
    '''strings_7
    Write a function called "undToShortCSV" that takes a string with words,
    each separated by an underscore, '_', changes the underscores to
    commas, ",", and returns only the first three words.  You can assume
    that there will always be more than three words separated by underscore
    given.
    >>> out = undToShortCSV('one_two_three_four_five')
    >>> out == 'one,two,three'
    True
    >>> out = undToShortCSV('one_two_ ')
    >>> out == 'one,two, '
    True
    >>> out = undToShortCSV(' _ __ _ ')
    >>> out == ' , ,'
    True
    '''
    comma_sep = ','.join(und_sep_words.split('_')[:3])
    return comma_sep


def getIndexOf(word, search_string):
    '''strings_8
    Wirte a functuion called "getIndexOf" that returns the index of a given
    word inside of a given string.  If the word is not present, it returns
    a -1. 
    For exmaple, if the word is "pizza", and the search_string is:
        "there is pizza on the plate"
    then the index is 9.
    >>> 9 == getIndexOf('pizza', 'there is pizza on the plate')
    True
    >>> -1 == getIndexOf('PIZZA', 'there is pizza on the plate')
    True
    '''
    if word in search_string:
        return search_string.index(word)
    else:
        return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
