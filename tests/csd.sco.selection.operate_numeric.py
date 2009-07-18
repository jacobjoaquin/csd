#!/usr/bin/env python
'''Tests for operate_numeric()'''

import sys
sys.path.append('../')
from csd.sco import selection

def test(n, expect, score_dict, pfield, pf_function, *args):
    result = selection.operate_numeric(score_dict, pfield, pf_function, *args)
    did_pass = result == expect

    return did_pass, n, 'operate_numeric()', str(expect), str(result)

def do_nothing(x): return x
print test(0, {0: 'i 1'}, {0: 'i 1'}, 1, do_nothing)

def add_one(x): return x + 1
print test(1, {0: 'i 2'}, {0: 'i 1'}, 1, add_one)
print test(2, {0: 'i 2.5'}, {0: 'i 1.5'}, 1, add_one)

def sum_all(x, *args): return x + (sum(args))
print test(3, {0: 'i 16'}, {0: 'i 1'}, 1, sum_all, 1, 2, 3, 4, 5)
print test(4, {0: 'i 16.5'}, {0: 'i 1.5'}, 1, sum_all, 1, 2, 3, 4, 5)
print test(5, {0: 'i 17.0'}, {0: 'i 1.5'}, 1, sum_all, 1, 2, 3, 4, 5.5)
print test(6, {0: 'i 1', 1: 'i 2'}, {0: 'i 0', 1: 'i 1'}, 1, sum_all, 1)
print test(7, {0: 'i 1', 1: 'i .'}, {0: 'i 0', 1: 'i .'}, 1, sum_all, 1)

def minus_one(x): return x - 1
print test(8, {0: 'i 0 8'}, {0: 'i 1 9'}, [1, 2], minus_one)
print test(9, {0: 'i 0 8', 1: 'i 2 3'}, {0: 'i 1 9', 1: 'i 3 4'}, [1, 2],
           minus_one)

