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

def arpeggiator(score, pattern, pfield_index_list, value_list):
    selected = sco.select(score, pattern)
    arp = Arpeggiator(value_list)
    selected = selection.replace(selected, pfield_index_list, arp.next)
    return ''.join(sco.merge(score, selected))

def main():
    # Get argv from command-line
    value_list = sys.argv[1].split()
    statement = list(sys.argv[2])
    identifier = eval(sys.argv[3])
    pfield_index_list = eval(sys.argv[4])

    # Get input
    stdin = sys.stdin.readlines()
    score = ''.join(stdin)

    # Arpeggiate
    print arpeggiator(score, {0: statement, 1: identifier}, pfield_index_list,
                      value_list),
    
if __name__ == '__main__':
    main()

