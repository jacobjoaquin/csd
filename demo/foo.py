#!/usr/bin/env python
'''Testing are for half-thought out ideas.'''

import sys

sys.path.append('../')  # Fix this.
from csd import sco
from csd.sco import selection

my_measure = '''
i 1 0 1 1.0 440 1.0
i 1 + . .   330 0.7
i 1 + . .   550 0.3
i 1 + . .   660 0.0
'''

def simple_mod(start, measure, transpose):
    selected = sco.select(measure, {0: 'i'})
    
    # Change start times
    selected = selection.operate_numeric(selected, 2, lambda x: x + start)
    
    # Transpose
    _transpose = lambda x: x * pow(2, transpose / 12.0)
    selected = selection.operate_numeric(selected, 5, _transpose)
    
    return sco.merge(measure, selected)

def complex_play(start, measure):
    selected = sco.select(measure, {0: 'i'})

    # Add 1
    selected = selection.operate_numeric(selected, 5, lambda x: x + 1)
    
    # Delay, transpose, swap pan, half amp
    s2 = selected.copy()
    s2 = selection.operate_numeric(s2, 2, lambda x: x + start + 0.125)
    _transpose = lambda x: x * pow(2, 7 / 12.0)
    s2 = selection.operate_numeric(s2, 5, _transpose)
    s2 = selection.operate_numeric(s2, 6, lambda x: 1.0 - x)
    s2 = selection.operate_numeric(s2, 4, lambda x: x * 0.5)
    
    output = []
    output.append(sco.merge(measure, selected))
    output.append(sco.merge(measure, s2))
    return ''.join(output)    
    
    
#for i in range(0, 8):
#    print simple_mod(i * 4, my_measure, i * 2),
    
#print complex_play(0, my_measure)
#print complex_play(4, my_measure)


# Serializing functions
f_list = (lambda x: x + 1, lambda x: x * 2)
this_measure = my_measure
selected = sco.select(this_measure, {0: 'i'})
for f in f_list:
    selected = selection.operate_numeric(selected, 5, f)
this_measure = sco.merge(this_measure, selected)
print 'this measure', this_measure


# Functions need arguments, specify pfield(s)
# Multiple types of functional pfunc type things:
#    do_all(pfield_index_list, pfunc, *args)       # processes all ievents
#                                                  # in block
#    do(pattern, pfield_index_list, [pfunc, *args], ...)  # with pattern
'''
def punch(score, *func_args):
 
this_measure = my_measure

punch(this_measure, [do_all(5, lambda x: (x + y), 1)],
                    [do({1: 2}, 6, lambda x: 1.0 - x)])
   
punch [ ]:
    this_measure

def foo(selection, *funcargs):
    for f in funcargs:
        
    return selection

section my_section::
    
    i 1 0 1 1.0 440 1.0
    i 1 + . .   330 0.7
    i 1 + . .   550 0.3
    i 1 + . .   660 0.0
    
my_section_2 = process([pattern={0: 'i'}, pf=6, pfunc=lambda x: x + 1],
                       [pattern={0: 'i'}, pf=5, pfunc=lambda x: 1.0 - x]:
                           
    i 1 0 1 1.0 440 1.0
    i 1 + . .   330 0.7
    i 1 + . .   550 0.3
    i 1 + . .   660 0.0

play(0, my_section_2)
    
play(0) process([pattern={0: 'i'}, pf=6, pfunc=lambda x: x + 1],
                [pattern={0: 'i'}, pf=5, pfunc=lambda x: 1.0 - x]:
                           
    i 1 0 1 1.0 440 1.0
    i 1 + . .   330 0.7
    i 1 + . .   550 0.3
    i 1 + . .   660 0.0

play.process([pattern={0: 'i'}, pf=6, pfunc=lambda x: x + 1],
             [pattern={0: 'i'}, pf=5, pfunc=lambda x: 1.0 - x],
             [pattern={0: 'i'}, pf=5, pfunc=add_multiply, (1, 2)],
    """
    i 1 0 1 1.0 440 1.0
    i 1 + . .   330 0.7
    i 1 + . .   550 0.3
    i 1 + . .   660 0.0
    """)
    
'''


