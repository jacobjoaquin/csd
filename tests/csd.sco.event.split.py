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

'''Tests for split()'''

import sys
sys.path.append('../')
from csd.sco import event as s

def test(n, line, expect):
    result = s.split(line)
    did_pass = result == expect

    return did_pass, n, 'split()', str(expect), str(result)

print test(0, '', [])
print test(1, 'i', ['i'])
print test(2, ' i', ['i'])
print test(3, 'i 1', ['i', '1'])
print test(4, 'i1', ['i', '1'])
print test(5, 'i"instrname"', ['i', '"instrname"'])
print test(6, 'i "instrname"', ['i', '"instrname"'])
print test(7, 'i$macro', ['i', '$macro'])
print test(8, 'i 0 1 440 6.666', ['i', '0', '1', '440', '6.666'])
print test(9, '   i    0  1   440  6.666   ', ['i', '0', '1', '440', '6.666'])
print test(10, 'i 0 1 440 6.666  ; comment', ['i', '0', '1', '440', '6.666',
               '; comment'])
print test(11, 'i 0 1 440 6.666  /* my comment */', ['i', '0', '1', '440',
               '6.666', '/* my comment */'])
print test(12, 'i 0 1 /*foo*/ 440 6.666  /* my comment */', ['i', '0', '1',
               '/*foo*/', '440', '6.666', '/* my comment */'])
print test(13, 'i 0 1/*foo*/ 1 /* my comment */', ['i', '0', '1', '/*foo*/',
               '1', '/* my comment */'])

print test(14, 'i 0 1/*foo*/1 /* my comment */', ['i', '0', '1', '/*foo*/',
               '1', '/* my comment */'])
print test(15, 'i 0 1 /* my comment */1 /* my comment */', ['i', '0', '1',
               '/* my comment */', '1', '/* my comment */'])
print test(16, 'i {{ }} 1', ['i', '{{ }}', '1'])               
print test(17, 'i {{  }} 1', ['i', '{{  }}', '1'])               
print test(18, 'i "  " 1', ['i', '"  "', '1'])               
print test(19, 'i 0 3; my comment', ['i', '0', '3', '; my comment'])
print test(20, 'f 0 3; my comment', ['f', '0', '3', '; my comment'])
print test(21, 'f0 3; my comment', ['f', '0', '3', '; my comment'])
# z is a non-statement
print test(22, 'z0 3; my comment', ['z0', '3', '; my comment'])  
print test(23, 'z0 3; my comment', ['z0', '3', '; my comment'])  
print test(24, 'i  {{foo}}  0  {{foo }}', ['i', '{{foo}}', '0', '{{foo }}'])
print test(25, 'i  "foo"  0  "foo "', ['i', '"foo"', '0', '"foo "'])

#Deprecated.  
#print test(26, 'i  [~]  0  [~]', ['i', '[~]', '0', '[~]'])

print test(27, 'i /**/ 1', ['i', '/**/', '1'])
print test(28, 'i 1;', ['i', '1', ';'])
print test(29, 'i 1 0 1 np4', ['i', '1', '0', '1', 'np4'])
print test(30, 'i 1 0 1 pp4', ['i', '1', '0', '1', 'pp4'])
print test(31, 'i 1 0 1 np4 5', ['i', '1', '0', '1', 'np4', '5'])
print test(32, 'i 1 0 1 pp4 5', ['i', '1', '0', '1', 'pp4', '5'])


