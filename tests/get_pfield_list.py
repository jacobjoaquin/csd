#!/usr/bin/env python
'''Tests for get_pfield_list()'''

import sys
sys.path.append('../')
from csd.sco import event as s

def test(n, line, expect):
    result = s.get_pfield_list(line)
    did_pass = result == expect

    return did_pass, n, 'get_pfield_list()', str(expect), str(result)

print test(0, 'i', ['i'])
print test(1, 'i 1', ['i', '1'])
print test(2, ' i  1 ', ['i', '1'])
print test(3, 'i1', ['i', '1'])
print test(4, 'i 1 + . $masterAmp 440.0 "wtf"', ['i', '1', '+', '.',
              '$masterAmp', '440.0', '"wtf"'])
print test(5, 'i 1 + . [~ * 100 + 100]', ['i', '1', '+', '.',
              '[~ * 100 + 100]'])
print test(6, '/* */ i 1', ['i', '1'])
print test(7, '/* */i 1', ['i', '1'])
print test(8, '/* */i1', ['i', '1'])
print test(9, '/* */  /*asdf*/i1', ['i', '1'])
print test(10, 'i/*asdf*/1', ['i', '1'])
print test(11, 'i1/*asdf*/', ['i', '1'])
print test(12, 'i1;comment', ['i', '1'])
print test(13, 'i  {{foo}}  0  {{foo }}', ['i', '{{foo}}', '0', '{{foo }}'])
print test(14, 'i  "foo"  0  "foo "', ['i', '"foo"', '0', '"foo "'])

