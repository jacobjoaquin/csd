'''These methods operate on selections.'''

from csd.sco import event
from csd.sco import element

def operate(): pass
#def operate_str(): pass
#def operate_macro(): pass
#def operate_expression(): pass

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
    
    # Operate on all events in selection.  Sorted is a must.
    for k, v in sorted(selection.iteritems()):
        
        # Operate on each pfield
        for pf in pfield_list:
            pf_value = event.get(v, pf)
            
            # Preserve non-numeric pfields
            if element.token_type(pf_value) is element.NUMERIC:
                pf_value = element.str_to_numeric(pf_value)
                v = event.set(v, pf, pf_function(pf_value, *args))
                selection[k] = v

    return selection

def swap(selection, x, y):
    '''Returns a selection with swapped pfield columns.

    See :term:`selection`, :term:`score`
    
    .. warning:: Needs to check for multiple events as lists. May
       create a internalized function for this.  e.g. _iter_selection()
    
    '''
    
    for k, v in selection.iteritems():
        selection[k] = event.swap(v, x, y)
    
    return selection

