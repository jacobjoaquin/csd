#!/usr/bin/env python
'''Exchanges all score columns for a specified statement and
identifier.

.. program:: swap_columns
.. cmdoption:: -s  Statement (required)
.. cmdoption:: -i  Identifier (required)
.. cmdoption:: -a  Pfield A (required)
.. cmdoption:: -b  Pfield B (required)

The following command-line swaps pfields 4 and 5 for all instrument
1 events::

    $ cat swap_columns.sco | ./swap_columns.py -si -i1 -a4 -b5

Before::
   
    i 1 0 1 7.00 0.8
    i 1 + . 7.02 0.8
    i 1 + . 7.04 1.0
    i 1 + . 7.05 0.8

After::
   
    i 1 0 1 0.8 7.00
    i 1 + . 0.8 7.02
    i 1 + . 1.0 7.04
    i 1 + . 0.8 7.05

'''

import sys
from optparse import OptionParser

sys.path.append('../')  # Fix this.
from csd import sco
from csd.sco import selection

if __name__ == '__main__':
    # Get command-line flags
    u = ['usage: <stdout> |']
    u.append('python swap_columns.py -s(statement) -i(instr) -a(int) -b(int)')
    usage = ' '.join(u)
    parser = OptionParser(usage)
    parser.add_option("-s", dest="statement", help="statement")
    parser.add_option("-i", dest="instr", help="instr")
    parser.add_option("-a", dest="pfield_a", help="pfield a")
    parser.add_option("-b", dest="pfield_b", help="pfield b")
    (o, args) = parser.parse_args()

    # Get stdin
    stdin = sys.stdin.readlines()
    s = ''.join(stdin)

    if o.pfield_a is None or o.pfield_b is None\
            or o.statement is None or o.instr is None:
        # Pass through input if all flags aren't specified.
        print s

        error = []
        error.append('WARNING!!  No modifications were made\n  ')
        error.append(usage)
        error.append('\n')
        print >> sys.stderr, ''.join(error)
    else:
        selected = sco.select(s, {0: o.statement, 1: o.instr})
        selected = selection.swap(selected, o.pfield_a, o.pfield_b)
        output = sco.merge(s, selected)
        
        print output,

