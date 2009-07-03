#!/usr/bin/env python
'''Replaces repeated values with carry preprocessor.'''

import sys
sys.path.append('../')  # Fix this.
import score
from optparse import OptionParser

def carry_replace(s):
    output = []
    values = []
    last_id = None
    
    for row in s:
        if score.get_pfield(row, 0) is 'i'\
                and score.get_pfield(row, 1) == last_id:
            for i in range(3, len(values)):
                v = values[i]
                
                if v == score.get_pfield(row, i):
                    glyph = '.'
                    row = score.set_pfield(row, i, glyph)
                else:
                    glyph = score.get_pfield(row, i)
                    values[i] = score.get_pfield(row, i)
                    row = score.set_pfield(row, i, glyph)
            output.append(row)
            
        elif score.get_pfield(row, 0) == None:
            output.append(row)

        else:
            values = []
            last_id = ''
            values = score.get_pfield_list(row)
            last_id = score.get_pfield(row, 1)
            output.append(row)
        
    return ''.join(output)

if __name__ == '__main__':
    # Get command-line flags
#    u = ['usage: <stdout> |']
#    u.append('python arpeggiator.py -i(statement) -n(identifier)')
#    u.append('-p(pfield) -v(number)')
#    usage = ' '.join(u)
#    parser = OptionParser(usage)
#    parser.add_option("-s", dest="statement", help="statement")
#    parser.add_option("-i", dest="identifier", help="identifier")
#    parser.add_option("-p", dest="pfield", help="pfield")
#    parser.add_option("-v", dest="value", help="value")
#    (options, args) = parser.parse_args()

    # Get input
    stdin = sys.stdin.readlines()
    s = ''.join(stdin).splitlines(True)

    print carry_replace(s),

