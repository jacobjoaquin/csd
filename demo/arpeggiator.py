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

'''Arpeggiates values in for a selected pfield column for a specific
event.

Use::
    
    <stdout> | ./pfunc.py STATEMENT INSTR PFIELD VALUES

Example::

    cat arpeggiator.sco | ./arpeggiator.py i 1 5 '7.00 7.03 6.09'
    
Before::
    
    i 1 0 0.25 0.3 7.00
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .

After::
    
    i 1 0 0.25 0.3 7.00
    i 1 + .    .   7.03
    i 1 + .    .   6.09
    i 1 + .    .   7.00
    i 1 + .    .   7.03
    i 1 + .    .   6.09
    i 1 + .    .   7.00
    i 1 + .    .   7.03

'''

import sys

from csd import sco
from csd.sco import selection

class Arpeggiator:
    def __init__(self, value_list):
        self.value_list = value_list
        self.arp_index = 0
        
    def next(self):
        output = self.value_list[self.arp_index]
        self.arp_index = (self.arp_index + 1) % len(self.value_list)
        return output

def arpeggiator(score, pattern, pfield_index_list, value_list):
    selected = sco.select(score, pattern)
    arp = Arpeggiator(value_list)
    selected = selection.replace(selected, pfield_index_list, arp.next)
    return ''.join(sco.merge(score, selected))

def main():
    # Get argv from command-line
    statement = list(sys.argv[1])
    identifier = eval(sys.argv[2])
    pfield_index_list = eval(sys.argv[3])
    value_list = sys.argv[4].split()

    # Get input
    stdin = sys.stdin.readlines()
    score = ''.join(stdin)

    # Arpeggiate
    print arpeggiator(score, {0: statement, 1: identifier}, pfield_index_list,
                      value_list),
    
if __name__ == '__main__':
    main()

