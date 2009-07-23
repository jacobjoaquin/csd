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

'''Tests for pop()'''

import sys
sys.path.append('../')
from csd.sco import event as s

def test(n, event, expect):
    result = s.pop(event)
    did_pass = result == expect

    return did_pass, n, 'pop()', str(expect), str(result)

print test(0, 'i 0 1', ('i 0 ', '1'))
print test(1, 'i 1 0/*foo*/4 0.5 440;comment', ('i 1 0/*foo*/4 0.5 ;comment', '440'))
print test(2, 'i 1 0 4 0.5 440', ('i 1 0 4 0.5 ', '440'))

print test(3, 'i 1 0/*foo*/4 0.5 440 ;comment', ('i 1 0/*foo*/4 0.5  ;comment', '440'))
print test(4, 'i 1 0 /*foo*/ 4 0.5 440 ;comment', ('i 1 0 /*foo*/ 4 0.5  ;comment', '440'))


