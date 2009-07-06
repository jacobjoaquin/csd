#!/usr/bin/env python
'''Tests for remove()'''

import sys
sys.path.append('../')
import score as s

def test(n, event, pfield, expect):
    result = s.remove(event, pfield)
    did_pass = result == expect

    return did_pass, n, 'remove()', str(expect), str(result)

print test(0, 'i 0 1', 2, ('i 0 ', '1'))
print test(1, 'i 0 1; comment', 2, ('i 0 ; comment', '1'))
print test(2, 'i 0 /*asdf*/1; comment', 2, ('i 0 /*asdf*/; comment', '1'))
print test(3, 'i 0 1', 3, ('i 0 1', ''))
print test(4, '', 0, ('', ''))
print test(5, 'i 0 1.0 440', 2, ('i 0  440', '1.0'))


