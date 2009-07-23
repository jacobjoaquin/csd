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

'''Tests that csd has been installed.

Use::
    
    ./test.py

Output::

    i 1 0 0.25 0.001
    i 1 + 0.25 0.778

'''

import sys

from csd.sco import map_

if __name__ == '__main__':
    score = 'i 1 0 0.25 0.999\ni 1 + 0.25 0.222'
    print map_(score, {0: 'i'}, 4, lambda x: 1.0 - x)

