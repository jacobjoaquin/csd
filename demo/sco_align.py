#!/usr/bin/env python
'''Auto-aligns groupings of i-events.

This script can be used as command-line script as well as a module.

.. program:: sco_align
.. cmdoption:: -s  Statement padding
.. cmdoption:: -p  Pfield padding
.. cmdoption:: -c  Comment padding
.. cmdoption:: -m  Minimum pfield width
.. cmdoption:: -t  Statement types. eg '-ti' aligns only i-events.

Example::

    $ cat sco_align.sco | ./sco_align.py

Before::
    
    f1 0 8192 10 1 ; Sine
    f2 0 8192 7 -1 4096 1 4096 -1; Triangle
    f3 0 8192 7 1 8192 -1 ; Saw
    f4 0 8192 7 1 4096 1 0 -1 4096 -1 ; Square 
    
    i1 0 4 6.04 15000 2 100 81 50 56 20 1
    i1 + . . . . 101 . . . . . 
    
    i2 0 1 0.1 8.00 0.5 0.333333  ; Begin new section
    i2 + < [~ * 0.5 + 0.5] 5.01 . .  ; Expressions work
    i2 + 0.44 .   (    ! ; Various score preprocessors
    i9 0 26 "beats.wav" 4.114 ; A string
    i$verb 32 6.2 0.28 ; Deep comment

After::
    
    f 1 0 8192 10 1                           ; Sine
    f 2 0 8192 7  -1 4096 1  4096 -1          ; Triangle
    f 3 0 8192 7  1  8192 -1                  ; Saw
    f 4 0 8192 7  1  4096 1  0    -1 4096 -1  ; Square 
    
    i 1 0 4 6.04 15000 2 100 81 50 56 20 1
    i 1 + . .    .     . 101 .  .  .  .  .
    
    i 2     0  1    0.1             8.00  0.5 0.333333  ; Begin new section
    i 2     +  <    [~ * 0.5 + 0.5] 5.01  .   .         ; Expressions work
    i 2     +  0.44 .               (     !             ; Various score preprocessors
    i 9     0  26   "beats.wav"     4.114               ; A string
    i $verb 32 6.2  0.28                                ; Deep comment

'''

import re
import sys

from optparse import OptionParser

from csd.sco import event
from csd.sco import element

def align(score, s=1, p=1, c=2, m=1, statements='fi'):
    '''Auto-aligns groupings of i-events.
    
    A grouping is a block of sequential events of the same statement
    type.
    
    '''
    
    score_list = score.splitlines(True)  # Each event is individually handled
    output = []                          # Collects events for the new score
    block = []                           # Collects groupings of events
    
    # Process each individual event
    for e in score_list:
        if event.get(e, 0) in list(statements):
            block.append(e)
        else:
            if block:
                b = ''.join(block)
                output.append(_align_block(b, s, p, c, m))
                block = []
            output.append(e)

    if block:
        b = ''.join(block)
        output.append(_align_block(b, s, p, c, m))
        
    return ''.join(output)

def _align_block(block, s=1, p=1, c=2, m=1):
    # Split score block into individual events
    event_list = block.splitlines()

    # Get the number of columns in block
    n_columns = max(event.number_of_pfields(e) for e in event_list)

    # Initialize pfield lengths with zeros
    pf_lengths = [0] * n_columns

    # Get the longest pfield lengths for each column
    for row in event_list:
        for i, col in enumerate(event.get_pfield_list(row)):
            pf_lengths[i] = max(len(col), pf_lengths[i])
        
    # Align pfields, without trailing comments
    align_pfields = []
    for e in event_list:
        line = []
        
        # Append score statement with whitespace determined by s
        line.append(event.get(e, 0).ljust(s + 1))
        
        # Appened each pfield with whitespace determined by p and m
        for i, L in enumerate(pf_lengths[1:event.number_of_pfields(e)]):
            line.append(event.get(e, i + 1).ljust(max(L, m)))
            line.append(''.ljust(p))
            
        # Strip end of any potential whitespace
        align_pfields.append(''.join(line).rstrip(' '))

    # Add trailing comments
    align_comments = []
    longest_event = max(len(e) for e in align_pfields)

    for i, e in enumerate(event_list):
        line = []
        line.append(''.join(align_pfields[i]))

        # Add whitespace and comment if comment exists
        if event.get_trailing_comment(e):
            line.append(''.ljust(longest_event - len(align_pfields[i])))
            line.append(''.ljust(c))
            line.append(event.get_trailing_comment(e))

        align_comments.append(''.join(line))

    return '\n'.join(align_comments) + '\n'

        
if __name__ == '__main__':
    # Get command-line flags
    u = ['usage: <stdout> |']
    u.append('python align.py [-spcmt]")')
    usage = ' '.join(u)
    parser = OptionParser(usage)
    parser.add_option('-s', dest='statement', help='statement padding',
                      default=1)
    parser.add_option('-p', dest='pfield', help='pfield padding',
                      default=1)
    parser.add_option('-c', dest='comment', help='comment padding',
                      default=2)
    parser.add_option('-m', dest='minimum', help='minimum pfield width',
                      default=1)
    parser.add_option('-t', dest='statement_types', help='statement_types',
                      default='fi')
    (o, args) = parser.parse_args()

    # Get stdin
    stdin = sys.stdin.readlines()  # stdin
    score = ''.join(stdin)

    # Sanitize input
    o.statement = int(o.statement)
    o.pfield = int(o.pfield)
    o.comment = int(o.comment)
    o.minimum = int(o.minimum)
    o.statement_types = str(o.statement_types)
    
    print align(score, o.statement, o.pfield, o.comment, o.minimum,
                o.statement_types),


