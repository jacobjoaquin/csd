#!/usr/bin/env python
'''Arpeggiates values in for a selected pfield column for a specific
event.

This script can be used as command-line script as well as a
module.

Example::

    $ cat arpeggiator.sco | ./arpeggiator.py '7.00 7.03 6.09' i 1 5
    
Before::
    
    i 1 0 0.25 0.3 7.00
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .

After::
    
    i 1 0 0.25 0.3 7.00
    i 1 + .    .   7.03
    i 1 + .    .   6.09
    i 1 + .    .   7.00
    i 1 + .    .   7.03
    i 1 + .    .   6.09
    i 1 + .    .   7.00
    i 1 + .    .   7.03

'''

import sys
from optparse import OptionParser

sys.path.append('../')  # Fix this.
from csd import sco
from csd.sco import selection

class Arpeggiator:
    def __init__(self, value_list):
        self.value_list = value_list
        self.arp_index = 0
        
    def next(self):
        output = self.value_list[self.arp_index]
        self.arp_index = (self.arp_index + 1) % len(self.value_list)
        return output

if __name__ == '__main__':
    # Get argv from command-line
    values = sys.argv[1]
    statement = list(sys.argv[2])
    identifier = eval(sys.argv[3])
    pfield = eval(sys.argv[4])

    # Get input
    stdin = sys.stdin.readlines()
    score = ''.join(stdin)

    selected = sco.select(score, {0: statement, 1: identifier})
    arp = Arpeggiator(values.split())
    selected = selection.replace(selected, pfield, arp.next)
    print sco.merge(score, selected),
    
