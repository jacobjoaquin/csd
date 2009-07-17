'''These methods operate on multiple score events at a time. Generally
speaking, these methods specifically deal with columns, where
csd.sco.event deals with rows.

.. note:: Need to create a glossary to include terms like score,
   selection, element (atom), event, pf_function, etc...

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

    See :term:`selection`, :term:`score`
    
    '''
    
    # Convert score string to list    
    s_list = score.splitlines()

    # Recursive function to process lists within lists
    def _sub_merge(event, temp_list):
        if type(event) is list:
            for e in event:
                _sub_merge(e, temp_list)
        else:
            temp_list.append(event)
            
    # Merge selection with the score list    
    for k, v in selection.items():
        temp_list = []
        _sub_merge(v, temp_list)
        s_list[k] = '\n'.join(temp_list)        

    # Appends an empty event in case of newline
    output = '\n'.join(s_list)
    if score.endswith('\n'):
        output = output + '\n'
    
    return output      

def operate_numeric(selection, pfield_list, pf_function, *args):
    '''Processes a matrix of pfields and events using the supplied
    pf_function and any optional arguments.
    
    In cases where the original numeric pfield was an int, but
    processed with floats, the int will be output as a float in the
    score, even if the output contains no fractional parts.  e.g. 1.0
    
    Example::
    
        >>> def multiply(pf, m): return pf * m
        ... 
        >>> sco.operate_numeric({0: 'i 1 0 4 1.0 440', 1: 'i 1 4 4 0.5 880'},
        ...                     5, multiply, 3)
        {0: 'i 1 0 4 1.0 1320', 1: 'i 1 4 4 0.5 2640'}
        
    See :term:`pf_function`, :term:`pfield_list`, :term:`selection`

    '''

    # Convert args from str to number types int or float
    args = list(args)
    for i, a in enumerate(args):
        if type(a) is str:
            args[i] = element.str_to_numeric(a)
    
    # Convert single single value to list
    if type(pfield_list) is not list:
        pfield_list = [pfield_list]
    
    # Operate on all events in selection
    for k, v in selection.iteritems():
        
        # Operate on each pfield
        for i, pf in enumerate(pfield_list):
            pf_value = event.get(v, pf)
            
            # Preserve non-numeric pfields
            if element.token_type(pf_value) is element.NUMERIC:
                pf_value = element.str_to_numeric(pf_value)
                v = event.set(v, pf, pf_function(pf_value, *args))
                selection[k] = v

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
        
    See :term:`pattern`, :term:`score`
    
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
        
    See :term:`score`

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

    See :term:`selection`, :term:`score`
    
    .. warning:: Needs to check for multiple events as lists. May
       create a internalized function for this.  e.g. _iter_selection()
    
    '''
    
    for k, v in selection.iteritems():
        selection[k] = event.swap(v, x, y)
    
    return selection
    
