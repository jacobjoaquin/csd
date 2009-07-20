#!/usr/bin/env python
'''Tests for replace()'''

import sys
sys.path.append('../')
from csd.sco import selection

def test(n, expect, score_dict, pfield, pgenerator, *args):
    result = selection.replace(score_dict, pfield, pgenerator, *args)
    did_pass = result == expect

    return did_pass, n, 'replace()', str(expect), str(result)

def one(): return 1
print test(0, {0: 'i 1'}, {0: 'i 1'}, 1, one)
print test(1, {0: 'i 1'}, {0: 'i 2'}, 1, one)

def macro(): return '$macro'
print test(0, {0: 'i 1'}, {0: 'i 1'}, 1, one)
print test(1, {0: 'i $macro'}, {0: 'i 1'}, 1, macro)


