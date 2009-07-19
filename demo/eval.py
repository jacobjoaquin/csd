#!/usr/bin/env python
'''Testing playground.'''

import sys
from math import *
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

# Get argv from command-line
statement = list(sys.argv[1])
identifier = eval(sys.argv[2])
pfield = eval(sys.argv[3])
eval_ = sys.argv[4]
if len(sys.argv) == 6:
    seed(sys.argv[5])

# Get input
s = ''.join(sys.stdin.readlines())

# Generic pf_function
def eval_this(x):
    global eval_
    return eval(eval_)
    
# Where the magic happens
print sco.map_(s, {0: statement, 1: identifier}, pfield, eval_this),


