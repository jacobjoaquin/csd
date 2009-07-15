'''These methods operate on multiple score events at a time. Generally
speaking, these methods specifically deal with columns, where
csd.sco.event deals with rows.

.. note:: Shaping up nicely.

'''

from csd.sco import event

def overwrite(score, dict_):
    '''Not implemented.
    
    Merges a back into a score string, overwriting existing events.
    
    '''
    pass

def select(score, pattern):
    '''Returns a dict with matched events from a score.
    {index_of_event: event}
    
    Example::

        >>> sco.select(
        ... """f 1 0 8192 10 1
        ... i 1 0 4 1.0 440
        ... i 1 4 4 0.5 880"""
        ... , {0: 'i'})
        {1: 'i 1 0 4 1.0 440', 2: 'i 1 4 4 0.5 880'}
        
    '''

    # Convert score string to list    
    s_list = score.splitlines()
    
    # Dictionary to store matched events.  {index_of_event: event}
    d = {}

    # Get matched events
    for i, e in enumerate(s_list):
        if event.match(e, pattern):
            d[i] = e
            
    return d

def select_all(score):
    '''Returns a dict of all events in a score, keyed by index.

    Example::

        >>> sco.select_all(
        ... """f 1 0 8192 10 1
        ... i 1 0 4 1.0 440
        ... i 1 4 4 0.5 880""")
        {0: 'f 1 0 8192 10 1', 1: 'i 1 0 4 1.0 440', 2: 'i 1 4 4 0.5 880'}
        
    '''

    # Convert score string to list    
    s_list = score.splitlines()
    
    # Dictionary to store all events.  {index_of_event: event}
    d = {}
    
    # Append each event
    for i, e in enumerate(s_list):
        d[i] = e
    
    # Appends an empty event in case of newline
    if score.endswith('\n'):
        d[i + 1] = ''

    return d

def swap(score_dict, x, y):
    '''Returns a score_dict with swapped pfield columns.'''
    
    for k, v in score_dict.iteritems():
        score_dict[k] = event.swap(v, x, y)
    
    return score_dict
    
# Move this to csd.sco.column.swap()
def swap_x(score, statement, identifier, a, b):
    '''Exchanges all score columns for a specified statement and
    identifier.
    '''
    
    score_output = []
    score_list = score.splitlines(True)
    
    for e in score_list:
        if event.match(e, {0: statement, 1:identifier}):
        
            # Check that pfields a and b are in range, return original if True.
            for pf in (a, b):
                if pf not in range(event.number_of_pfields(e)):
                    return score
                    
            # Swap pfields
            score_output.append(event.swap(e, a, b))
        else:
            score_output.append(e)
            
    return ''.join(score_output)

