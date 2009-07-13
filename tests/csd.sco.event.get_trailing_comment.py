#!/usr/bin/env python
'''Tests for get_trailing_comment'''

import sys
sys.path.append('../')
from csd.sco import event as s

def test(n, e, expect):
    result = s.get_trailing_comment(e)
    did_pass = result == expect

    return did_pass, n, 'get_trailing_comment', str(expect), str(result)

print test(0, 'i 1 0 440', '')
print test(1, 'i 1 0 440 ; comment', '; comment')
print test(2, 'i 1 0 440; comment', '; comment')
print test(3, 'i 1 0 440 /* comment */', '/* comment */')
print test(4, 'i 1 0 440 /* comment */ ', '/* comment */')
print test(5, 'i 1 0 440 /* c1 */ /* c2 */', '/* c1 */ /* c2 */')
print test(6, 'i 1 0 440/* c1 */ /* c2 */', '/* c1 */ /* c2 */')
print test(7, 'i 1 0 440 /* c1 */ ; c2', '/* c1 */ ; c2')
print test(8, 'i 1 0 440 /* c1 */ ; c2 ', '/* c1 */ ; c2')

