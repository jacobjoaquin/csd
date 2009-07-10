#!/usr/bin/env python
'''Tests for get_trailing_comment'''

import sys
sys.path.append('../')
from csd.sco import event as s

def test(n, line, pf, v, expect):
    result = s.set(e)
    did_pass = result == expect

    return did_pass, n, 'get_trailing_comment', str(expect), str(result)

print __file__, 'False'
