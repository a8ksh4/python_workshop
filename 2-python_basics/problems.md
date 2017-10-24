

# Variables and Data Types
## Basic Math
* addThem(int, int) -> int
  * 20
  * return the sum of the two given values
* remainder(int, int) -> int
  * 20
  * return the remainder of two vals... 
* divideThem(int, int) -> float
  * 20
  * return the floating point value of a divided by b
* divideThemInt(int, int) -> (int, int)
  * 21
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
* returnWithQuotes() -> string
  * 21
  * return a string containing both types of quote:  ", '
* strUpper(string) -> string
  * 21
  * return a given string converted to all upper case. 
* firstHalfLower(string) -> string
  * 22
  * convert first half of string to lower case.
* justEvenChars
  * 22
  * return only even numbered characters from a string.
* reverseOrder(string) -> string
  * 22
  * return the string with it's order reversed. 
* listToCSV(string) -> string
  * 22
  * return a list of words from a string containing comma separated values. 
* undToShortCSV(string) -> string
  * 23
  * conver _sv to 3 words of csv. 
* getIndexOf(word, my_string) -> int
  * 23
  * return the index of a given word in teh given string.



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
## Truthiness
## Branching
* getTruthiness(obj) -> string
  * 21
  * Given an object, return "tequilla" if the object evaluates True, or "margarita" if it evaluates false.
* twosTruthiness(bool, bool, bool, bool) -> string
  * 22
  * Given four boolean values, if any two of them are true, return "twos", if any three of them are true, return "threes", or otherwise return "foobar".
* carmenFound(dict) -> string
  * 23
  * given a dictionary of cities with corresponding boolean values indicating whether or not carmen is in teh city, return the name of the city if carmen is in the city.  Reuturn only the first city where carmen is found.  If carmen is in none of hte cities, return the string "false".
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
  
## List Comprehensions
* convertToAllCaps(list of words) -> list of words
  * 22
  * Use a list comprehension to convert the list of words to a list of all-caps words and return it. 
* getEvenNums(list of integers) -> list of integers
  * 23
  * Given a list of integers, use a list comprehension to return a new list contianing only the positive numbers from the first list. 
* onlyCoolStuff(dictionary of product coolness, integer) -> list of products
  * 24
  * Given a dictionary containing products and a numeric rating of their coolness, and an integer value, return a list of products that are as cool or more cool than the integer value given. 
* wordsHasBees(list of words) -> list of bool
  * 24
  * Given a list of words, use a list comprehension to return a list of boolean values indicating whether or not the corresponding words have the lower case character "b" in them. "b" is for boolean!
