#!/usr/bin/env python
'''Tests for sanitize()'''

import sys
sys.path.append('../')
from csd.sco import event as s

def test(n, line, expect):
    result = s.sanitize(line)
    did_pass = result == expect

    return did_pass, n, 'sanitize()', str(expect), str(result)

print test(0, 'i', 'i')
print test(1, ' i', 'i')
print test(2, ' i ', 'i')
print test(3, ' i \n', 'i')
print test(4, 'i 0 1', 'i 0 1')
print test(5, 'i 0 1 ; comment', 'i 0 1')
print test(6, 'i    0    1', 'i 0 1')
print test(7, 'i    0    [~ * 100 +   100] 2', 'i 0 [~ * 100 +   100] 2')
print test(8, 'i  $macro  0  1', 'i $macro 0 1')
print test(9, 'i  "named.instr"  0  1', 'i "named.instr" 0 1')
print test(10, 'i  " "  0  1', 'i " " 0 1')
print test(11, 'i  {{ }}  0  1', 'i {{ }} 0 1')
print test(12, 'i  {{   }}  0  1', 'i {{   }} 0 1')
print test(13, 'i  {{"   "}}  0  1', 'i {{"   "}} 0 1')
print test(14, 'i  "{{   }}"  0  1', 'i "{{   }}" 0 1')
print test(15, 'i 1 0 1 /* End comment */ ', 'i 1 0 1')
print test(16, '/* intro comment */ i 1 0 1 /* End comment */ ', 'i 1 0 1')
print test(17, '/* intro comment */ i 1/* middle */ 0 1 /* End comment */ ', 'i 1 0 1')
print test(18, 'i  [~]  0  [~]', 'i [~] 0 [~]')
print test(19, 'i  {{foo}}  0  {{foo }}', 'i {{foo}} 0 {{foo }}')
print test(20, 'i  "foo"  0  "foo "', 'i "foo" 0 "foo "')
print test(24, 'i 1 0/*foo*/4 0.5 440 ;comment', 'i 1 0 4 0.5 440')
print test(25, 'i /**/ 1', 'i 1')
print test(26, 'i 1;', 'i 1')







