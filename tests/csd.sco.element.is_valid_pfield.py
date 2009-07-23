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

'''Tests for is_valid_pfield'''

import sys

from csd.sco import element

def test(n, e, expect):
    result = element.is_valid_pfield(e)
    did_pass = result == expect

    return did_pass, n, 'is_valid_pfield', str(expect), str(result)

print test(0, 's', True)
print test(1, ' ', False)
print test(2, '; comment', False)
print test(3, '1', True)
print test(4, '1.1', True)
print test(5, '"foo"', True)
print test(6, '{{foo}}', True)
print test(7, '$foo', True)
print test(8, '<', True)
print test(9, '!', True)
print test(10, 'np4', True)
print test(11, 'pp4', True)
print test(12, '.', True)
print test(13, '(', True)
print test(14, ')', True)
print test(15, '~', True)
print test(16, '.+3', True)
print test(17, '/* c */', False)
print test(18, 'i 1', False)
print test(19, ' i', False)
print test(20, 'i ', False)
print test(21, '/*f*/i', False)
print test(22, '[~]', True)
print test(23, '[~]', True)
print test(24, '[~ * 100.01 + 100.01]', True)
print test(25, '', False)
print test(26, None, False)


