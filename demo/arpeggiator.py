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
import csd.sco.event as event

def arpeggiator(s, statement, identifier, pfield, v):
    '''Arpeggiates values in for a selected pfield column for a specific
    event.
    
    '''
    
    output = []
    
    i = 0  # Cycle index of looping arp list

    for row in s:
        if event.match(row, {0: statement, 1: identifier}):
            output.append(event.set(row, int(o.pfield), v[i]))
            i = (i + 1) % len(arp)
        else:
            output.append(row)

    return ''.join(output)

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
    sco = ''.join(stdin).splitlines(True)

    # Convert values into list
    arp = o.values.split()

    print arpeggiator(sco, o.statement, o.identifier, o.pfield, arp), 

