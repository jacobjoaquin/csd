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

'''Tests for csd.sco.preprocessor.value_to_carry'''

import sys

from csd.sco.preprocessor import value_to_carry

def test(n, score, expect):
    result = value_to_carry(score)
    did_pass = result == expect

    return did_pass, n, 'value_to_carry', str(expect), str(result)

score = '''\
i 1 2 3
i 1 2 3
i 1 2 3
'''
expect = '''\
i 1 2 3
i 1 2 .
i 1 2 .
'''
print test(0, score, expect)

score = '''\
i 1 2 3
i 1 2 3
i 2 2 3
'''
expect = '''\
i 1 2 3
i 1 2 .
i 2 2 3
'''
print test(1, score, expect)

score = '''\
i 1 2 3
i 1 2 3

i 1 2 3
'''
expect = '''\
i 1 2 3
i 1 2 .

i 1 2 3
'''
print test(2, score, expect)

score = '''\
i 1 2 3 4
i 1 2 3 4
i 1 2 5 4
i 1 2 5 4
'''
expect = '''\
i 1 2 3 4
i 1 2 . .
i 1 2 5 .
i 1 2 . .
'''
print test(3, score, expect)

score = '''\
i 1 2 $foo
i 1 2 $foo
i 1 2 $foo
'''
expect = '''\
i 1 2 $foo
i 1 2 .
i 1 2 .
'''
print test(4, score, expect)

