'''This module operates on individual Csound score events.'''

import re

from csd.sco import element

def get(event, pfield_index):
    '''Returns a pfield element for an event.
    
    The pfield maybe a number, string, expression, or a statement.
    Comments are right out.
    
    Example::

        >>> event.get('i 1 0 4 1.0 440  ; A440', 5)
        '440'

    See :term:`event`, :term:`pfield`
    
    '''

    # Pfield must be of type int, as it refers to an index in a list.
    pfield_index = int(pfield_index)

    event_list = get_pfield_list(event)

    if pfield_index in range(len(event_list)):
        return event_list[pfield_index]
    else:
        return None

def get_pfield_list(event):
    '''Returns a list of all the pfield elements in a list.
    
    Example::
        
        >>> event.get_pfield_list('i 1 0 4 1.0 440  ; A440')
        ['i', '1', '0', '4', '1.0', '440']
        
    See :term:`event`
    
    '''

    return split(sanitize(event))    

def get_trailing_comment(event):
    '''Returns a string of a trailing inline comment for an event.

    Returns an empty string if no trailing comment is found.

    Example::
        
        >>> event.get_trailing_comment('i1 0 4 1.0 440  ; comment')
        '; comment'
        
    See :term:`event`
    
    '''

    tokens = tokenize(event)
    tokens.reverse()
    
    # Get the index of the first valid pfield statement
    for i, t in enumerate(tokens):
        if element.is_valid_pfield(t):
            break

    # Un-reverse list and compensate index
    tokens.reverse()
    i = len(tokens) - i
    
    return ''.join(tokens[i:]).strip()

def insert(event, pfield_index, fill='.'):
    '''Returns a new event with an inserted pfield element.
    
    The fill attribute is the character or string which will be
    inserted into the event.

    Example::
        
        >>> event.insert('i 1 0 4 1.0 440  ; A440', 5, '1138')
        'i 1 0 4 1.0 1138 440  ; A440'
        
    See :term:`event`, :term:`pfield`
    
    '''    

    # Fill must be a string. This allows numbers to be passed to function.
    fill = str(fill)
    
    if pfield_index in range(number_of_pfields(event)):
        pf = get(event, pfield_index)
        new = [fill, ' ', pf]
        event = set(event, pfield_index, ''.join(new))  
    elif pfield_index == number_of_pfields(event):
        pf = get(event, pfield_index - 1)
        new = [pf, ' ', fill]
        event = set(event, pfield_index - 1, ''.join(new))  
    
    return event

def match(event, pattern):
    '''Returns a boolean determined whether an event matches the
    requirements of a pattern.
    
    A pattern is built from a Python dict, and must follow strict
    guidelines.  The key must be an integer, as the key is the index
    of the pfield in which this function will test.  The value of the
    dict can be either a single value or several values in list form.
        
    A pattern that returns True for i-events::
        
        {0: 'i'}
    
    A pattern that returns True for i-events and f-tables::
        
        {0: ['i', 'f']}
        
    A single pattern may check against multiple pfields.  The following
    example returns True for an i-event with an identifier of 1, 2, or
    3::
    
        {0: 'i', 1: [1, 2, 3]}
    
    Example::
       
        >>> event.match('i 1 0 4 1.0 440', {0: 'i'})
        True
        >>> event.match('i 1 0 4 1.0 440', {0: 'i', 1: 1})
        True
        >>> event.match('i 1 0 4 1.0 440', {0: 'i', 1: 2})
        False
       
    .. note:: Limited support for the moment.  Functions for designing
       patterns may come at a later time.

    See :term:`event`, :term:`pattern`.
    
    '''
 
    # Return false if empty
    if pattern == {}:
        return False
        
    for pf, v in pattern.items():
        # Items in v must be of type str
        if type(v) is list:
            for i, item in enumerate(v):
                v[i] = str(item)
                
        # v must be in list form
        else:
            v = [str(v)]

        # Test to see if event passes all requirements of the pattern
        if (get(event, pf) in v) is False:
            return False

    return True
    
def number_of_pfields(event):
    '''Returns an integer of the amounts of pfield elements in an
    event.
    
    The statement (pfield 0) is also counted.  Comments and whitespace
    are omitted from the tally.

    Example::

        >>> event.number_of_pfields('i 1 0 4 1.0 440  ; A440')
        6
        
    See :term:`event`

    '''
    
    return len(get_pfield_list(event))

def pop(event):
    '''Removes the last pfield element from an event and returns a
    tuple containing a new event and the removed element.

    This function preserves whitespace.    

    Example::
        
        >>> event.pop('i 1 0 4 1.0 440  ; A440')
        ('i 1 0 4 1.0   ; A440', '440')
        
    See :term:`event`

    '''
    
    return remove(event, number_of_pfields(event) - 1)

def push(event, fill='.'):
    '''Appends a pfield element to the last pfield and returns the new
    event.
    
    The fill attribute is the character or string which will be
    inserted into the event.

    Example::

        >>> event.push('i 1 0 4 1.0 440  ; A440', '1138')
        'i 1 0 4 1.0 440 1138  ; A440'

    See :term:`event`

    '''

    return insert(event, number_of_pfields(event), fill)

def remove(event, pfield_index):
    '''Removes a pfield and returns a tuple containing the new event
    and the removed element.

    This function preserves whitespace.    

    Example::
        
        >>> event.remove('i 1 0 4 1.0 440  ; A440', 4)
        ('i 1 0 4  440  ; A440', '1.0')
        
    See :term:`event`, :term:`pfield`

    '''

    # An emptry string is preferable than None for the return    
    pf = ''
    
    if pfield_index in range(number_of_pfields(event)):
        pf = get(event, pfield_index)
        event = set(event, pfield_index, '')
    
    return event, pf
    
def sanitize(event):
    '''Returns a copy of the score event with extra whitespace and
    comments removed.

    This function will introduce a single space between a statement and
    the following non-whitespace element.

    Example::
        
        >>> event.sanitize('i1 0 4    1.0 440  ; A440')
        'i 1 0 4 1.0 440'
        
    See :term:`event`

    '''

    # Remove comments
    p = re.compile('\;.*|\/\*.*?\*\/')
    m = p.search(event)
    
    if m:
        event = p.sub(' ', event)
    
    event = event.strip()

    # Insert a single whitespace after statement if necessary
    event = statement_spacer(event, spacer=1)
    
    # Compress whitespace between fields
    p = re.compile('(\".+?\"|\{\{.+?\}\}|\[.+?\]|\S+)')
    
    return ' '.join(p.findall(event))

def set(event, pfield_index, value):
    '''Returns a new event string with the specified pfield set with
    the new value.
    
    Example::
        
        >>> event.set('i 1 0 4 1.0 440  ; A440', 5, 1138)
        'i 1 0 4 1.0 1138  ; A440'
        
    See :term:`event`, :term:`pfield`

    '''

    # Pfield must be of type int, as it refers to an index in a list.
    pfield_index = int(pfield_index)
    
    # Skip if pfield is out of range
    if pfield_index not in range(number_of_pfields(event)):
        return event
    
    tokens = tokenize(event)
    
    pf_index = -1
    for i, t in enumerate(tokens):
        if pf_index == -1:
            if element.token_type(t) == element.STATEMENT:
                pf_index += 1
        else:
            if element.is_valid_pfield(t):
                pf_index += 1

        if pf_index == pfield_index:
            
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
        
    See :term:`event`

    '''

    # Separate statement from p1 if necessary
    event = statement_spacer(event, spacer=1)

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

def statement_spacer(event, spacer=1):
    '''Returns a new string with the whitespace between a statement
    and the following element altered.

    The spacer attribute is the number of whitespace characters to
    place between the statement and the following pfield.
    
    Example::
        
        >>> event.statement_spacer('i1 0 4 1.0 440')
        'i 1 0 4 1.0 440'
    
    See :term:`event`

    '''
    
    tokens = tokenize(event)

    # Index of statement requires initializing, in case of zero tokens.
    i = 0

    # Get index for the statement and identifier    
    for i, e in enumerate(tokens):
        if element.token_type(e) == element.STATEMENT:
            break
            
    # Modify tokens[] item proceeding the statement
    i = i + 1
    if i < len(tokens):
        tokens[i] = ' ' * spacer + tokens[i].lstrip()

    return ''.join(tokens)

def swap(event, pfield_index_a, pfield_index_b):
    '''Returns a new event string after swapping two pfield elements.
    
    Example::
        
        >>> event.swap('i 1 0 4 1.0 440 ; A440', 4, 5)
        'i 1 0 4 440 1.0 ; A440'

    .. note:: This currently will not swap pfield 0.  Not sure if it
       should, though throwing an error might be in order.
       
    See :term:`event`

    '''

    a, b = get(event, pfield_index_a), get(event, pfield_index_b)
    event = set(event, pfield_index_a, b)
    event = set(event, pfield_index_b, a)
    
    return event

def tokenize(event):
    '''Returns a list of all elements in an event.
    
    Elements include pfield data, comments and whitespace.

    Example::
        
        >>> event.tokenize('i 1 0 4 1.0 440  ; A440')
        ['i', ' ', '1', ' ', '0', ' ', '4', ' ', '1.0', ' ', '440', '  ', '; A440']
    
    .. note:: This function will attempt to tokenize invalid elements.
        Be sure that the event you provide is syntactically correct.
        
    See :term:`event`

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
        
    # Tokenize the rest of the event
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
    [tokens.append(t) for t in p.findall(event)]        

    return tokens

