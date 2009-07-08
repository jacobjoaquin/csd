#!/usr/bin/env python
'''Sets space between a statement and the first active element.

.. program:: space_statement
.. cmdoption:: -p  Pad amount between statement and identifier

Example::
    
    $ cat unfactored.sco | ./space_statement.py -p0
    
Before::
    
    i 1 0 4    1.0 9.07
    i 2 0 0.25 0.3 7.00
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 2 + .    .   .
    i 1 0 4    1.0 9.11

After::
    
    i1 0 4    1.0 9.07
    i2 0 0.25 0.3 7.00
    i2 + .    .   .
    i2 + .    .   .
    i2 + .    .   .
    i2 + .    .   .
    i2 + .    .   .
    i2 + .    .   .
    i2 + .    .   .
    i2 + .    .   .
    i2 + .    .   .
    i1 0 4    1.0 9.11
'''

import re
import sys
sys.path.append('../')  # Fix this.
import csd.sco.event as event

from optparse import OptionParser

def pad(event_, pad):
    elements = event.tokenize(event_)
    statement_index = None
    identifier_index = None
    statement_found = False

    # Get index for the statement and identifier    
    for i, e in enumerate(elements):
        if not statement_found:
            if event.token_type(e) == event.STATEMENT:
                statement_index = i
                statement_found = True
        else:
            if event.token_type(e) in [event.NUMERIC, event.MACRO,
                                       event.STRING]:
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
    u.append('python arpeggiator.py -p(pad)')
    usage = ' '.join(u)
    parser = OptionParser(usage)
    parser.add_option("-p", default=1, dest='pad', help='pad')
    (options, args) = parser.parse_args()

    options.pad = int(options.pad)  # Flag option needs to be an int, not str
    stdin = sys.stdin.readlines()   # Get data from stdin
    sco = []                        # Stores each new score line as list items

    for event_ in stdin:
        sco.append(pad(event_, options.pad))

    print ''.join(sco)

