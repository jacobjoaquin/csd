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

'''Tests for statement_spacer'''

import sys
sys.path.append('../')
from csd.sco import event

def test(n, e, s, expect):
    result = event.statement_spacer(e, spacer=s)
    did_pass = result == expect

    return did_pass, n, 'statement_spacer', str(expect), str(result)

print test(0, 'i', 0, 'i')
print test(1, 'i', 1, 'i')
print test(2, 'i1', 0, 'i1')
print test(3, 'i1', 1, 'i 1')
print test(4, 'i1', 2, 'i  1')
print test(5, 'i1 1 0 440', 2, 'i  1 1 0 440')
print test(6, '  i1 1 0 440', 2, '  i  1 1 0 440')
print test(7, 'i 1', 1, 'i 1')
print test(8, 'i    1', 1, 'i 1')
print test(9, 'i1', 4, 'i    1')
print test(10, 'i/*c*/1', 0, 'i/*c*/1')
print test(11, 'i/*c*/1', 1, 'i /*c*/1')
print test(12, ' i/*c*/1', 1, ' i /*c*/1')

