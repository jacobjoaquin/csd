#!/usr/bin/env python
'''Pulls a score from a csd.'''

import sys
sys.path.append('../')  # Fix this.
import score

if __name__ == '__main__':

    # Get input
    stdin = sys.stdin.readlines()
    s = ''.join(stdin)

    print score.extract(s),

