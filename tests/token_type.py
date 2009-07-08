#!/usr/bin/env python
'''Tests for token_type()'''

import sys
sys.path.append('../')
from csd.sco import event as s

def test(n, line, expect):
    result = s.token_type(line)
    did_pass = result == expect

    return did_pass, n, 'token_type()', str(expect), str(result)
    
print test(0, 'i', s.STATEMENT)
print test(1, '440', s.NUMERIC)
print test(2, '"foo"', s.STRING)
print test(3, '[~]', s.EXPRESSION)
print test(4, '$foo', s.MACRO)
print test(5, '.', s.CARRY)
print test(6, '!', s.NO_CARRY)
print test(7, 'np4', s.NEXT_PFIELD)
print test(8, 'pp4', s.PREVIOUS_PFIELD)
print test(9, '<', s.RAMP)
print test(10, '(', s.EXPONENTIAL_RAMP)
print test(11, ')', s.EXPONENTIAL_RAMP)
print test(12, '~', s.RANDOM)
print test(13, '+', s.CARRY_PLUS)
print test(14, '^+1', s.CARRY_PLUS)
print test(15, '^-1', s.CARRY_PLUS)


