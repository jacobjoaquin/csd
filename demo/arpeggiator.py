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
#    usage = 'usage: <stdout> | python swap_columns.py -i(statement) -n(instr) -a(int) -b(int)'
#    parser = OptionParser(usage)
#    parser.add_option("-s", dest="statement", help="statement")
#    parser.add_option("-i", dest="instr", help="instr")
#    parser.add_option("-a", dest="pfield_a", help="pfield a")
#    parser.add_option("-b", dest="pfield_b", help="pfield b")
#    (options, args) = parser.parse_args()

    # Get stdin
#    stdin = sys.stdin.readlines()
#    s = ''.join(stdin)

    statement = 'i'
    identifier = '2'
    pf = 5
    
    sco = '''
i 1 0 1    1.0 440
i 2 0 0.25 1.0 7.00
i 2 + .    1.0 7.00
i 2 + .    1.0 7.00
i 2 + .    1.0 7.00
i 2 + .    1.0 7.00
i 2 + .    1.0 7.00
i 2 + .    1.0 7.00
i 3 4 14   0.3 1000
'''
    
    arp_input = "7.00 7.03 7.07 7.11"
    arp = []
    arp = arp_input.split()

    s = sco.splitlines(True)
    
    output = []
    
    i = 0  # Cycle index of looping arp list
    
    for row in s:
        if score.get_pfield(row, 0) is statement\
                and score.get_pfield(row, 1) == str(identifier):
            output.append(score.set_pfield(row, pf, arp[i]))
            i = (i + 1) % len(arp)
        else:
            output.append(row)
    
    print ''.join(output)
    
