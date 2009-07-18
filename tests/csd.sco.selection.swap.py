#!/usr/bin/env python
'''Tests for swap()'''

import sys
sys.path.append('../')
from csd.sco import selection

def test(n, score_dict, x, y, expect):
    result = selection.swap(score_dict, x, y)
    did_pass = result == expect

    return did_pass, n, 'swap()', str(expect), str(result)
    
print test(0, {0: 'i 1 2', 1: 'i 3 4'}, 1, 2, {0: 'i 2 1', 1: 'i 4 3'})
print test(1, {0: 'i 1 2', 1: 'i 3 4', 2: 'i 5 6'}, 1, 2, 
           {0: 'i 2 1', 1: 'i 4 3', 2: 'i 6 5'})
print test(2, {0: 'i 1 2', 1: 'i 3 4', 2: ''}, 1, 2,
           {0: 'i 2 1', 1: 'i 4 3', 2: ''})
print test(3, {0: 'i $a "b"', 1: 'i $c "d"'}, 1, 2,
           {0: 'i "b" $a', 1: 'i "d" $c'})
print test(4, {0: 'i 1 2 3', 1: 'i 4 5 6'}, 1, 3,
           {0: 'i 3 2 1', 1: 'i 6 5 4'})

