#!/usr/bin/env python
'''Tests tokenize_event()'''

import sys
sys.path.append('../')
import score as s

def test(n, line, expect):
    result = s.tokenize_event(line)
    did_pass = result == expect

    return did_pass, n, 'token_type()', str(expect), str(result)

print test(0, '', [])
print test(1, ' ', [' '])
print test(2, '  ', ['  '])
print test(3, 'i', ['i'])
print test(4, 'f', ['f'])
print test(5, 'i 0', ['i', ' ', '0'])
print test(6, '  i 0', ['  ', 'i', ' ', '0'])
print test(7, '  i  0 3', ['  ', 'i', '  ', '0', ' ', '3'])
print test(8, 'i 0 3 ; my comment', ['i', ' ', '0', ' ', '3', ' ',
              '; my comment'])
print test(9, 'i 0 3 /* my comment */', ['i', ' ', '0', ' ', '3', ' ',
              '/* my comment */'])
print test(10, 'i 0 3 /* my comment */ ', ['i', ' ', '0', ' ', '3', ' ',
              '/* my comment */', ' '])
print test(11, 'i 0 3 ; my comment ', ['i', ' ', '0', ' ', '3', ' ',
              '; my comment '])
print test(12, '/* my comment */i  0 3', ['/* my comment */', 'i', '  ', '0',
               ' ', '3'])
print test(13, 'i/* my comment */ 0 3', ['i', '/* my comment */', ' ', '0',
               ' ', '3'])
print test(14, 'i/* my comment */0 3', ['i', '/* my comment */', '0', ' ',
               '3'])
print test(15, 'i/* my comment */0/*foo*/3', ['i', '/* my comment */', '0',
               '/*foo*/', '3'])
print test(16, 'i1 0', ['i', '1', ' ', '0'])
print test(17, ' /*a*/ /*b*/i 1 0', [' ', '/*a*/', ' ', '/*b*/', 'i', ' ', '1',
               ' ', '0'])
print test(18, ' /*a*/ /*b*/i1 0', [' ', '/*a*/', ' ', '/*b*/', 'i', '1', ' ',
               '0'])
print test(19, 'i 0 3; my comment', ['i', ' ', '0', ' ', '3', '; my comment'])

print test(20, 'i [~] 0 [~]', ['i', ' ', '[~]', ' ', '0', ' ', '[~]'])
print test(21, 'i {{foo}} 0 {{bar}}', ['i', ' ', '{{foo}}', ' ', '0', ' ',
                '{{bar}}'])
print test(22, 'i "foo" 0 "foo"', ['i', ' ', '"foo"', ' ', '0', ' ', '"foo"'])


