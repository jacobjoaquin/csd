#!/usr/bin/env python
'''Tests for insert_pfield()'''

import sys
sys.path.append('../')
import score as s

def test(n, event, pfield, fill, expect):
    result = s.insert_pfield(event, pfield, fill)
    did_pass = result == expect

    return did_pass, n, 'insert_pfield()', str(expect), str(result)

print test(0, 'i', 0, '.', '. i')
print test(1, 'i', 1, '.', 'i .')
print test(2, 'i 0', 1, '.', 'i . 0')
print test(3, 'i 0', 2, '.', 'i 0 .')
print test(4, 'i 0', 1, '[~]', 'i [~] 0')
print test(5, 'i [~] 0 [~]', 1, '[~]', 'i [~] [~] 0 [~]')
print test(6, 'i {{foo}} 0 {{foo}}', 1, '{{foo}}',
              'i {{foo}} {{foo}} 0 {{foo}}')
print test(7, 'i "~" 0 "~"', 1, '"~"', 'i "~" "~" 0 "~"')
