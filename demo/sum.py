#!/usr/bin/env python
'''Arpeggiates a supplied list of values for a specific i statement
and identifier'''

import sys
sys.path.append('../')  # Fix this.
import score
from optparse import OptionParser

def sum_(s, statement, identifier, pfield, v):
    output = []
    
    for row in s:
        if score.get_pfield(row, 0) is statement\
                and score.get_pfield(row, 1) == identifier:
            
            # Sum values, or ignore if original pfield is not NUMERIC
            pf = score.get_pfield(row, int(options.pfield))
            if score.token_type(pf) is score.NUMERIC:
                pf = float(pf) + float(v)

            output.append(score.set_pfield(row, int(options.pfield), pf))
        else:
            output.append(row)

    return ''.join(output)

if __name__ == '__main__':
    # Get command-line flags
    u = ['usage: <stdout> |']
    u.append('python arpeggiator.py -i(statement) -n(identifier)')
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

