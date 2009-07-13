#!/usr/bin/env python
'''Tests for statement_spacer'''

import sys
sys.path.append('../')
from csd.sco import event

def test(n, e, s, expect):
    result = event.statement_spacer(e, spacer=s)
    did_pass = result == expect

    return did_pass, n, 'statement_spacer', str(expect), str(result)

print test(0, 'i', 0, 'i')
print test(1, 'i', 1, 'i')
print test(2, 'i1', 0, 'i1')
print test(3, 'i1', 1, 'i 1')
print test(4, 'i1', 2, 'i  1')
print test(5, 'i1 1 0 440', 2, 'i  1 1 0 440')
print test(6, '  i1 1 0 440', 2, '  i  1 1 0 440')
print test(7, 'i 1', 1, 'i 1')
print test(8, 'i    1', 1, 'i 1')
print test(9, 'i1', 4, 'i    1')
print test(10, 'i/*c*/1', 0, 'i/*c*/1')
print test(11, 'i/*c*/1', 1, 'i /*c*/1')
print test(12, ' i/*c*/1', 1, ' i /*c*/1')

