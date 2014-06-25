#!/usr/bin/env python

#global x
x = 1

def set_x():
    #global x
    x = 5
    print "inside set_x, x is: {0}".format(x)

print "outside set_x, x is: {0}".format(x)
set_x()
print "outside set_x, x is: {0}".format(x)

