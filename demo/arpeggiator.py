#!/usr/bin/env python
'''Arpeggiates a supplied list of values for a specific i statement
and identifier'''

import sys
sys.path.append('../')  # Fix this.
import score
from optparse import OptionParser

def arpeggiator(sco, statement, identifier, pfield, v):
    output = []
    
    i = 0  # Cycle index of looping arp list
    
    for row in sco:
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
    u.append('python arpeggiator.py -i(statement) -n(identifier)')
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
    
