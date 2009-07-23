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

'''Exchanges all score columns for a specified statement and
identifier.

.. program:: swap_columns
.. cmdoption:: -s  Statement (required)
.. cmdoption:: -i  Identifier (required)
.. cmdoption:: -a  Pfield A (required)
.. cmdoption:: -b  Pfield B (required)

The following command-line swaps pfields 4 and 5 for all instrument
1 events::

    $ cat swap_columns.sco | ./swap_columns.py -si -i1 -a4 -b5

Before::
   
    i 1 0 1 7.00 0.8
    i 1 + . 7.02 0.8
    i 1 + . 7.04 1.0
    i 1 + . 7.05 0.8

After::
   
    i 1 0 1 0.8 7.00
    i 1 + . 0.8 7.02
    i 1 + . 1.0 7.04
    i 1 + . 0.8 7.05

'''

import sys

from csd import sco
from csd.sco import selection

def main():
    # Get argv from command-line
    statement = list(sys.argv[1])
    identifier = eval(sys.argv[2])
    a = int(sys.argv[3])
    b = int(sys.argv[4])

    # Get stdin
    stdin = sys.stdin.readlines()
    s = ''.join(stdin)

    selected = sco.select(s, {0: statement, 1: identifier})
    selected = selection.swap(selected, a, b)
    print sco.merge(s, selected)

if __name__ == '__main__':
    main()

