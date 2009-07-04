#!/usr/bin/env python
'''Swaps two pfields for all rows that match a specified statement
and identifier.

i.e. 'i 7' where the 'i' is a i-event statement and '7' is the
instrument number.

    example: $ cat swap.sco | ./swap_pfields.py -si -i7 -a4 -b5
    
The previous command-line will swap pfields 4 and 5 for all instrument
7 events.
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

