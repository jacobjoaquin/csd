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

'''Tests for number_of_pfields()'''

import sys

from csd.sco import event as s

def test(n, line, expect):
    result = s.number_of_pfields(line)
    did_pass = result == expect

    return did_pass, n, 'number_of_pfields()', str(expect), str(result)

print test(0, 'i', 1)
print test(1, 'i\n', 1)
print test(2, 'i 1', 2)
print test(3, 'i1', 2)
print test(4, 'i1 0 1', 4)
print test(5, 'i1 + .', 4)
print test(6, 'i1 + . $freq', 5)
print test(7, 'i1 + . [~ * 100 + 100]', 5)
print test(8, 'i1 + . [~ * 100 + 100] 440', 6)
print test(9, 'i1 + . ; this is a comment', 4)
print test(10, 'i1 + . /* this is a comment */', 4)
print test(11, 'i1 + . /* this is a comment */ 5', 5)
print test(12, 'i$instr + .', 4)
print test(13, 'i"instr" + .', 4)
print test(14, "i'instr' + .", 4)
print test(15, 'i "instr" + .', 4)
print test(16, 'i {{instr}} + .', 4)
print test(17, 'i 1 0 .0', 4)
print test(18, 'i 1 0 0.', 4)
print test(19, 'i 1 0 0.', 4)
print test(20, 'i 1 0 0.', 4)
print test(21, 'i 1 0 $macro.with.dots.in.name', 4)
print test(22, 'i1 + . ; this is a comment 440 800', 4)
print test(23, 'i1 + . ; this is a "comment" 440 800', 4)
print test(24, 'i1 + . ; this is a [comment 440] 800', 4)
print test(25, 'i1 + . " " 1', 6)
print test(26, 'i1 + . {{ }} 1', 6)
print test(27, 'i1 + . {{" "}} 1', 6)
print test(28, 'i1 + . "{{ }}" 1', 6)
print test(29, 'i  [~]  0  [~]', 4)
print test(30, 'i  {{foo}}  0  {{foo }}', 4)
print test(31, 'i  "foo"  0  "foo "', 4)
print test(32, 'f 1 0 8192 19 1', 6)
print test(33, 'f1 0 8192 19 1', 6)
print test(34, 'z1 0 8192 19 1', 5)  # 'z' is non-statement
print test(35, 'i 1 0/*foo*/4 0.5 440 ;comment', 6)
print test(36, 'i 1 0/*foo*/ 4 0.5 440 ;comment', 6)
print test(37, 'i 1 0 /*foo*/4 0.5 440 ;comment', 6)


