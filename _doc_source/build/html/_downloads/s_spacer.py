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

def pad(event_, pad):
    elements = event.tokenize(event_)
    statement_index = None
    identifier_index = None
    statement_found = False

    # Get index for the statement and identifier    
    for i, e in enumerate(elements):
        if not statement_found:
            if element.token_type(e) == element.STATEMENT:
                statement_index = i
                statement_found = True
        else:
            if element.token_type(e) in [element.NUMERIC, element.MACRO,
                                         element.STRING]:
                identifier_index = i
                break

    # If no statement or identifier exists, return unaltered event_
    if None in [statement_index, identifier_index]:
        return event_
    
    # Create a new list of elements, replacing any potential whitespace or
    # comments that exists between the statement and the identifier
    new_elements = []

    # Append all elements through the statement    
    for i in range(0, statement_index + 1):
        new_elements.append(elements[i])
        
    # Append whitespace
    new_elements.append(' ' * pad)
    
    # Append everything between the identifier and the end of the event_
    for i in range(identifier_index, len(elements)):
        new_elements.append(elements[i])
        
    return ''.join(new_elements)
    
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

    for event_ in stdin:
        sco.append(pad(event_, options.spacer))

    print ''.join(sco),

