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

'''Tests for replace()'''

import sys

from csd.sco import selection

def test(n, expect, score_dict, pfield, pgenerator, *args):
    result = selection.replace(score_dict, pfield, pgenerator, *args)
    did_pass = result == expect

    return did_pass, n, 'replace()', str(expect), str(result)

def one(): return 1
print test(0, {0: 'i 1'}, {0: 'i 1'}, 1, one)
print test(1, {0: 'i 1'}, {0: 'i 2'}, 1, one)

def macro(): return '$macro'
print test(0, {0: 'i 1'}, {0: 'i 1'}, 1, one)
print test(1, {0: 'i $macro'}, {0: 'i 1'}, 1, macro)


