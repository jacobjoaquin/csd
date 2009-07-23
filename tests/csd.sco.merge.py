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

'''Tests for merge()'''

import sys
sys.path.append('../')
from csd import sco

def test(n, score, score_dict, expect):
    result = sco.merge(score, score_dict)
    did_pass = result == expect

    return did_pass, n, 'merge()', str(expect), str(result)

print test(0, 'i', {0: 'f'}, 'f')
print test(1, 'i 1', {0: 'i 2'}, 'i 2')
print test(2, 'i 1\ni 2', {0: 'i 3'}, 'i 3\ni 2')
print test(3, 'i 1\ni 2\ni 3', {0: 'i 3', 2: 'i 1'}, 'i 3\ni 2\ni 1')
print test(4, 'i 1\ni 2\ni 3', {1: 'i 4\ni 5'}, 'i 1\ni 4\ni 5\ni 3')
print test(5, 'i\n ', {0: 'f'}, 'f\n ')
print test(6, 'i\n', {0: 'f'}, 'f\n')
print test(7, 'i 1', {0: ['i 2', 'i 3']}, 'i 2\ni 3')
print test(8, 'i 1', {0: ['i 2', 'i 3', '']}, 'i 2\ni 3\n')
print test(9, 'i 1\ni 4', {0: ['i 2', 'i 3', '']}, 'i 2\ni 3\n\ni 4')
print test(10, 'i 1\ni 4', {0: ['i 2', ['i 3', 'i 5'], 'i 6']},
            'i 2\ni 3\ni 5\ni 6\ni 4')
print test(11, 'i 1\ni 4', {0: ['i 2', ['i 3', '', '', 'i 5'], 'i 6']},
            'i 2\ni 3\n\n\ni 5\ni 6\ni 4')

