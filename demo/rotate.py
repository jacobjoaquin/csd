#!/usr/bin/env python
'''Testing playground.'''

import sys

sys.path.append('../')  # Fix this.
from csd import sco
from csd.sco import event

score = '''f 1 0 8192 10 1

i 1 0 4 1.0 440 0.9
i 1 + . 0.7 .   0.25

i 2 0 4 1.0 880 1.0    ; p6 is pan
i 2 + . .   .   0.25
i 2 + . .   .   0.999
i 2 + . .   .   0.0
'''
    
class MyRotateClass:
    def __init__(self, r, list_of_values):
        self.data = list_of_values
        self.r = r % len(self.data)
        
    def get(self, x):
        output = self.data[self.r]
        self.r = (self.r + 1) % len(self.data)
        return output

pfield_index = 6
rotate = 1

selection = sco.select(score, {0: 'i', 1: 2})

# get all pfields-6 and place into list
values = []
for k, v in sorted(selection.items()):
    values.append(event.get(v, pfield_index))

r = MyRotateClass(rotate, values)
selection = sco.operate_numeric(selection, pfield_index, r.get)
print sco.merge(score, selection)


