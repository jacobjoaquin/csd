#!/usr/bin/env python
'''Tests for split_event()'''

import sys
sys.path.append('../')
import score as s

def test(n, line, expect):
    result = s.split_event(line)
    did_pass = result == expect

    return did_pass, n, 'split_event()', str(expect), str(result)

print test(0, '', [])
print test(1, 'i', ['i'])
print test(2, ' i', ['i'])
print test(3, 'i 1', ['i', '1'])
print test(4, 'i1', ['i', '1'])
print test(5, 'i"instrname"', ['i', '"instrname"'])
print test(6, 'i "instrname"', ['i', '"instrname"'])
print test(7, 'i$macro', ['i', '$macro'])
print test(8, 'i 0 1 440 6.666', ['i', '0', '1', '440', '6.666'])
print test(9, '   i    0  1   440  6.666   ', ['i', '0', '1', '440', '6.666'])
print test(10, 'i 0 1 440 6.666  ; comment', ['i', '0', '1', '440', '6.666',
               '; comment'])
print test(11, 'i 0 1 440 6.666  /* my comment */', ['i', '0', '1', '440',
               '6.666', '/* my comment */'])
print test(12, 'i 0 1 /*foo*/ 440 6.666  /* my comment */', ['i', '0', '1',
               '/*foo*/', '440', '6.666', '/* my comment */'])
print test(13, 'i 0 1/*foo*/ 1 /* my comment */', ['i', '0', '1', '/*foo*/',
               '1', '/* my comment */'])

print test(14, 'i 0 1/*foo*/1 /* my comment */', ['i', '0', '1', '/*foo*/',
               '1', '/* my comment */'])
print test(15, 'i 0 1 /* my comment */1 /* my comment */', ['i', '0', '1',
               '/* my comment */', '1', '/* my comment */'])
print test(16, 'i {{ }} 1', ['i', '{{ }}', '1'])               
print test(17, 'i {{  }} 1', ['i', '{{  }}', '1'])               
print test(18, 'i "  " 1', ['i', '"  "', '1'])               
print test(19, 'i 0 3; my comment', ['i', '0', '3', '; my comment'])
print test(20, 'f 0 3; my comment', ['f', '0', '3', '; my comment'])
print test(21, 'f0 3; my comment', ['f', '0', '3', '; my comment'])
# z is a non-statement
print test(22, 'z0 3; my comment', ['z0', '3', '; my comment'])  


