#!/usr/bin/env python
'''Arpeggiates values in for a selected pfield column for a specific
event.

This script can be used as command-line script as well as a
module.

.. program:: arpeggiator
.. cmdoption:: -s  Statement (required)
.. cmdoption:: -i  Identifier (required)
.. cmdoption:: -p  Pfield (required)
.. cmdoption:: -v  Values (required)

Example::

    $ cat arpeggiator.sco | ./arpeggiator.py -si -i1 -p5 -v'7.00 7.03 6.09'
    
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
    def __init__(self, list_of_values):
        self.list_of_values = list_of_values
        self.arp_index = 0
        
    def next(self, x):
        output = self.list_of_values[self.arp_index]
        self.arp_index = (self.arp_index + 1) % len(self.list_of_values)
        print output
        return output


if __name__ == '__main__':
    # Get command-line flags
    u = ['usage: <stdout> |']
    u.append('python arpeggiator.py -s(statement) -i(identifier)')
    u.append('-p(pfield) -v("value1 value2 etc..")')
    usage = ' '.join(u)
    parser = OptionParser(usage)
    parser.add_option("-s", dest="statement", help="statement")
    parser.add_option("-i", dest="identifier", help="identifier")
    parser.add_option("-p", dest="pfield", help="pfield")
    parser.add_option("-v", dest="values", help="values")
    (o, args) = parser.parse_args()

    # Get input
    stdin = sys.stdin.readlines()
    score = ''.join(stdin)

    selected = sco.select(score, {0: o.statement, 1: o.identifier})
    arp = Arpeggiator([7, 8, 9])
    selected = selection.operate_numeric(selected, o.pfield, arp.next)
    print sco.merge(score, selected)

    
    
    
    
    
    
    
