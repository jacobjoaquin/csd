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

    $ cat arp.sco | ./arpeggiator.py -si -i2 -p5 -v"7.00 7.03 7.07 7.10"
    
Before::
    
    i 1 0 4    1.0 9.07
    i 2 0 0.25 0.3 7.00
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 1 0 4    1.0 9.11

After::
    
    i 1 0 4    1.0 9.07
    i 2 0 0.25 0.3 7.00
    i 2 + .    .   7.03
    i 2 + .    .   7.07
    i 2 + .    .   7.10
    i 2 + .    .   7.00
    i 2 + .    .   7.03
    i 2 + .    .   7.07
    i 2 + .    .   7.10
    i 2 + .    .   7.00
    i 2 + .    .   7.03
    i 1 0 4    1.0 9.11
'''

import sys
sys.path.append('../')  # Fix this.
import score
from optparse import OptionParser

def arpeggiator(s, statement, identifier, pfield, v):
    '''Arpeggiates values in for a selected pfield column for a specific
event.'''
    
    output = []
    
    i = 0  # Cycle index of looping arp list

    for row in s:
        if score.get_pfield(row, 0) is statement\
                and score.get_pfield(row, 1) == identifier:
            output.append(score.set_pfield(row, int(options.pfield), v[i]))
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
    (options, args) = parser.parse_args()

    # Get input
    stdin = sys.stdin.readlines()
    sco = ''.join(stdin).splitlines(True)

    # Convert vales into list
    arp = options.values.split()

    print arpeggiator(sco, options.statement, options.identifier,\
                      options.pfield, arp), 

