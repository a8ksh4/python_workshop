#!/usr/bin/env python

print "** About Spam **"
with open("../DATA/spam.txt") as sp:
    for line in sp:
        print line[:-1]  # or print line.rstrip()

with open("../DATA/eggs.txt") as eg:
    eggs = eg.readlines()
    
print "\n\n** About Eggs **"
print eggs[0][:-1]
print eggs[2][:-1]
