#!/usr/bin/env python
'''Tests for number_of_pfields()'''

import sys
sys.path.append('../')
import score as s

def test(n, line, expect):
    result = s.number_of_pfields(line)
    did_pass = result == expect

    return did_pass, n, 'token_type()', str(expect), str(result)

print test(0, 'i', 1)
print test(1, 'i\n', 1)
print test(2, 'i 1', 2)
print test(3, 'i1', 2)
print test(4, 'i1 0 1', 4)
print test(5, 'i1 + .', 4)
print test(6, 'i1 + . $freq', 5)
print test(7, 'i1 + . [~ * 100 + 100]', 5)
print test(8, 'i1 + . [~ * 100 + 100] 440', 6)
print test(9, 'i1 + . ; this is a comment', 4)
print test(10, 'i1 + . /* this is a comment */', 4)
print test(11, 'i1 + . /* this is a comment */ 5', 5)
print test(12, 'i$instr + .', 4)
print test(13, 'i"instr" + .', 4)
print test(14, "i'instr' + .", 4)
print test(15, 'i "instr" + .', 4)
print test(16, 'i {{instr}} + .', 4)
print test(17, 'i 1 0 .0', 4)
print test(18, 'i 1 0 0.', 4)
print test(19, 'i 1 0 0.', 4)
print test(20, 'i 1 0 0.', 4)
print test(21, 'i 1 0 $macro.with.dots.in.name', 4)
print test(22, 'i1 + . ; this is a comment 440 800', 4)
print test(23, 'i1 + . ; this is a "comment" 440 800', 4)
print test(24, 'i1 + . ; this is a [comment 440] 800', 4)
print test(25, 'i1 + . " " 1', 6)
print test(26, 'i1 + . {{ }} 1', 6)
print test(27, 'i1 + . {{" "}} 1', 6)
print test(28, 'i1 + . "{{ }}" 1', 6)


