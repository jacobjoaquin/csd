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

'''Tests for swap()'''

import sys

from csd.sco import selection

def test(n, score_dict, x, y, expect):
    result = selection.swap(score_dict, x, y)
    did_pass = result == expect

    return did_pass, n, 'swap()', str(expect), str(result)
    
print test(0, {0: 'i 1 2', 1: 'i 3 4'}, 1, 2, {0: 'i 2 1', 1: 'i 4 3'})
print test(1, {0: 'i 1 2', 1: 'i 3 4', 2: 'i 5 6'}, 1, 2, 
           {0: 'i 2 1', 1: 'i 4 3', 2: 'i 6 5'})
print test(2, {0: 'i 1 2', 1: 'i 3 4', 2: ''}, 1, 2,
           {0: 'i 2 1', 1: 'i 4 3', 2: ''})
print test(3, {0: 'i $a "b"', 1: 'i $c "d"'}, 1, 2,
           {0: 'i "b" $a', 1: 'i "d" $c'})
print test(4, {0: 'i 1 2 3', 1: 'i 4 5 6'}, 1, 3,
           {0: 'i 3 2 1', 1: 'i 6 5 4'})

