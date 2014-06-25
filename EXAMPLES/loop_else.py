#!/usr/bin/env python

print "\nThree tries to enter an 'a'.\n"

for c in range(3):
    input = raw_input("Try number {0}: ".format(c))
    if input == 'a':
        print "\nThat was correct!\n"
        break
    else:
        print "That was not correct..."
else:
    print "\nYou failed to enter an 'a'. \n"
