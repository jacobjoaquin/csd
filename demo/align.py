#!/usr/bin/env python
'''Aligns groups of i-events.'''

import re
import sys
sys.path.append('../')  # Fix this.
from csd.sco import event
from csd.sco import element

def align_score(score, s=1, p=1, c=2, m=1, statements=['i']):
    '''Aligns groupings of events.'''

    score_list = score.splitlines(True)

    output = []
    block = []

    for e in score_list:
        if event.get(e, 0) in statements:
            block.append(e)
        else:
            if block:
                b = ''.join(block)
                output.append(align_block(b, s, p, c, m, statements))
                block = []
            output.append(e)

    if block:
        b = ''.join(block)
        output.append(align_block(b, s, p, c, m, statements))
        
    return ''.join(output)
        
def align_block(block, s=1, p=1, c=2, m=1, statements=['i']):
    block_list = block.splitlines()

    # Get the number of columns in block
    n_columns = max(event.number_of_pfields(e) for e in block_list)

    # Pad pfield lengths list with zeros
    pf_lengths = [0] * n_columns
    
    # Get the longest pfield lengths for each column
    event_pf_list = []
    for e in block_list:
        event_pf_list.append(event.get_pfield_list(e))    
    for e in event_pf_list:
        for i, pf in enumerate(e):
            pf_lengths[i] = max(len(pf), pf_lengths[i])

    # Align pfields
    pass_0 = []
    
    for e in block_list:
        line = []
        line.append('i')
        line.append(' ' * s)
        
        for i in range(1, event.number_of_pfields(e)):
            field_width = max(pf_lengths[i], m)
            line.append(event.get(e, i).ljust(field_width, ' '))
            line.append(''.ljust(p, ' '))
            
        pass_0.append(''.join(line).rstrip(' '))

    # Add trailing comments
    longest_event = max(len(e) for e in pass_0)

    pass_1 = []
    for i, e in enumerate(block_list):
        line = []
        line.append(''.join(pass_0[i]))
        comment = get_trailing_comment(e)

        # Add whitespace and comment if comment exists
        if comment:
            line.append(''.ljust(longest_event - len(pass_0[i]), ' '))
            line.append(''.ljust(c, ' '))
            line.append(comment)

        pass_1.append(''.join(line))

    return '\n'.join(pass_1) + '\n'

def get_trailing_comment(e):
    tokens = []
    tokens = event.tokenize(e)
    
    p = re.compile(';.*')
    m = p.match(tokens[-1])
    
    if m:
        return tokens[-1]
    else:
        return None
    
if __name__ == '__main__':
    # Get stdin
    stdin = sys.stdin.readlines()  # stdin
    score = ''.join(stdin)

    print align_score(score, 1, 1, 2, 4),
