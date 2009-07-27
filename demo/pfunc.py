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

'''**Csound Pfield Calculator**

This command-line tool allows easy, quick and efficient operations on
Csound score code.  The scripts comes equipped with dozens of functions
imported from Python Libraries math and random.  For a full reference
of supported functions, look at the import statements in
``demo/pfunc.py``.

**How it works**

pfunc operates on Csound score code piped into the script, requiring
four arguments: *statement*, *instrument*, *pfield_index*, *pfunction*::

    <stdout> | ./pfunc.py STATEMENT INSTR PFIELD FUNCTION

To use the existing pfield value, use the variable x in the function.
Non-numeric pfield data types, i.e. carry, expression, etc, are
ignored by pfunc, and will be preserved.

The following example applies the function ``'1.0 - x'`` to every
pfield 6 for all instrument 1 events::
    
    cat pfunc.sco | ./pfunc.py i 1 6 '1.0 - x'

Before::

    f 1 0 8192 10 1
    
    i 1 0 0.25 0.5 7.00 1.0    # p6 is pan
    i 1 + 0.25 0.5 7.00 0.5
    i 1 + 0.25 0.5 8.00 0.222
    i 1 + 0.25 0.5 8.00 0.1
    
    i 2 + 0.25 0.6 7.06 1.0
    i 2 + 0.25 0.6 7.06 0.5
    i 2 + 0.25 0.6 6.06 0.222
    i 2 + 0.25 0.6 6.06 0.1

After::
    
    f 1 0 8192 10 1

    i 1 0 0.25 0.5 7.00 0.0    # p6 is pan
    i 1 + 0.25 0.5 7.00 0.5
    i 1 + 0.25 0.5 8.00 0.778
    i 1 + 0.25 0.5 8.00 0.9
    
    i 2 + 0.25 0.6 7.06 1.0
    i 2 + 0.25 0.6 7.06 0.5
    i 2 + 0.25 0.6 6.06 0.222
    i 2 + 0.25 0.6 6.06 0.1

Multiple statements, instruments and pfields may be passed in as
arguments.  For statements, type in all characters without white space,
e.g. ``if``.  For instruments and pfields, there are two approaches
(maybe more).  The manual method is to create a quoted python list. e.g.
``'[1, 2, 3]'``.  For integer sequences, you can use a quote python
range function e.g. ``'range(1, 10)'`` includes numberes 1 through 9.

Instruments 1 through 10, pfield 4::
    
    ./pfunc.py i 'range(1, 11)' 4 'x'   

Instrument 1, pfields 4 and 5::
    
    ./pfunc.py i 1 '[4, 5]' 'x'

F-tables and instruments 1 through 999, pfields 1 through 999::
    
    ./pfunc.py if 'range(1, 1000)' 'range(1, 1000)' 'x'
    
Function examples::
    
    1.0
    x * x
    1.0 - x
    x / 32768.0
    sin(x)
    x + x * random() * pow(2, 1 / 12)
    7.00 + choice(['0.00', '0.03', '0.07', '0.11'])
    pi

.. note:: The name **pfunc** is derived from **pfield function**, and
    is not at all a reference to George Clinton and the Parliament
    Funkadelic (P-Funk).  *Or is it?*
    
'''

import sys

from math import acos
from math import asin
from math import atan
from math import atan2
from math import ceil
from math import cos
from math import cosh 
from math import degrees
from math import e
from math import exp
from math import fabs
from math import floor
from math import fmod
from math import hypot
from math import log
from math import log10
from math import pi
from math import pow
from math import radians
from math import sin
from math import sinh
from math import sqrt
from math import tan
from math import tanh
from random import betavariate
from random import choice
from random import expovariate
from random import gammavariate
from random import gauss
from random import lognormvariate
from random import normalvariate
from random import paretovariate
from random import seed
from random import random
from random import randint
from random import uniform
from random import vonmisesvariate
from random import weibullvariate

from csd import sco
from csd.sco import event

def __func(x):
    '''Runs pfield x through a function stored in __formula.'''
    
    global __formula
    return eval(__formula)

def fround(x, n=8):
    '''Return a float rounded to the nth decimal place.'''
    
    return float(('%.' + str(n) + 'f') % x)

def pfunc(score, statement, identifier, pfield, formula):
    '''Returns a modified score with selected pfields processed with
    the provided formula.
    
    A global variable is used because a pfunction requires that its
    arguments be of csd type numeric.  Thus, passing a forumula string
    does not work.

    '''
    
    global __formula
    __formula = formula
    return sco.map_(score, {0: statement, 1: identifier}, pfield, __func)

# Stores function. Initial state of 'x' is to do nothing.
__formula = 'x'

def main():
    # Get argv from command-line
    statement = list(sys.argv[1])
    identifier = eval(sys.argv[2])
    pfield = eval(sys.argv[3])
    formula = sys.argv[4]
    if len(sys.argv) == 6:
        seed(sys.argv[5])
    
    # Get input
    s = ''.join(sys.stdin.readlines())
        
    # Where the magic happens
    print pfunc(s, statement, identifier, pfield, formula),

if __name__ == '__main__':
    main()

