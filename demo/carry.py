#!/usr/bin/env python
#
# Copyright (C) 2009 Jacob Joaquin
#
# This file is part of csd.
# 
# csd is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# csd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with csd.  If not, see <http://www.gnu.org/licenses/>.

'''Replaces subsequent repeated values with a carry (.)

This script can be used as command-line script as well as a
module.

Example::
    
    $ cat carry.sco | ./carry.py | ./sco_align.py

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
    
    i 1 0 0.25 0.5 7.00
    i 1 + .    .   .
    i 1 + .    .   8.00
    i 1 + .    .   .
    i 1 + .    0.6 7.06
    i 1 + .    .   .
    i 1 + .    .   6.06
    i 1 + .    .   .
    i 1 + .    .   7.00
    i 1 + .    .   .

'''

import sys

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

