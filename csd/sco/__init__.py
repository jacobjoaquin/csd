'''These methods operate on multiple score events at a time. Generally
speaking, these methods specifically deal with columns, where
csd.sco.event deals with rows.

.. note:: Need to create a glossary to include terms like score,
   selection, element (atom), event, pf_function, etc...

'''

from csd.sco import event
from csd.sco import element
from csd.sco import selection

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
    
def map_(score, pattern, pfield_index_list, pf_function, *args):
    '''Not yet implemented.
    
    Consolidates operate functions into a single line.  Accepts a score
    and returns a score.
    
    '''
    
    selection_ = select(score, pattern)
    selection_ = selection.operate_numeric(selection_, pfield_index_list,
                                           pf_function, *args)
    return merge(score, selection_)
    
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

