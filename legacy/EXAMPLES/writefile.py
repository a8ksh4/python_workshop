#!/usr/bin/env python

states = (
    'Virginia',
    'North Carolina',
    'Washington',
    'New York',
    'Florida',
    'Ohio',
)

with open("states.txt","w") as statefile:
    for state in states:
        statefile.write(state + "\n")
