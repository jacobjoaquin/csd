#!/usr/bin/env python
'''Tests for merge()'''

import sys
sys.path.append('../')
from csd import sco

def test(n, score, score_dict, expect):
    result = sco.merge(score, score_dict)
    did_pass = result == expect

    return did_pass, n, 'merge()', str(expect), str(result)

print test(0, 'i', {0: 'f'}, 'f')
print test(1, 'i 1', {0: 'i 2'}, 'i 2')
print test(2, 'i 1\ni 2', {0: 'i 3'}, 'i 3\ni 2')
print test(3, 'i 1\ni 2\ni 3', {0: 'i 3', 2: 'i 1'}, 'i 3\ni 2\ni 1')
print test(4, 'i 1\ni 2\ni 3', {1: 'i 4\ni 5'}, 'i 1\ni 4\ni 5\ni 3')
print test(5, 'i\n ', {0: 'f'}, 'f\n ')
print test(6, 'i\n', {0: 'f'}, 'f\n')
print test(7, 'i 1', {0: ['i 2', 'i 3']}, 'i 2\ni 3')
print test(8, 'i 1', {0: ['i 2', 'i 3', '']}, 'i 2\ni 3\n')
print test(9, 'i 1\ni 4', {0: ['i 2', 'i 3', '']}, 'i 2\ni 3\n\ni 4')
print test(10, 'i 1\ni 4', {0: ['i 2', ['i 3', 'i 5'], 'i 6']},
            'i 2\ni 3\ni 5\ni 6\ni 4')
print test(11, 'i 1\ni 4', {0: ['i 2', ['i 3', '', '', 'i 5'], 'i 6']},
            'i 2\ni 3\n\n\ni 5\ni 6\ni 4')

