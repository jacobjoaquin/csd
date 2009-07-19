#!/usr/bin/env python
'''Testing playground.'''

import sys
from math import *

sys.path.append('../')  # Fix this.
from csd import sco
from csd.sco import event

# Get argv from command-line
statement = list(sys.argv[1])
identifier = eval(sys.argv[2])
pfield = eval(sys.argv[3])
eval_ = sys.argv[4]

# Get input
s = ''.join(sys.stdin.readlines())

# Generic pf_function
def eval_this(x):
    global eval_
    return eval(eval_)
    
# Where the magic happens
print sco.map_(s, {0: statement, 1: identifier}, pfield, eval_this),

