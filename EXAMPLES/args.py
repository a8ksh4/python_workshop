#!/usr/bin/env python

import argparse
import sys

if '--debug' in sys.argv:
    print('We can check for specific args outside of argparse.\n')
    DEBUG=True

def getArgs():
    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description="Test Program for Argparse\nThese sorts of things can be\nvery exciting.",
        epilog="And now, you know the rest of the story!")
    parser.add_argument('--verbose', '-v', help="verbose mode", action='count')
    parser.add_argument('--debug', help="debug mode", action='store_true')
    parser.add_argument('--widgets', type=int, help="number of widgets", action='store')

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = getArgs()
    print("ARGS ARE:")
    print(args)
