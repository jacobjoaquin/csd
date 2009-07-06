#!/usr/bin/env python
'''Tests for push()'''

import sys
sys.path.append('../')
import score as s

def test(n, event, fill, expect):
    result = s.push(event, fill)
    did_pass = result == expect

    return did_pass, n, 'push()', str(expect), str(result)

print test(0, 'i', '.', 'i .')
print test(1, 'i 1', '[~]', 'i 1 [~]')
print test(2, 'i1', '[~]', 'i1 [~]')
print test(3, 'i1; comment', '[~]', 'i1 [~]; comment')
print test(4, 'i1/*foo*/', '[~]', 'i1 [~]/*foo*/')


