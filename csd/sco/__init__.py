'''These methods operate on multiple score events at a time. Generally
speaking, these methods specifically deal with columns, where
csd.sco.event deals with rows.

'''

from csd.sco import event

def merge(score, score_dict):
    '''Merges a score_dict back into a score string, overwriting the
    existing parts of the score.
    
    The follow example merges a score string with a score_dict,
    replacing the second line (index 1) with a new event.
    
    Example::
        
        >>> sco.merge(
        ... """i 1 0 4 1.0 440
        ... i 1 4 4 0.5 880""",
        ... {1: 'i 1 4 4 0.5 1138'})
        'i 1 0 4 1.0 440\\ni 1 4 4 0.5 1138'
        
    '''
    
    # Convert score string to list    
    s_list = score.splitlines()

    # Merge score_dict with the score list    
    for k, v in score_dict.items():
        
        # Merge list of events
        if type(v) is list:
            s_list[k] = '\n'.join(v)
            
        # Merge single event
        else:
            s_list[k] = v

    # Appends an empty event in case of newline
    output = '\n'.join(s_list)
    if score.endswith('\n'):
        output = output + '\n'
    
    return output      

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
    '''Returns a score_dict with swapped pfield columns.
    
    .. warning:: Needs to check for multiple events as lists.
    
    '''
    
    for k, v in score_dict.iteritems():
        score_dict[k] = event.swap(v, x, y)
    
    return score_dict
    
