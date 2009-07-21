#!/usr/bin/env python
'''Testing playground.'''

import sys

sys.path.append('../')  # Fix this.
from csd import sco

score = '''
f 2 0 1 7  -1 0.5 1  0.5 -1           ; Triangle
f 3 0 1 7  1  1 -1                    ; Saw
f 4 0 1 7  1  0.5 1  0     -1 0.5-1  ; Square
'''
bar = lambda x: x * x * x

print sco.map_(score, {0: 'f'}, 4, lambda x: x * x * x)

