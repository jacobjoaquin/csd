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

'''Tests for select_all()'''

import sys

from csd import sco

def test(n, score, expect):
    result = sco.select_all(score)
    did_pass = result == expect

    return did_pass, n, 'select_all()', str(expect), str(result)

print test(0, 'i 1 0 1', {0: 'i 1 0 1'})
print test(1, 'i 1 0 1\n ', {0: 'i 1 0 1', 1: ' '})
print test(2, 'i 1 0 1\ni 1 1 1', {0: 'i 1 0 1', 1: 'i 1 1 1'})
print test(3, 'i 1 0 1\n', {0: 'i 1 0 1', 1: ''})
print test(4, 'i 1 0 1\n\n', {0: 'i 1 0 1', 1: '', 2: ''})
print test(5, 'i 1 0 1\ni 1 1 1', {0: 'i 1 0 1', 1: 'i 1 1 1'})
print test(6, 'i 1 0 1\ni 1 1 1\nf 1', {0: 'i 1 0 1', 1: 'i 1 1 1', 2: 'f 1'})
print test(7, 'i 1 0 1\nf 1\ni 1 1 1', {0: 'i 1 0 1', 1: 'f 1', 2: 'i 1 1 1'})
print test(8, 'i 1 0 1\nf 1\ni 1 1 1\ne',
           {0: 'i 1 0 1', 1: 'f 1', 2: 'i 1 1 1', 3: 'e'})
print test(9, 'i 1 0 1\nf 1\ni 2 1 1\n',
           {0: 'i 1 0 1', 1: 'f 1', 2: 'i 2 1 1', 3: ''})
print test(10, 'i 1 0 1\n\n\ni 1 1 1\n',
           {0: 'i 1 0 1', 1: '', 2: '', 3: 'i 1 1 1', 4: ''})

