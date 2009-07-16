'''These methods operate on multiple score events at a time. Generally
speaking, these methods specifically deal with columns, where
csd.sco.event deals with rows.

'''

from csd.sco import event
from csd.sco import element

def merge(score, selection):
    '''Merges a selection back into a score string, overwriting the
    existing parts of the score.
    
    The follow example merges a score string with a selection,
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

    # Merge selection with the score list    
    for k, v in selection.items():
        
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

def operate_numeric(selection, pfield, pf_function, *args):
    '''Not implemented yet.
    
    If the original pfield was an int, and a function performs
    calculations involving a float, it will be returned as a float
    with decimal point and trailing number(s).  For example, a
    13 will be returned as 13.0 if summed with 0.0
    
    '''
    
    def _str_to_numeric(str_):
        '''Converts a str to numeric type int or float.
        
        .. note:: Should this inspire a csd.utils module?  Or should
        this go into csd.sco.element?
        
        '''
        
        try:
            return int(str_)
        except:
            return float(str_)

    # Convert args from str to number types int or float
    args = list(args)
    for i, a in enumerate(args):
        if type(a) is str:
            args[i] = _str_to_numeric(a)

    # Convert pfield str in int    
    pfield = int(pfield)
    
    # Operate on all events in selection
    for k, v in selection.iteritems():
        pf_value = event.get(v, pfield)
        
        # Preserve non-numeric pfields
        if element.token_type(pf_value) is element.NUMERIC:
            pf_value = _str_to_numeric(pf_value)
            selection[k] = event.set(v, pfield, pf_function(pf_value, *args))

    return selection
    
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

def swap(selection, x, y):
    '''Returns a selection with swapped pfield columns.
    
    .. warning:: Needs to check for multiple events as lists.
    
    '''
    
    for k, v in selection.iteritems():
        selection[k] = event.swap(v, x, y)
    
    return selection
    
