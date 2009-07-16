#!/usr/bin/env python

import sys

sys.path.append('../')  # Fix this.
from csd import sco

def swap_pan_position(x):
    return 1.0 - x

score = '''f 1 0 8192 10 1

i 1 0 4 1.0 440  ; comment
i 1 + . 0.7   .
i 1 + . 0.5   .

i 2 0 4 1.0 880 1.0    ; p6 is pan
i 2 + . .   .   0.333
i 2 + . .   .   0.0
'''

pattern = {0: 'i', 1: 2}
selection = sco.select(score, pattern)
selection = sco.operate_numeric(selection, 6, swap_pan_position)
score = sco.merge(score, selection)

print score
