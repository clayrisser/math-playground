#!/usr/bin/env python

import sys
from plots import exponential, sigmoid

def main():
    command = sys.argv[len(sys.argv) - 1]
    if (command == 'exponential'):
        exponential.plot()
    if (command == 'sigmoid'):
        sigmoid.plot()
    else:
        print('Invalid command')
        exit(1)

main()
