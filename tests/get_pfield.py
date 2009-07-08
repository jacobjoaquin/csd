#!/usr/bin/env python
'''Tests for get()'''

import sys
sys.path.append('../')
from csd.sco import event as s

def test(n, line, pf, expect):
    result = s.get(line, pf)
    did_pass = result == expect

    return did_pass, n, 'get()', str(expect), str(result)

print test(0, 'i', 0, 'i')
print test(1, 'i 0', 0, 'i')
print test(2, 'i 0', 1, '0')
print test(3, 'i 0 1.337', 2, '1.337')
print test(4, 'i 0 1.337 5', 2, '1.337')
print test(5, 'i 0 1.337 5', 4, None)
print test(6, 'i 0 1 ; comment', 4, None)
print test(7, 'i 0 1 ; comment', -1, None)
print test(8, 'i 0 1 ; comment', 2, '1')
print test(9, 'i 0 /* foo bar */ 1 ; comment', 2, '1')

