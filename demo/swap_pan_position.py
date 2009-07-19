#!/usr/bin/env python
'''An example that demonstrates how a script can operate a custom
python function for every pfield in a column for a select group of
events from a score used the map_() function.

Here's the scenario.  You've listened to your piece and have decided
that the panning in instrument 2 would sound better if the left and
right channels were swapped.  How could you do this with CSD?


#. Define a pf_function, swap_pan_position()
#. Define a pattern to select instrument 2 events.
#. Choose which pfield column to operate on.
#. Run selected pfield data through swap_pan_position() with map_

The code::

    def swap_pan_position(x):
        return 1.0 - x
    
    new_score = sco.map_(score, {0: 'i', 1: 2}, 6, swap_pan_position)
    
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

new_score = sco.map_(score, {0: 'i', 1: 2}, 6, swap_pan_position)

# Compare original score with modified score
print '__original score__'
print score
print '__modified score__'
print new_score


