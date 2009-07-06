#!/usr/bin/env python
'''This module is designed to parse Csound score events.

An *element* refers to pfield data, a comment, a continuous block of
whitespace.

An *event* is a score event. For example, ``i 1 0 4 1.0 440  ; A440``
is an event.

A *statement* is the type of Csound of event. For example, an ``i`` is
an instrument event (i-event) while an ``f`` is a function table event.

An *identifier* is the unique name of index that indicates a specific
instrument or f-table, and immediately proceeds a *statement*. For
example, ``33`` is the identifier in ``i 33 0 11``.
'''

import re

RE_STATEMENT = re.compile('[abefimnqrstvx]')
RE_NUMERIC = re.compile('\d+.\d+|\d+.|.\d+|\d+')
RE_STRING = re.compile('\".+?\"|\{\{.+?\}\}')
RE_EXPRESSION = re.compile('\[.+?\]')
RE_MACRO = re.compile('\$\S+')
RE_CARRY = re.compile('\.')
RE_NO_CARRY = re.compile('\!')
RE_NEXT_PFIELD = re.compile('np\d+')
RE_PREVIOUS_PFIELD = re.compile('pp\d+')
RE_RAMP = re.compile('\<')
RE_EXPONENTIAL_RAMP = re.compile('[\(\)]')
RE_RANDOM = re.compile('\~')
RE_CARRY_PLUS = re.compile('\+|\^\+\d+|\^\-\d+')

# Class this?
STATEMENT = 1
NUMERIC = 2
STRING = 3
EXPRESSION = 4
MACRO = 5
CARRY = 6
NO_CARRY = 7
NEXT_PFIELD = 8
PREVIOUS_PFIELD = 9
RAMP = 10
EXPONENTIAL_RAMP = 11
RANDOM = 12
CARRY_PLUS = 13

def get(event, pfield):
    '''Returns a pfield element for an event.
    
    The pfield maybe a number, string, expression, or a statement.
    Comments are right out.
    
    Example::
        
        >>> score.get('i 1 0 4 1.0 440  ; A440', 5)
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
        
        >>> score.get_pfield_list('i 1 0 4 1.0 440  ; A440')
        ['i', '1', '0', '4', '1.0', '440']
    '''

    event = sanitize(event)
    return split(event)    

def insert(event, pfield, fill='.'):
    '''Returns a new event with an inserted pfield element.
    
    Example::
        
        >>> score.insert('i 1 0 4 1.0 440  ; A440', 5, '1138')
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

        >>> score.number_of_pfields('i 1 0 4 1.0 440  ; A440')
        6
    '''
    
    return len(get_pfield_list(event))

def pop(event):
    '''Removes the last pfield element from an event and returns a
    tuple containing a new event and the removed element.

    This function preserves whitespace.    

    Example::
        
        >>> score.pop('i 1 0 4 1.0 440  ; A440')
        ('i 1 0 4 1.0   ; A440', '440')
    '''
    
    return remove(event, number_of_pfields(event) - 1)

def push(event, fill='.'):
    '''Appends a pfield element to the last pfield and returns the new
    event.
    
    Example::

        >>> score.push('i 1 0 4 1.0 440  ; A440', '1138')
        'i 1 0 4 1.0 440 1138  ; A440'
    '''

    return insert(event, number_of_pfields(event), fill)

def remove(event, pfield):
    '''Removes a pfield and returns a tuple containing the new event
    and the removed element.

    This function preserves whitespace.    

    Example::
        
        >>> score.remove('i 1 0 4 1.0 440  ; A440', 4)
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
    
        >>> score.sanitize('i 1 0 4    1.0 440  ; A440')
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
        
        >>> score.set('i 1 0 4 1.0 440  ; A440', 5, 1138)
        'i 1 0 4 1.0 1138  ; A440'
    '''

    # Ensure pfield type is number, as string versions do seep in.
    pfield = int(pfield)
    
    # Skip if pfield is out of range
    if pfield not in range(number_of_pfields(event)):
        '%%% set not in range'
        return event
    
    tokens = tokenize(event)
    
    pf_index = -1
    for i, t in enumerate(tokens):
        if pf_index == -1:
            if token_type(t) == STATEMENT:
                pf_index += 1
        else:
            if token_type(t) in [NUMERIC, MACRO, EXPRESSION, STRING, CARRY,
                                 RAMP, EXPONENTIAL_RAMP, RANDOM, CARRY_PLUS,
                                 NO_CARRY, NEXT_PFIELD, PREVIOUS_PFIELD]:
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
        
        >>> score.split('i 1 0 4 1.0 440  ; A440')
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

def swap_columns(score, statement, identifier, a, b):
    '''Exchanges all score columns for a specified statement and
    identifier.
    
    DEPRECATED
    '''
    
    score_output = []
    score_list = score.splitlines(True)
    
    for row in score_list:
        # Test statement type and statement identifier.
        if get(row, 0) is statement\
                and get(row, 1) == str(identifier):
                    
            # Check that pfields a and b are in range, return original if True.
            for pf in (a, b):
                if pf not in range(number_of_pfields(row)):
                    return score
                    
            # Swap pfields
            score_output.append(swap(row, a, b))
        else:
            score_output.append(row)
            
    return ''.join(score_output)
    
def swap(event, pfield_a, pfield_b):
    '''Returns a new event string after swapping two pfield elements.
    
    Example::
        
        >>> score.swap('i 1 0 4 1.0 440 ; A440', 4, 5)
        'i 1 0 4 440 1.0 ; A440'
    '''

    a = get(event, pfield_a)
    b = get(event, pfield_b)

    event = set(event, pfield_a, b)
    event = set(event, pfield_b, a)

    return event

def token_type(element):
    '''Returns the Csound score token type of an element.
        
    Example::
        
        >>> score.token_type('[~ * 440 + 440]') == score.EXPRESSION
        True
        >>> score.token_type('i') == score.EXPRESSION
        False
    
    .. note:: The mechanisms handling tokens will change in the
        future. For the mean time, tokens are treated as faux-
        enums, and should be compared directly with the token
        constants.
    '''

    type_ = None

    if RE_NEXT_PFIELD.match(element):
        type_ = NEXT_PFIELD
    elif RE_PREVIOUS_PFIELD.match(element):
        type_ = PREVIOUS_PFIELD
    elif RE_STATEMENT.match(element):
        type_ = STATEMENT
    elif RE_NUMERIC.match(element):
        type_ = NUMERIC
    elif RE_STRING.match(element):
        type_ = STRING
    elif RE_EXPRESSION.match(element):
        type_ = EXPRESSION
    elif RE_MACRO.match(element):
        type_ = MACRO
    elif RE_CARRY.match(element):
        type_ = CARRY
    elif RE_NO_CARRY.match(element):
        type_ = NO_CARRY
    elif RE_RAMP.match(element):
        type_ = RAMP
    elif RE_EXPONENTIAL_RAMP.match(element):
        type_ = EXPONENTIAL_RAMP
    elif RE_RANDOM.match(element):
        type_ = RANDOM
    elif RE_CARRY_PLUS.match(element):
        type_ = CARRY_PLUS
    else:
        type_ = None

    return type_            

def tokenize(event):
    '''Returns a list of all elements in an event.
    
    Elements include pfield data, comments and whitespace.

    Example::
        
        >>> score.tokenize('i 1 0 4 1.0 440  ; A440')
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
    m = RE_STATEMENT.match(event)
    
    if m:
        tokens.append(m.group())
        event = RE_STATEMENT.sub('', event, 1)
        
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

