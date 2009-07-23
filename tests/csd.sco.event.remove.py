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

'''Tests for remove()'''

import sys
sys.path.append('../')
from csd.sco import event as s

def test(n, event, pfield, expect):
    result = s.remove(event, pfield)
    did_pass = result == expect

    return did_pass, n, 'remove()', str(expect), str(result)

print test(0, 'i 0 1', 2, ('i 0 ', '1'))
print test(1, 'i 0 1; comment', 2, ('i 0 ; comment', '1'))
print test(2, 'i 0 /*asdf*/1; comment', 2, ('i 0 /*asdf*/; comment', '1'))
print test(3, 'i 0 1', 3, ('i 0 1', ''))
print test(4, '', 0, ('', ''))
print test(5, 'i 0 1.0 440', 2, ('i 0  440', '1.0'))


