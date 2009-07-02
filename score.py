#!/usr/bin/env python

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

def token_type(t):
    '''Analyses the input and returns the t type of a Csound
    score.'''

    type_ = None

    if RE_NEXT_PFIELD.match(t):
        type_ = NEXT_PFIELD
    elif RE_PREVIOUS_PFIELD.match(t):
        type_ = PREVIOUS_PFIELD
    elif RE_STATEMENT.match(t):
        type_ = STATEMENT
    elif RE_NUMERIC.match(t):
        type_ = NUMERIC
    elif RE_STRING.match(t):
        type_ = STRING
    elif RE_EXPRESSION.match(t):
        type_ = EXPRESSION
    elif RE_MACRO.match(t):
        type_ = MACRO
    elif RE_CARRY.match(t):
        type_ = CARRY
    elif RE_NO_CARRY.match(t):
        type_ = NO_CARRY
    elif RE_RAMP.match(t):
        type_ = RAMP
    elif RE_EXPONENTIAL_RAMP.match(t):
        type_ = EXPONENTIAL_RAMP
    elif RE_RANDOM.match(t):
        type_ = RANDOM
    elif RE_CARRY_PLUS.match(t):
        type_ = CARRY_PLUS
    else:
        type_ = None

    return type_            

def sanitize_event(event):
    '''Removes everything unnecessary to a score event.
    
    Unnecessary includes extra white space and comments.
    '''

    # Remove comments
    p = re.compile('\;.+|\/\*.+?\*\/')
    m = p.search(event)
    
    if m:
        event = p.sub(' ', event)
    
    event = event.strip()

    # Compress whitespace between fields
    p = re.compile('(\".+?\"|\{\{.+?\}\}|\[.+?\]|\S+)')
    event = ' '.join(p.findall(event))

    return event

def number_of_pfields(event):
    '''Counts the pfields present in an i-event string, returning
    an integer.'''
    
    return len(get_pfield_list(event))

def get_pfield_list(event):
    '''Creates a list of only pfield elements'''

    event = sanitize_event(event)
    return split_event(event)    

def split_event(event):
    '''Breaks a score event into a list.
    
    The process is ignorant of comments, and will include these as
    list items. Use santize_event() prior to using this function if
    your plans are to process the event further.
    
    If you require that white space and comments be preserved, use
    the function tokenize_event()
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
                  \;.+        |
                  \/\*.+?\*\/ |
                  \S+(?=\/\*) |
                  \S+(?=;)    |
                  \S+)
                  '''
                  
    p = re.compile(pattern, re.VERBOSE)

    return p.findall(event)

def tokenize_event(event):
    '''Breaks a score event into a list similar to split_event,
    except elements of white space are preserved, and returns a list.
    
    Beware that this function will attempt to token non-valid events,
    but the results are not to be trusted.
    '''
    
    tokens = []

    # Get leading white space and /* comments */
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
                  \;.+        |
                  \/\*.+?\*\/ |
                  \S+(?=\/\*) |
                  \S+(?=;)    |
                  \S+)
                  '''
    
    p = re.compile(pattern, re.VERBOSE)
    
    for t in p.findall(event):
        tokens.append(t)
    
    return tokens
    
def get_pfield(event, pfield):
    '''Searches an i-event string for a pfield specified by the
    the caller by index, and returns the content.
    
    The pfield maybe a number, string, expression, or a statement.
    Comments are right out.
    '''
    
    event = sanitize_event(event)
    event_list = split_event(event)

    if pfield in range(len(event_list)):
        value = event_list[pfield]
    else:
        value = None

    return value

def set_pfield(event, pfield, value):
    '''Replaces a pfield with the supplied value in an i-event
    string, and returns a new string.'''

    # Skip if pfield is out of range
    if pfield not in range(number_of_pfields(event)):
        '%%% set_pfield not in range'
        return event
    
    tokens = tokenize_event(event)
    
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
            tokens[i] = value
            break

    return ''.join(tokens)

def swap_pfields(event, pfield_a, pfield_b):
    '''Swaps pfields of an event at the two specified indexes'''

    a = get_pfield(event, pfield_a)
    b = get_pfield(event, pfield_b)

    event = set_pfield(event, pfield_a, b)
    event = set_pfield(event, pfield_b, a)

    return event

def insert_pfield(event, pfield, fill='.'):
    '''Inserts a pfield.'''
    
    if pfield in range(number_of_pfields(event)):
        pf = get_pfield(event, pfield)
        new = [fill, ' ', pf]
        event = set_pfield(event, pfield, ''.join(new))  
    elif pfield == number_of_pfields(event):
        pf = get_pfield(event, pfield - 1)
        new = [pf, ' ', fill]
        event = set_pfield(event, pfield - 1, ''.join(new))  
    
    return event

def push_pfield(event, fill='.'):
    '''Appends a pfield after the last pfields.'''

    return insert_pfield(event, number_of_pfields(event), fill)

def remove_pfield(event, pfield):
    '''Eliminates a pfield and returns a tuple: (new event,
    pfield removed)
    
    Leaves surrounding white space. Use other functions to clean
    white if that is what you wish.
    '''
    
    pf = ''
    
    if pfield in range(number_of_pfields(event)):
        pf = get_pfield(event, pfield)
        event = set_pfield(event, pfield, '')
    
    return event, pf
    
def pop_pfield(event):
    '''Grabs the last pfield, and removes from event. Perhaps this
    should return new_string, popped_pfield?
    '''
    
    return remove_pfield(event, number_of_pfields(event) - 1)

def swap_columns(score, statement, identifier, a, b):
    '''Exchanges all score columns for a specified statement and
    identifier.
    
    Returns a new string.
    '''
    
    score_output = []
    score_list = score.splitlines(True)
    
    for row in score_list:
        # Test statement type and statement identifier.
        if get_pfield(row, 0) is statement\
                and get_pfield(row, 1) == str(identifier):
                    
            # Check that pfields a and b are in range, return original if True.
            for pf in (a, b):
                if pf not in range(number_of_pfields(row)):
                    return score
                    
            # Swap pfields
            score_output.append(swap_pfields(row, a, b))
        else:
            score_output.append(row)
            
    return ''.join(score_output)
    
def shift_column(score, statement, identifier, move):
    '''NOT IMPLEMENTED.
    
    Shifts a columns pfield position.
    
    The move parameter specifies how many columns to shift, with a
    positive number indicating moving to the right, and a negative
    number indicating a move to the left.
    '''
    
    pass

def insert_column(score, statement, identifier, index, fill='.'):
    '''NOT IMPLEMENTED.'''
    pass

def remove_column(score, statement, identifier, index):
    '''NOT IMPLEMENTED.'''
    pass
    
def pop_column(score, statement, identifier):
    '''NOT IMPLEMENTED.'''
    pass
    
def push_column(score, statement, identifier, fill='.'):
    '''NOT IMPLEMENTED.'''
    pass
