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

'''Sets space between a statement and the first active element.

.. program:: s_spacer
.. cmdoption:: -s  Whitespace amount between statement and identifier

Example::
    
    $ cat s_spacer.sco | ./s_spacer.py
    
Before::
    
    i1 0 0.25 0.5 7.00
    i1 + .    0.5 7.00
    i1 + .    0.5 8.00
    i1 + .    0.5 8.00
    i1 + .    0.6 7.06
    i1 + .    0.6 7.06
    i1 + .    0.6 6.06
    i1 + .    0.6 6.06
    i1 + .    0.6 7.00
    i1 + .    0.6 7.00

After::
    
    i 1 0 0.25 0.5 7.00
    i 1 + .    0.5 7.00
    i 1 + .    0.5 8.00
    i 1 + .    0.5 8.00
    i 1 + .    0.6 7.06
    i 1 + .    0.6 7.06
    i 1 + .    0.6 6.06
    i 1 + .    0.6 6.06
    i 1 + .    0.6 7.00
    i 1 + .    0.6 7.00

'''

import re
import sys

from csd.sco import event
from csd.sco import element

from optparse import OptionParser
    
if __name__ == '__main__':
    # Get command-line flags
    u = ['usage: <stdout> |']
    u.append('python s_spacer.py -s[pad amount]')
    usage = ' '.join(u)
    parser = OptionParser(usage)
    parser.add_option("-s", default=1, dest='spacer', help='spacer')
    (options, args) = parser.parse_args()

    options.spacer = int(options.spacer)  # Flag option needs to be an int
    stdin = sys.stdin.readlines()         # Get data from stdin
    sco = []                              # New score lines as list items

    for e in stdin:
        sco.append(event.statement_spacer(e, options.spacer))

    print ''.join(sco),

