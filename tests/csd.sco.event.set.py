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

'''Tests for set()'''

import sys
sys.path.append('../')
from csd.sco import event as s

def test(n, line, pf, v, expect):
    result = s.set(line, pf, v)
    did_pass = result == expect

    return did_pass, n, 'set()', str(expect), str(result)

print test(0, ' ', 0, '', ' ')
print test(1, '/* */', 0, '', '/* */')
print test(2, '/* */', 0, '', '/* */')
print test(3, '/* */ ', 0, '', '/* */ ')
print test(4, '/* */ /* */ ', 0, '', '/* */ /* */ ')
print test(5, 'i', 0, 'i', 'i')
print test(6, 'i', 0, 'f', 'f')
print test(7, '/* */ /* */ i', 0, 'f', '/* */ /* */ f')
print test(8, 'i 1', 1, '3', 'i 3')
print test(9, 'i 1 0 4 0.777', 4, '0.666', 'i 1 0 4 0.666')
print test(10, 'i 1 0 $foo', 3, '$bar', 'i 1 0 $bar')
print test(11, 'i 1 0 [~ * 100 + 100]', 3, '[~ * 440 + 440]',
               'i 1 0 [~ * 440 + 440]')
print test(12, 'i 1 0 "foo"', 3, '"bar"', 'i 1 0 "bar"')
print test(13, 'i 1 0 "foo"', 3, '"bar"', 'i 1 0 "bar"')
print test(14, 'i 1 0 4', 4, 'asdf', 'i 1 0 4')
print test(15, 'i 1 0 4', -1, 'asdf', 'i 1 0 4')
print test(16, 'i 1 0 {{foo}}', 3, '{{bar}}', 'i 1 0 {{bar}}')
print test(17, 'i 1 0 4 ; my comment', 3, '4.1', 'i 1 0 4.1 ; my comment')
print test(18, 'i 1 0 4; my comment', 3, '4.1', 'i 1 0 4.1; my comment')
print test(19, 'i 1 0 .', 3, '4', 'i 1 0 4')
print test(20, 'i 1 0 <', 3, '.', 'i 1 0 .')
print test(21, 'i 1 0 (', 3, '.', 'i 1 0 .')
print test(22, 'i 1 0 )', 3, '.', 'i 1 0 .')
print test(23, 'i 1 0 ~', 3, '.', 'i 1 0 .')
print test(24, 'i 1 0 +', 3, '.', 'i 1 0 .')
print test(25, 'i 1 0 ^+1', 3, '.', 'i 1 0 .')
print test(26, 'i 1 0 ^-1', 3, '.', 'i 1 0 .')
print test(27, 'i 1 0 !', 3, '.', 'i 1 0 .')
print test(28, 'i 1 0 np4', 3, 'np5', 'i 1 0 np5')
print test(29, 'i 1 0 pp4', 3, 'np5', 'i 1 0 np5')
print test(30, 'i 1 0 np14', 3, 'np5', 'i 1 0 np5')
print test(21, 'i 1 0 pp14', 3, 'np5', 'i 1 0 np5')
print test(22, 'i 1 2 $three 4 5 "six"', 3, '"six"', 'i 1 2 "six" 4 5 "six"')
print test(23, 'i 1 2 $three 4 5 "six"', 6, '$three',
           'i 1 2 $three 4 5 $three')
print test(24, 'i 1 0/*foo*/4 0.5 440 ;comment', 5, '',
           'i 1 0/*foo*/4 0.5  ;comment')
print test(25, 'i 1 0 4 0.5 440 ;comment', 5, '',
           'i 1 0 4 0.5  ;comment')
print test(26, 'i 1 0 4 0.5 440 ;comment', '5', '',
               'i 1 0 4 0.5  ;comment')

