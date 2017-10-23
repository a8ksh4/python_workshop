

# Variables and Data Types
## Basic Math
* divideThem(int, int) -> float
  * 20
  * return the floating point value of a divided by b
* divideThemInt(int, int) -> (int, int)
  * 20
  * return the integer result of a divided by b AND the modulues result of a mod b.
```python 
def divideThemInt(a, b):
    #...
    div_result = 
    mod_result = 
    return (div_result, mod_result)
```
* convertCToF(int) -> int
  * 20
  * given a temperature in Centigrade, return the equiv. temperature in F.  (c/5 + 32/9 = f) 

## Strings
* quoteIt() -> string
  * 20
  * return a string with both single and doubel quotes inside of it.'
* getIndexOf(word, my_string) -> int
  * 20
  * return the index of a given word in teh given string.
* matchAnimals(some_string) -> bool
  * 20
```python
 def matchAnimals(my_string):
     animals = ('dog', 'cat', 'elephant', 'moose', 'duck')
     for animal in animals:
         if _put_something_here_:
             return True
     return False
```
*   0 (1, 'math_example_1', 'add(int, int) -> int')
*   1 (1, 'math_example_2', 'remainder(int, int) -> int')
*   2 (1, 'math_examples_3', 'toInt(float) -> int')
*   3 (4, 'quoting_example_1', 'returnWithQuotes() -> string')
*   4 (4, 'string_example_1', 'strUpper(string) -> string')
*   5 (4, 'string_example_2', 'firstHalfLower(string) -> string')
*   6 (4, 'string_example_3', 'justEvenChars(string) -> (string)')
*   7 (5, 'string_example_4', 'reverseOrder(string) -> string')
*   8 (5, 'string_example_5', 'listToCSV(list) -> string')
*   9 (5, 'string_example_6', 'undToShortCSV(string) -> string')

## Lists and Tuples
* sumAllItems(list of number) -> number
  * 21
  * sum all of the items in a list and return the value
* smallestOfList(list of number) -> number
  * 21
  * find and return the smallest number in teh given list. 


## Sets
* convTupleUnique(list) -> tuple
  * 21
  * given a list of objects, return a tuple with only unique items from the given list. 
* convTupleUniqueOrder(list) -> tuple
  * 22
  * given list of objects, return tuple with only unique items, preserving order of original list, so the first time an object appears, it will be found int he resulting tuple.  subsequent occurences of the objcet in the given list are ignored. 
* createSet(obj, obj, obj, obj, obj) -> set
  * 21
  * given several args, add each of them to a set and return the set. 
* removeFromSet(set, obj) -> set
  * 20
  * given a set and an object, remove the object from the set and retunr teh set. 
  
## Dictionaries
*  10 (6, 'dict_example_1', 'pocketContents() -> dict')
*  11 (6, 'dict_example_2', 'myPricesDict() -> dict')
*  12 (6, 'dict_example_3', 'mergeToDict(list, list) -> dict')
* listsToDict(keys, values) -> dict
  * 21
  * given a list of keys and another list of corresponding values, convert them into a dictionary and return it. 
* getDictKeys(dict) -> list
  * 21
  * given a dictoinary, return a list of it's keys (only), no values.
* checkKeyExists(dict, key) -> bool
  * 20
  * given a ditionary and a key, return true or false to indicate whether or not the key is in the dictionary.
* checkKeysExist(dict, list) -> dict
  * 23
  * given a list of keys and a dictionary, check if each key exists in the dictionary, return a dictionary consisting
    of the list of keys and boolean values indicating whether or not they exist.  
* printGivenKeys(dict, list)
  * 22
  * given a dictionary and a list of keys, for each key in teh list, print the key name and the value assocaited with it. 

# Syntax and Namespace
## Loops
https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
* loopStarPyramid()
  * 24
  * use nested for loops to produce the following pattern:
```
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
```
* getFibThrough(int) -> list
  * 24
  * return a list of fibonacci series up to the given number. 
* returnNoneArray(int, int) -> list of lists
  * 24
  * given two non-zero integers, return a list of lists of "None" with the dimmensions given.
* convStrToDict(list of string) -> dict
  * 25
  * given a list of string values like "Key : value", iterate over each string, split out the key and value, and add them
    into a dictionary.  Return the dictionary. 
* countDigitAndLetter(string) -> (int, int)
  * 25
  * given a string, count the number of numbers and the number of letters in the string and return them in a tuple. (num_numbers, num_letters). 
* lastNumForSum(list of int, int) -> int
  * 24
  * iterate over a list of integers and return the last number before the sume of all previous numbers is more than the second arg given int. 
* 
