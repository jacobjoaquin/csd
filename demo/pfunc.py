#!/usr/bin/env python
'''Csound Score Calculator

This command-line tool allows easy, quick and efficient operations on
Csound score code.

Example Equations::
    
    1.0
    x * x
    1.0 - x
    sin(x)
    x + x * random() * 0.01259
    7.00 + choice(['0.00', '0.03', '0.07', '0.11'])

Command-line::

    $ cat pfunc.sco | ./pfunc.py '1.0 - x' i 1 4 
    $ cat pfunc.sco | ./pfunc.py '1.0 - x' i 'range(1, 11)' 4
    $ cat pfunc.sco | ./pfunc.py '1.0 - x' i 1 '[4, 5]' 
    $ cat pfunc.sco | ./pfunc.py 'random()' i 1 4 0.1
    
'''

import sys

from math import ceil
from math import fabs
from math import floor
from math import fmod
from math import exp
from math import log
from math import log10
from math import pow
from math import sqrt
from math import acos
from math import asin
from math import atan
from math import atan2
from math import cos
from math import hypot
from math import sin
from math import tan
from math import degrees
from math import radians
from math import cosh 
from math import sinh
from math import tanh
from math import pi
from math import e
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

sys.path.append('../')  # Fix this.
from csd import sco
from csd.sco import event

# Generic pfunction
def eval_this(x):
    global eval_
    return eval(eval_)

def fround(x, n=8):
    '''Return a float rounded to the nth decimal place.'''
    
    return float(('%.' + str(n) + 'f') % x)

# Get argv from command-line
eval_ = sys.argv[1]
statement = list(sys.argv[2])
identifier = eval(sys.argv[3])
pfield = eval(sys.argv[4])
if len(sys.argv) == 6:
    seed(sys.argv[5])

# Get input
s = ''.join(sys.stdin.readlines())
    
# Where the magic happens
print sco.map_(s, {0: statement, 1: identifier}, pfield, eval_this),

