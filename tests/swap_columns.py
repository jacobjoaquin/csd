#!/usr/bin/env python
'''Tests for swap_columns()'''

import sys
sys.path.append('../')
import score as s

def test(n, score, statement, identifier, a, b, expect):
    result = s.swap_columns(score, statement, identifier, a, b)
    did_pass = result == expect

    return did_pass, n, 'swap_columns()', str(expect), str(result)

print test(0, 'i 1 0 1 440 1.0', 'i', 1, 4, 5, 'i 1 0 1 1.0 440')

score = '''i 1 0 1 440 1.0
i 1 0 1 220 0.333'''
expect = '''i 1 0 1 1.0 440
i 1 0 1 0.333 220'''
print test(1, score, 'i', 1, 4, 5, expect)

score = '''i 1 0 1 440 1.0
i 2 0 1 220 0.333'''
expect = '''i 1 0 1 1.0 440
i 2 0 1 220 0.333'''
print test(2, score, 'i', 1, 4, 5, expect)

# Pfield out of range
score = '''i 1 0 1 440 1.0'''
expect = '''i 1 0 1 440 1.0'''
print test(3, score, 'i', 1, 4, 6, expect)

# Pfield out of range
score = '''i 1 0 1 440 1.0'''
expect = '''i 1 0 1 440 1.0'''
print test(4, score, 'i', 1, 4, -1, expect)

score = '''i 1 2 3 4 5 6'''
expect = '''i 1 6 3 4 5 2'''
print test(5, score, 'i', 1, 2, 6, expect)

score = '''i 1 2 $three 4 5 "six"'''
expect = '''i 1 2 "six" 4 5 $three'''
print test(6, score, 'i', 1, 3, 6, expect)

score = '''
i 1 0 1 440 1.0
f 1 0 8192 10 1 1 1 1'''
expect = '''
i 1 0 1 1.0 440
f 1 0 8192 10 1 1 1 1'''
print test(7, score, 'i', 1, 4, 5, expect)

score = '''
i 1 0 1 440 1.0
f 1 0 8192 10 1 1 1 1'''
expect = '''
i 1 0 1 440 1.0
f 1 0 8192 1 10 1 1 1'''
print test(8, score, 'f', 1, 4, 5, expect)

score = '''
i 1 0 1 440 1.0
f 1 0 8192 10 1 1 1 1'''
expect = '''
i 1 0 1 440 1.0
f 1 0 8192 1 10 1 1 1'''
print test(9, score, 'f', 1, 4, 5, expect)

score = '''i1 0 1 440 1.0'''
expect = '''i1 0 1 1.0 440'''
print test(10, score, 'i', 1, 4, 5, expect)


