#!/usr/bin/env python

import random

TOTAL_GUESSES = 6
WORD_FILE = 'wordlist'

with open(WORD_FILE) as wl:
    words = wl.read().split('\n')

mystery_word = random.choice(words)
guess_word = [ "_" for c in mystery_word ]

print mystery_word

wrong_guesses = 0
while wrong_guesses < TOTAL_GUESSES:
    print "Mystery word is: {0}".format('.'.join(guess_word))
    response = raw_input("Enter a guess leter: ")
    if len(response) > 1 or not response.isalpha():
        print "Please only enter one letter!"
        continue

    if response in mystery_word:
        for c in range(len(mystery_word)):
            if mystery_word[c] == response:
                guess_word[c] = mystery_word[c]
        print "Correct!\n"
    else:
        print "Wrong, try again...\n"
        wrong_guesses += 1
    if ''.join(guess_word) == mystery_word:
        print "you found the correct word!"
        break

else:
    print "FAIL.  The word was: {0}".format(mystery_word)

