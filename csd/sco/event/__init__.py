#!/usr/bin/env python

'''This module is designed to parse Csound score events.

* An *element* refers to pfield data, a comment, a continuous block of
  whitespace.

* An *event* is a score event. For example, ``i 1 0 4 1.0 440  ; A440``
  is an event.

* A *statement* is the type of Csound o an ``f`` is a function table event.

* An *identifier* is the unique name of index that indicates a specific
  instrument or f-table, and immediately proceeds a *statement*. For
  example, ``33`` is the identifier in ``i 33 0 11``.
  
Many of the following methods utilize the python interpretor to
demonstrate input and output. For each of these, assume the following
import statement has been called::
    
    >>> from csd.sco import event

'''

import re
from .. import element

def get(event, pfield):
    '''Returns a pfield element for an event.
    
    The pfield maybe a number, string, expression, or a statement.
    Comments are right out.
    
    Example::

        >>> event.get('i 1 0 4 1.0 440  ; A440', 5)
        '440'
    '''

    event = sanitize(event)
    event_list = split(event)

    if pfield in range(len(event_list)):
        value = event_list[pfield]
    else:
        value = None

    return value

def get_pfield_list(event):
    '''Returns a list of all the pfield elements in a list.
    
    Example::
        
        >>> event.get_pfield_list('i 1 0 4 1.0 440  ; A440')
        ['i', '1', '0', '4', '1.0', '440']
    '''
    event = sanitize(event)
    return split(event)    

def insert(event, pfield, fill='.'):
    '''Returns a new event with an inserted pfield element.
    
    Example::
        
        >>> event.insert('i 1 0 4 1.0 440  ; A440', 5, '1138')
        'i 1 0 4 1.0 1138 440  ; A440'
    
    .. note:: The parameter fill must be a string. Future versions
        will automatically re-type numbers to strings.
    '''
    
    if pfield in range(number_of_pfields(event)):
        pf = get(event, pfield)
        new = [fill, ' ', pf]
        event = set(event, pfield, ''.join(new))  
    elif pfield == number_of_pfields(event):
        pf = get(event, pfield - 1)
        new = [pf, ' ', fill]
        event = set(event, pfield - 1, ''.join(new))  
    
    return event

def number_of_pfields(event):
    '''Returns an integer of the amounts of pfield elements in an
    event.
    
    The statement (pfield 0) is also counted.  Comments and whitespace
    are omitted from the tally.

    Example::

        >>> event.number_of_pfields('i 1 0 4 1.0 440  ; A440')
        6
    '''
    
    return len(get_pfield_list(event))

def pop(event):
    '''Removes the last pfield element from an event and returns a
    tuple containing a new event and the removed element.

    This function preserves whitespace.    

    Example::
        
        >>> event.pop('i 1 0 4 1.0 440  ; A440')
        ('i 1 0 4 1.0   ; A440', '440')
    '''
    
    return remove(event, number_of_pfields(event) - 1)

def push(event, fill='.'):
    '''Appends a pfield element to the last pfield and returns the new
    event.
    
    Example::

        >>> event.push('i 1 0 4 1.0 440  ; A440', '1138')
        'i 1 0 4 1.0 440 1138  ; A440'
    '''

    return insert(event, number_of_pfields(event), fill)

def remove(event, pfield):
    '''Removes a pfield and returns a tuple containing the new event
    and the removed element.

    This function preserves whitespace.    

    Example::
        
        >>> event.remove('i 1 0 4 1.0 440  ; A440', 4)
        ('i 1 0 4  440  ; A440', '1.0')
    '''
    
    pf = ''
    
    if pfield in range(number_of_pfields(event)):
        pf = get(event, pfield)
        event = set(event, pfield, '')
    
    return event, pf
    
def sanitize(event):
    '''Returns a copy of the score event with extra whitespace and
    comments removed::
    
        >>> event.sanitize('i 1 0 4    1.0 440  ; A440')
        'i 1 0 4 1.0 440'
        
    .. note:: A statement and identifier will stay conjoined if there
        is no whitespace between them. This will most likey not be the
        case in the future.
    '''

    # Remove comments
    p = re.compile('\;.*|\/\*.*?\*\/')
    m = p.search(event)
    
    if m:
        event = p.sub(' ', event)
    
    event = event.strip()

    # Compress whitespace between fields
    p = re.compile('(\".+?\"|\{\{.+?\}\}|\[.+?\]|\S+)')
    event = ' '.join(p.findall(event))

    return event

def set(event, pfield, value):
    '''Returns a new event string with the specified pfield set with
    a new element.
    
    Example::
        
        >>> event.set('i 1 0 4 1.0 440  ; A440', 5, 1138)
        'i 1 0 4 1.0 1138  ; A440'
    '''

    # Ensure pfield type is number, as string versions do seep in.
    pfield = int(pfield)
    
    # Skip if pfield is out of range
    if pfield not in range(number_of_pfields(event)):
        return event
    
    tokens = tokenize(event)
    
    valid_pfields = [element.NUMERIC, element.MACRO, element.EXPRESSION,
                     element.STRING, element.CARRY, element.RAMP,
                     element.EXPONENTIAL_RAMP, element.RANDOM,
                     element.CARRY_PLUS, element.NO_CARRY, element.NEXT_PFIELD,
                     element.PREVIOUS_PFIELD]
    
    pf_index = -1
    for i, t in enumerate(tokens):
        if pf_index == -1:
            if element.token_type(t) == element.STATEMENT:
                pf_index += 1
        else:
            if element.token_type(t) in valid_pfields:
                pf_index += 1

        if pf_index == pfield:
            
            # Create test case for str(value)
            tokens[i] = str(value)
            break

    return ''.join(tokens)

def split(event):
    '''Returns a list that includes all event pfield and comments
    elements.

    Example::
        
        >>> event.split('i 1 0 4 1.0 440  ; A440')
        ['i', '1', '0', '4', '1.0', '440', '; A440']
    '''

    # Separate statement from p1 if necessary.
    p = re.compile('([abefimnqrstvx])\S')
    m = p.match(event)

    if m:
        event = event.replace(m.group(1), m.group(1) + ' ', 1)
    
    # Pattern for pfields
    pattern = '''(\".+?\"     |
                  \{\{.+?\}\} |
                  \[.+?\]     |
                  \;.*        |
                  \/\*.*?\*\/ |
                  \S+(?=\/\*) |
                  \S+(?=;)    |
                  \S+)
                  '''
                  
    p = re.compile(pattern, re.VERBOSE)

    return p.findall(event)

def swap(event, pfield_a, pfield_b):
    '''Returns a new event string after swapping two pfield elements.
    
    Example::
        
        >>> event.swap('i 1 0 4 1.0 440 ; A440', 4, 5)
        'i 1 0 4 440 1.0 ; A440'
    '''

    a = get(event, pfield_a)
    b = get(event, pfield_b)

    event = set(event, pfield_a, b)
    event = set(event, pfield_b, a)

    return event

def tokenize(event):
    '''Returns a list of all elements in an event.
    
    Elements include pfield data, comments and whitespace.

    Example::
        
        >>> event.tokenize('i 1 0 4 1.0 440  ; A440')
        ['i', ' ', '1', ' ', '0', ' ', '4', ' ', '1.0', ' ', '440', '  ', '; A440']
    
    .. note:: This function will attempt to tokenize invalid elements.
        Be sure that the event you provide is syntactically correct.
    '''
    
    tokens = []

    # Get leading whitespace and /* comments */
    p = re.compile('\s+|\/\*.+?\*\/')
    
    while p.match(event):
        m = p.match(event)
        tokens.append(m.group())
        event = p.sub('', event, 1)
        
    # Get statement
    m = element.RE_STATEMENT.match(event)
    
    if m:
        tokens.append(m.group())
        event = element.RE_STATEMENT.sub('', event, 1)
        
    # Token the rest of the event
    pattern = '''(\s+         |
                  \".+?\"     |
                  \{\{.+?\}\} |
                  \[.+?\]     |
                  \;.*        |
                  \/\*.*?\*\/ |
                  \S+(?=\/\*) |
                  \S+(?=;)    |
                  \S+)
                  '''
    
    p = re.compile(pattern, re.VERBOSE)
    
    for t in p.findall(event):
        tokens.append(t)
    
    return tokens

