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

'''Tests tokenize()'''

import sys

from csd.sco import event

def test(n, line, expect):
    result = event.tokenize(line)
    did_pass = result == expect

    return did_pass, n, 'token_type()', str(expect), str(result)

print test(0, '', [])
print test(1, ' ', [' '])
print test(2, '  ', ['  '])
print test(3, 'i', ['i'])
print test(4, 'f', ['f'])
print test(5, 'i 0', ['i', ' ', '0'])
print test(6, '  i 0', ['  ', 'i', ' ', '0'])
print test(7, '  i  0 3', ['  ', 'i', '  ', '0', ' ', '3'])
print test(8, 'i 0 3 ; my comment', ['i', ' ', '0', ' ', '3', ' ',
              '; my comment'])
print test(9, 'i 0 3 /* my comment */', ['i', ' ', '0', ' ', '3', ' ',
              '/* my comment */'])
print test(10, 'i 0 3 /* my comment */ ', ['i', ' ', '0', ' ', '3', ' ',
              '/* my comment */', ' '])
print test(11, 'i 0 3 ; my comment ', ['i', ' ', '0', ' ', '3', ' ',
              '; my comment '])
print test(12, '/* my comment */i  0 3', ['/* my comment */', 'i', '  ', '0',
               ' ', '3'])
print test(13, 'i/* my comment */ 0 3', ['i', '/* my comment */', ' ', '0',
               ' ', '3'])
print test(14, 'i/* my comment */0 3', ['i', '/* my comment */', '0', ' ',
               '3'])
print test(15, 'i/* my comment */0/*foo*/3', ['i', '/* my comment */', '0',
               '/*foo*/', '3'])
print test(16, 'i1 0', ['i', '1', ' ', '0'])
print test(17, ' /*a*/ /*b*/i 1 0', [' ', '/*a*/', ' ', '/*b*/', 'i', ' ', '1',
               ' ', '0'])
print test(18, ' /*a*/ /*b*/i1 0', [' ', '/*a*/', ' ', '/*b*/', 'i', '1', ' ',
               '0'])
print test(19, 'i 0 3; my comment', ['i', ' ', '0', ' ', '3', '; my comment'])

print test(20, 'i [~] 0 [~]', ['i', ' ', '[~]', ' ', '0', ' ', '[~]'])
print test(21, 'i {{foo}} 0 {{bar}}', ['i', ' ', '{{foo}}', ' ', '0', ' ',
                '{{bar}}'])
print test(22, 'i "foo" 0 "foo"', ['i', ' ', '"foo"', ' ', '0', ' ', '"foo"'])
print test(23, 'i 1/*foo*/4', ['i', ' ', '1', '/*foo*/', '4'])
print test(24, 'i 1 0/*foo*/4 0.5 440 ;comment',
               ['i', ' ', '1', ' ', '0', '/*foo*/', '4', ' ', '0.5', ' ', '440', ' ', ';comment'])
print test(25, 'i /**/ 1', ['i', ' ', '/**/', ' ', '1'])
print test(26, 'i 1;', ['i', ' ', '1', ';'])


