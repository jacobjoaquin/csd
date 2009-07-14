#!/usr/bin/env python
'''Sets space between a statement and the first active element.

.. program:: s_spacer
.. cmdoption:: -s  Whitespace amount between statement and identifier

Example::
    
    $ cat s_spacer.sco | ./s_spacer.py
    
Before::
    
    i1 0 0.25 0.5 7.00
    i1 + .    0.5 7.00
    i1 + .    0.5 8.00
    i1 + .    0.5 8.00
    i1 + .    0.6 7.06
    i1 + .    0.6 7.06
    i1 + .    0.6 6.06
    i1 + .    0.6 6.06
    i1 + .    0.6 7.00
    i1 + .    0.6 7.00

After::
    
    i 1 0 0.25 0.5 7.00
    i 1 + .    0.5 7.00
    i 1 + .    0.5 8.00
    i 1 + .    0.5 8.00
    i 1 + .    0.6 7.06
    i 1 + .    0.6 7.06
    i 1 + .    0.6 6.06
    i 1 + .    0.6 6.06
    i 1 + .    0.6 7.00
    i 1 + .    0.6 7.00

'''

import re
import sys

sys.path.append('../')  # Fix this.
from csd.sco import event
from csd.sco import element

from optparse import OptionParser
    
if __name__ == '__main__':
    # Get command-line flags
    u = ['usage: <stdout> |']
    u.append('python s_spacer.py -s[pad amount]')
    usage = ' '.join(u)
    parser = OptionParser(usage)
    parser.add_option("-s", default=1, dest='spacer', help='spacer')
    (options, args) = parser.parse_args()

    options.spacer = int(options.spacer)  # Flag option needs to be an int
    stdin = sys.stdin.readlines()         # Get data from stdin
    sco = []                              # New score lines as list items

    for e in stdin:
        sco.append(event.statement_spacer(e, options.spacer))

    print ''.join(sco),

