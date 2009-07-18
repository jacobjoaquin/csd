#!/usr/bin/env python
'''Sums each pfield in an column with a user-specified value.

This script can be used as command-line script as well as a
module.

.. program:: add
.. cmdoption:: -s  Statement (required)
.. cmdoption:: -i  Identifier (required)
.. cmdoption:: -p  Pfield (required)
.. cmdoption:: -v  Value (required)

Example::
    
    $ cat add.sco | ./add.py -si -i1 -p4 -v0.4

Before::
    
    i 1 0 0.25 0.5 7.00
    i 1 + 0.25 0.5 7.00
    i 1 + 0.25 0.5 8.00
    i 1 + 0.25 0.5 8.00
    i 1 + 0.25 0.6 7.06
    i 1 + 0.25 0.6 7.06
    i 1 + 0.25 0.6 6.06
    i 1 + 0.25 0.6 6.06
    i 1 + 0.25 0.6 7.00
    i 1 + 0.25 0.6 7.00

After::

    i 1 0 0.25 0.9 7.00
    i 1 + 0.25 0.9 7.00
    i 1 + 0.25 0.9 8.00
    i 1 + 0.25 0.9 8.00
    i 1 + 0.25 1.0 7.06
    i 1 + 0.25 1.0 7.06
    i 1 + 0.25 1.0 6.06
    i 1 + 0.25 1.0 6.06
    i 1 + 0.25 1.0 7.00
    i 1 + 0.25 1.0 7.00

'''

import sys

from optparse import OptionParser

sys.path.append('../')  # Fix this.
from csd.sco import event
from csd.sco import element
from csd import sco

def add(s, statement, identifier, pfield, v):
    '''Adds v with to every numeric value in a pfield column.'''
    
    def _add(pf, x): return pf + x
    selection = sco.select(s, {0: statement, 1: identifier})
    selection = sco.operate_numeric(selection, pfield, _add, v)
    return sco.merge(s, selection)

def __sum_the_old_fashion_way(s, statement, identifier, pfield, v):
    '''Sums each pfield in a column with a user-specified value.
    
    .. note:: This is left in for the purpose of comparing the
              operate_numeric version to the older way of doing it.
    
    '''
    
    output = []
    
    for e in s:
        if event.match(e, {0: statement, 1: identifier}):
            
            # Sum values, or ignore if original pfield is not NUMERIC
            pf = event.get(e, int(options.pfield))
            if element.token_type(pf) is element.NUMERIC:
                pf = float(pf) + float(v)

            output.append(event.set(e, int(options.pfield), pf))
        else:
            output.append(e)

    return ''.join(output)

def main():
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
    (o, args) = parser.parse_args()

    # Get input
    stdin = sys.stdin.readlines()
    s = ''.join(stdin)

    print add(s, o.statement, o.identifier, o.pfield, o.value), 

if __name__ == '__main__':
    main()

