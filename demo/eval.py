#!/usr/bin/env python
'''Testing playground.'''

import sys

sys.path.append('../')  # Fix this.
from csd import sco
from csd.sco import event

# Get argv from command-line
statement = list(sys.argv[1])
identifier = eval(sys.argv[2])
pfield = sys.argv[3]
eval_ = sys.argv[4]

# Get input
stdin = sys.stdin.readlines()
s = ''.join(stdin)

def eval_this(p):
    global eval_
    return eval(eval_)
    
print sco.map_(s, {0: statement, 1: identifier}, pfield, eval_this),

