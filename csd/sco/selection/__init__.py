'''These methods operate on selections.'''

from csd.sco import event
from csd.sco import element

#def operate(): pass
#def operate_str(): pass
#def operate_macro(): pass
#def operate_expression(): pass

def __pfield_index_to_list(pfield_index_list):
    '''Forces a single value to be translated into a list.'''
    
    if type(pfield_index_list) is not list:
        pfield_index_list = [pfield_index_list]
        
    return pfield_index_list

def replace(selection, pfield_index_list, pgenerator, *args):
    '''Replaces pfield values in an event/column matrix using a
    supplied pgenerator function or method.'''
    
    pfield_index_list = __pfield_index_to_list(pfield_index_list)

    # Operate on all events in selection.  Sorted is a must.
    for k, v in sorted(selection.iteritems()):
        
        # Operate on each pfield
        for pf in pfield_index_list:
            v = event.set(v, pf, pgenerator(*args))
            selection[k] = v

    return selection

def operate_numeric(selection, pfield_index_list, pfunction, *args):
    '''Processes a matrix of pfields and events using the supplied
    pfunction and any optional arguments.
    
    In cases where the original numeric pfield was an int, but
    processed with floats, the int will be output as a float in the
    score, even if the output contains no fractional parts.  e.g. 1.0
    
    Example::
    
        >>> def multiply(pf, m): return pf * m
        ... 
        >>> sco.operate_numeric({0: 'i 1 0 4 1.0 440', 1: 'i 1 4 4 0.5 880'},
        ...                     5, multiply, 3)
        {0: 'i 1 0 4 1.0 1320', 1: 'i 1 4 4 0.5 2640'}
        
    See :term:`pfunction`, :term:`pfield_list`, :term:`selection`

    '''

    # Convert args from str to number types int or float
    args = list(args)
    for i, a in enumerate(args):
        if type(a) is str:
            args[i] = element.str_to_numeric(a)
    
    # Convert single single value to list
    pfield_index_list = __pfield_index_to_list(pfield_index_list)
    
    # Operate on all events in selection.  Sorted is a must.
    for k, v in sorted(selection.iteritems()):
        
        # Operate on each pfield
        for pf in pfield_index_list:
            pf_value = event.get(v, pf)
            
            # Preserve non-numeric pfields
            if element.token_type(pf_value) is element.NUMERIC:
                pf_value = element.str_to_numeric(pf_value)
                v = event.set(v, pf, pfunction(pf_value, *args))
                selection[k] = v

    return selection

def swap(selection, a, b):
    '''Returns a selection with swapped pfield columns.

    See :term:`selection`, :term:`score`
    
    .. warning:: Needs to check for multiple events as lists. May
       create a internalized function for this.  e.g. _iter_selection()
    
    '''
    
    for k, v in selection.iteritems():
        selection[k] = event.swap(v, a, b)
    
    return selection

