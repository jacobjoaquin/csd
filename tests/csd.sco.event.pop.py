#!/usr/bin/env python
'''Tests for pop()'''

import sys
sys.path.append('../')
from csd.sco import event as s

def test(n, event, expect):
    result = s.pop(event)
    did_pass = result == expect

    return did_pass, n, 'pop()', str(expect), str(result)

print test(0, 'i 0 1', ('i 0 ', '1'))
print test(1, 'i 1 0/*foo*/4 0.5 440;comment', ('i 1 0/*foo*/4 0.5 ;comment', '440'))
print test(2, 'i 1 0 4 0.5 440', ('i 1 0 4 0.5 ', '440'))

print test(3, 'i 1 0/*foo*/4 0.5 440 ;comment', ('i 1 0/*foo*/4 0.5  ;comment', '440'))
print test(4, 'i 1 0 /*foo*/ 4 0.5 440 ;comment', ('i 1 0 /*foo*/ 4 0.5  ;comment', '440'))

