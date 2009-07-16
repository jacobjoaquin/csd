'''Csound score elements.'''

import re

import csd.sco.event

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

# Make COMMENT a type?
# Make WHITESPACE a type?
# Make NEWLINE a type?
# Make COMPOUND_STATEMENT a type?  For throwing error purposes?

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

# Valid pfield data types
_VALID_PFIELDS = [STATEMENT, NUMERIC, MACRO, EXPRESSION, STRING, CARRY, RAMP,
                 EXPONENTIAL_RAMP, RANDOM, CARRY_PLUS, NO_CARRY, NEXT_PFIELD,
                 PREVIOUS_PFIELD]

def is_valid(element):
    '''Returns a boolean value indicating if the element if valid.
    
    An example of an invalid element is a compound element, consiting
    of two or more elements.  Continuous space is valid.

    Example::
        
        >>> element.is_valid('440')
        True
        >>> element.is_valid(' ')
        True
        >>> element.is_valid('i 1')
        False
        
    '''

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

    tokens = []
    p = re.compile(pattern, re.VERBOSE)
    [tokens.append(t) for t in p.findall(element)]        
    
    return len(tokens) == 1
        
def str_to_numeric(numeric):
    '''Converts a str to numeric type int or float.'''
    
    try:
        return int(numeric)
    except:
        return float(numeric)
        
def is_valid_pfield(element):
    '''Returns a boolean value indicating if element is a pfield data
    type.
    
    Example::
        
        >>> element.is_valid_pfield('440')
        True
        >>> element.is_valid_pfield(' ')
        False
        >>> element.is_valid_pfield('i 1')
        False
    
    '''
    
    if is_valid(element):
        return token_type(element) in _VALID_PFIELDS
    else:
        return False
    
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

    # Check for valid element first
    if is_valid(element) is False:
        return None

    # Determine element type        
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

