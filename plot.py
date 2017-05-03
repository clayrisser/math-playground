#!/usr/bin/env python

import sys
from plots import exponential

def main():
    command = sys.argv[len(sys.argv) - 1]
    if (command == 'exponential'):
        exponential.plot()
    else:
        print('Invalid command')
        exit(1)

main()
