#!/usr/bin/env python
'''Tests for map_()'''

import sys
sys.path.append('../')
from csd import sco

def test(n, expect, score, pattern, pfield_index, pf_function, *args):
    result = sco.map_(score, pattern, pfield_index, pf_function, *args)
    did_pass = result == expect

    return did_pass, n, 'map_()', str(expect), str(result)

def do_nothing(x): return x
print test(0, 'i 1', 'i 1', {}, 1, do_nothing)
print test(1, 'i 1', 'i 1', {0: 'i'}, 1, do_nothing)

def add_one(x): return x + 1
print test(2, 'i 1', 'i 1', {}, 1, add_one)
print test(3, 'i 2', 'i 1', {0: 'i'}, 1, add_one)
print test(4, 'i 2\ni 3', 'i 1\ni 2', {0: 'i'}, 1, add_one)
print test(5, 'i 2\ni 2', 'i 1\ni 2', {0: 'i', 1: 1}, 1, add_one)
print test(6, 'i 1\ni 3', 'i 1\ni 2', {0: 'i', 1: 2}, 1, add_one)
print test(7, 'i 2 2\ni 2 2', 'i 1 1\ni 1 1', {0: 'i'}, [1, 2], add_one)

def multiply(x, y): return x * y
print test(8, 'i 3.1459', 'i 1', {0: 'i'}, 1, multiply, 3.1459)


