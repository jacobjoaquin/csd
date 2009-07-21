#!/usr/bin/env python
'''Testing playground.'''

import sys

sys.path.append('../')  # Fix this.
from csd import sco
from csd.sco import selection

score = []

my_measure = '''
i 1 0 1 1.0 440
i 1 + . .   330
i 1 + . .   550
i 1 + . .   660
'''

score.append('''f 1 0 8192 10 1''')

def play_measure(start, measure, transpose):
    selected = sco.select(measure, {0: 'i'})
    
    # Change start times
    selected = selection.operate_numeric(selected, 2, lambda x: x + start)
    
    # Transpose
    _transpose = lambda x: x * pow(2, transpose / 12.0)
    selected = selection.operate_numeric(selected, 5, _transpose)
    
    return sco.merge(measure, selected)

for i in range(0, 8):
    print play_measure(i * 4, my_measure, i * 2),
    

