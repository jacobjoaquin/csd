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

    $ cat swap.sco | ./swap_columns.py -si -i1 -a4 -b5

Before::
   
    i 1 0 4 6.04 15000 2 100 81 50 56 20 1
    i 1 + . .    .     . 101 .  .  .  .  .
    i 1 + . 6.02 5000  2 100 81 50 56 20 1
    i 1 + . .    .     . 101 .  .  .  .  .
    i 1 + . 6.01 8000  2 100 81 50 56 20 1
    i 1 + . .    .     . 101 .  .  .  .  .
    i 1 + . 6.09 11000 2 100 81 50 56 20 1
    i 1 + . .    .     . 101 .  .  .  .  .
    
    i 7 16.4 3.5 8000 5.019 0.2 0.7 0.5 2 3 0.1
    i 7 19.3 6.4 8000 5.041 .   0.9 1   3 2 0.1
    i 7 16.4 3.5 8000 5.019 0.2 0.7 0.5 2 3 0.1
    i 7 19.3 6.4 8000 5.041 .   0.9 1   3 2 0.1

After::
   
    i 1 0 4 15000 6.04 2 100 81 50 56 20 1
    i 1 + . .    .     . 101 .  .  .  .  .
    i 1 + . 5000 6.02  2 100 81 50 56 20 1
    i 1 + . .    .     . 101 .  .  .  .  .
    i 1 + . 8000 6.01  2 100 81 50 56 20 1
    i 1 + . .    .     . 101 .  .  .  .  .
    i 1 + . 11000 6.09 2 100 81 50 56 20 1
    i 1 + . .    .     . 101 .  .  .  .  .
    
    i 7 16.4 3.5 8000 5.019 0.2 0.7 0.5 2 3 0.1
    i 7 19.3 6.4 8000 5.041 .   0.9 1   3 2 0.1
    i 7 16.4 3.5 8000 5.019 0.2 0.7 0.5 2 3 0.1
    i 7 19.3 6.4 8000 5.041 .   0.9 1   3 2 0.1
'''

import sys
sys.path.append('../')  # Fix this.
import score
from optparse import OptionParser

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
    (options, args) = parser.parse_args()

    # Get stdin
    stdin = sys.stdin.readlines()
    s = ''.join(stdin)

    if options.pfield_a is None or options.pfield_b is None\
            or options.statement is None or options.instr is None:
        # Pass through input if all flags aren't specified.
        print s

        error = []
        error.append('WARNING!!  No modifications were made\n  ')
        error.append(usage)
        error.append('\n')
        print >> sys.stderr, ''.join(error)
    else:
        # Swap columns
        output = score.swap_columns(s, options.statement, options.instr,
                 int(options.pfield_a), int(options.pfield_b))
        print output

