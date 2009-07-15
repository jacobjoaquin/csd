'''These methods operate on multiple score events at a time. Generally
speaking, these methods specifically deal with columns, where
csd.sco.event deals with rows.

.. warning:: Stay away from this module for awhile.  This is currently
   ill-conceived.
   
'''

from csd.sco import event

'''Ideas.

def get_list_of(score, statements, identifiers):
    collection_of_matches = {}
    
    for i, e in enumerate(score):
        if event.get(0) is element.STATEMENT and event.get(1) == identifier:
            collection_of_matches({i: e})

    return collection_of_matches
    
'''

def select(score, pattern):
    '''Returns a dict with matched events from a score.
    {index_of_event: event}
    
    Example::

        >>> sco.match("""f 1 0 8192 10 1
        ... i 1 0 4 1.0 440
        ... i 1 4 4 0.5 880""", {0: 'i'})
        {1: 'i 1 0 4 1.0 440', 2: 'i 1 4 4 0.5 880'}
        
    '''

    # Convert score string to list    
    s_list = score.splitlines()
    
    # Dictionary to story matched events.  {index_of_event: event}
    m = {}

    # Get matched events
    for i, e in enumerate(s_list):
        if event.match(e, pattern):
            m[i] = e
            
    return m

def overwrite(score, dict_):
    '''Merges a back into a score string, overwriting existing events.'''
    pass
    
# Move this to csd.sco.column.swap()
def swap(score, statement, identifier, a, b):
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
    
def insert():
    pass
    
def pop():
    pass
    
def push():
    pass
    
def remove():
    pass
    
def replace(fill='.'):
    # replaces a column with stuff
    pass

