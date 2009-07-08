#!/usr/bin/env python
'''Replaces subsequent repeated values with a carry (.)

This script can be used as command-line script as well as a
module.

Example::
    
    $ cat carry.sco | ./carry.py | ./align.py

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
    
    i 2 0 0.25 0.3 7.00
    i 2 + .    .   .
    i 2 + .    .   .
    /**/
    i 2 + .    0.5 .
    i 2 + .    0.3 .
    i 2 + .    0.5 .
    i 1 0 0.25 0.5 7.00
    i 1 1 .    .   .
    i 1 1 .    .   .
    i 1 1 .    .   .
'''

import sys
sys.path.append('../')  # Fix this.
import csd.sco.event as event

def replace(s):
    '''Replaces subsequent repeated values with a carry (.)'''
    
    output = []
    values = []
    last_id = None
    
    for row in s:
        if event.get(row, 0) is 'i'\
                and event.get(row, 1) == last_id:
            for i in range(3, len(values)):
                v = values[i]
                
                if v == event.get(row, i):
                    glyph = '.'
                    row = event.set(row, i, glyph)
                else:
                    glyph = event.get(row, i)
                    values[i] = event.get(row, i)
                    row = event.set(row, i, glyph)
            output.append(row)
            
        elif event.get(row, 0) == None:
            output.append(row)

        else:
            values = []
            last_id = ''
            values = event.get_pfield_list(row)
            last_id = event.get(row, 1)
            output.append(row)
        
    return ''.join(output)

if __name__ == '__main__':

    # Get input
    stdin = sys.stdin.readlines()
    s = ''.join(stdin).splitlines(True)

    print replace(s),

