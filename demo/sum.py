#!/usr/bin/env python
'''Sums each pfield in an column with a user-specified value.

This script can be used as command-line script as well as a
module.

.. program:: sum
.. cmdoption:: -s  Statement (required)
.. cmdoption:: -i  Identifier (required)
.. cmdoption:: -p  Pfield (required)
.. cmdoption:: -v  Value (required)

Example::
    
    $ cat carry.sco | ./sum.py -si -i2 -p4 -v0.999

Before::
    
    i 2 0 0.25 0.3 7.00
    i 2 + 0.25 0.3 7.00
    i 2 + 0.25 0.3 7.00
    /**/
    i 2 + 0.25 0.5 7.00
    i 2 + 0.25 0.3 7.00
    i 2 + 0.25 0.5 7.00
    i 1 0 0.25 0.5 7.00
    i 1 1 0.25 0.5 7.00
    i 1 1 0.25 0.5 7.00
    i 1 1 0.25 0.5 7.00

After::

    i 2 0 0.25 1.299 7.00
    i 2 + 0.25 1.299 7.00
    i 2 + 0.25 1.299 7.00
    /**/
    i 2 + 0.25 1.499 7.00
    i 2 + 0.25 1.299 7.00
    i 2 + 0.25 1.499 7.00
    i 1 0 0.25 0.5 7.00
    i 1 1 0.25 0.5 7.00
    i 1 1 0.25 0.5 7.00
    i 1 1 0.25 0.5 7.00
'''

import sys
sys.path.append('../')  # Fix this.
import csd.sco.event as event
from optparse import OptionParser

def sum_(s, statement, identifier, pfield, v):
    '''Sums each pfield in a column with a user-specified value.'''
    
    output = []
    
    for row in s:
        if event.get(row, 0) is statement\
                and event.get(row, 1) == identifier:
            
            # Sum values, or ignore if original pfield is not NUMERIC
            pf = event.get(row, int(options.pfield))
            if event.token_type(pf) is event.NUMERIC:
                pf = float(pf) + float(v)

            output.append(event.set(row, int(options.pfield), pf))
        else:
            output.append(row)

    return ''.join(output)

if __name__ == '__main__':
    # Get command-line flags
    u = ['usage: <stdout> |']
    u.append('python arpeggiator.py -s(statement) -i(identifier)')
    u.append('-p(pfield) -v(number)')
    usage = ' '.join(u)
    parser = OptionParser(usage)
    parser.add_option("-s", dest="statement", help="statement")
    parser.add_option("-i", dest="identifier", help="identifier")
    parser.add_option("-p", dest="pfield", help="pfield")
    parser.add_option("-v", dest="value", help="value")
    (options, args) = parser.parse_args()

    # Get input
    stdin = sys.stdin.readlines()
    sco = ''.join(stdin).splitlines(True)

    print sum_(sco, options.statement, options.identifier,\
                      options.pfield, options.value), 

