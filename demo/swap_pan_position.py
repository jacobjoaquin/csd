#!/usr/bin/env python
'''An example that demonstrates how a script can operate a custom
python function for every pfield in a column for a select group of
events from a score.

Here's the scenario.  You've listened to your piece and have decided
that the panning in instrument 2 would sound better if the left and
right channels were swapped.  How could you do this with CSD?

#. Define a pf_function, swap_pan_position()
#. Select all i-events for instr 2 from the score
#. Operate on every pfield 6 in the selection with swap_pan_position()
#. Merge the modifications with the original score

The code::

    def swap_pan_position(x):
        return 1.0 - x
    
    selection = sco.select(score, {0: 'i', 1: 2})
    selection = sco.operate_numeric(selection, 6, swap_pan_position)
    new_score = sco.merge(score, selection)
    
The original score compared with the modified score::
    
    __original score__
    f 1 0 8192 10 1
    
    i 1 0 4 1.0 440 0.9
    i 1 + . 0.7 .   0.25
    
    i 2 0 4 1.0 880 1.0    ; p6 is pan
    i 2 + . .   .   0.25
    i 2 + . .   .   0.999
    i 2 + . .   .   0.0
    
    __modified score__
    f 1 0 8192 10 1
    
    i 1 0 4 1.0 440 0.9
    i 1 + . 0.7 .   0.25
    
    i 2 0 4 1.0 880 0.0    ; p6 is pan
    i 2 + . .   .   0.75
    i 2 + . .   .   0.001
    i 2 + . .   .   1.0

Now imagine applying this technique to dozens, or even hundreds of
events.  Be sure to follow the links below, as each will help explain
each of the components in further detail. (assuming you are reading
from the CSD manual)

    :term:`pattern`, :term:`pf_function`, :term:`selection`,
    :term:`score`

    :func:`csd.sco.merge`, :func:`csd.sco.operate_numeric`,
    :func:`csd.sco.select`

'''

import sys

sys.path.append('../')  # Fix this.
from csd import sco

score = '''f 1 0 8192 10 1

i 1 0 4 1.0 440 0.9
i 1 + . 0.7 .   0.25

i 2 0 4 1.0 880 1.0    ; p6 is pan
i 2 + . .   .   0.25
i 2 + . .   .   0.999
i 2 + . .   .   0.0
'''

def swap_pan_position(x):
    return 1.0 - x

selection = sco.select(score, {0: 'i', 1: 2})
selection = sco.operate_numeric(selection, 6, swap_pan_position)
new_score = sco.merge(score, selection)

# Compare original score with modified score
print '__original score__'
print score
print '__modified score__'
print new_score


