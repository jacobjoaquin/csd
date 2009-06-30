#!/usr/bin/env python
'''Tests for swap_pfields()'''

import sys
sys.path.append('../')
import score as s

def test(n, line, a, b, expect):
    result = s.swap_pfields(line, a, b)
    did_pass = result == expect

    return did_pass, n, 'swap_pfields()', str(expect), str(result)

print test(0, 'i 0 1', 1, 2, 'i 1 0')
print test(0, 'i 0 1 [~ * 440 + 440] $macro', 3, 4,
           'i 0 1 $macro [~ * 440 + 440]')

