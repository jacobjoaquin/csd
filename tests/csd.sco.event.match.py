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

'''Tests for match()'''

import sys

from csd.sco import event as s

def test(n, line, pattern, expect):
    result = s.match(line, pattern)
    did_pass = result == expect

    return did_pass, n, 'match()', str(expect), str(result)

print test(0, 'i', {0: 'i'}, True)
print test(1, 'f', {0: 'i'}, False)
print test(2, 'i 1 0 4', {0: 'i'}, True)
print test(3, 'i 1 0 4', {3: '4'}, True)
print test(4, 'i 1 0 4', {3: '3'}, False)
print test(5, 'i 1 0 4', {3: range(1, 5)}, True)
print test(6, 'i 1 0 4', {3: range(6, 10)}, False)
print test(7, 'i 1 0 4', {3: range(11, 15)}, False)
print test(8, 'i 1 0 4', {0: 'i', 1: '1'}, True)
print test(9, 'i 1 0 4', {0: 'i', 1: '2'}, False)
print test(10, 'i 1 0 4', {0: list('if'), 1: '1'}, True)
print test(11, 'f 1 0 4', {0: list('if'), 1: '1'}, True)
print test(12, 'x 1 0 4', {0: list('if'), 1: '1'}, False)
print test(13, 'i 1 0 $foo', {3: '$foo'}, True)
print test(14, 'i 1 0 4', {3: 4}, True)
print test(15, 'i 1 0 4', {3: 4.1}, False)
print test(15, 'i 1 0 [~]', {3: '[~]'}, True)
print test(16, 'i 1 0 "foo"', {3: '"foo"'}, True)
print test(17, 'i 1 0 {{foo}}', {3: '{{foo}}'}, True)
print test(18, 'i 1 0 4', {}, False)

