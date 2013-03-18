# Copyright (C) 2009 Jacob Joaquin
#
# This file is part of csd.
# 
# csd is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# csd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with csd.  If not, see <http://www.gnu.org/licenses/>.

'''These methods operate on selections.'''

from csd.sco import event
from csd.sco import element

def __convert_args_to_numeric(args_tuple):
    '''Returns a list of numeric args.'''

    args = list(args_tuple)
    for i, a in enumerate(args):
        if type(a) is str:
            args[i] = element.str_to_numeric(a)
    return args

def __pfield_index_to_list(pfield_index_list):
    '''Forces a single value to be translated into a list.'''
    
    if type(pfield_index_list) is not list:
        pfield_index_list = [pfield_index_list]
        
    return pfield_index_list

def operate_numeric(selection, pfield_index_list, pfunction, *args):
    '''Processes a matrix of pfields and events using the supplied
    :term:`pfunction` and any optional arguments.
    
    In cases where the original numeric pfield was an int, but
    processed with floats, the int will be output as a float in the
    score, even if the output contains no fractional parts.
    
    Example::
    
        >>> def multiply(pf, m): return pf * m
        ... 
        >>> sco.operate_numeric({0: 'i 1 0 4 1.0 440', 1: 'i 1 4 4 0.5 880'},
        ...                     5, multiply, 3)
        {0: 'i 1 0 4 1.0 1320', 1: 'i 1 4 4 0.5 2640'}
        
    A lambda function can specified as the pfunction argument::
    
        # Invert pfield
        operate_numeric(score, pf, lambda x: 1.0 / x)
        
    See :term:`pfield_index_list`, :term:`pfunction`, :term:`selection`

    '''

    # Args need to be numeric
    args = __convert_args_to_numeric(args)
    
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
                selection[k] = v = event.set(v, pf, pfunction(pf_value, *args))

    return selection

def operate_string(selection, pfield_index_list, pfunction, *args):
    # Convert single single value to list
    pfield_index_list = __pfield_index_to_list(pfield_index_list)
    
    # Operate on all events in selection.  Sorted is a must.
    for k, v in sorted(selection.iteritems()):
        
        # Operate on each pfield
        for pf in pfield_index_list:
            pf_value = event.get(v, pf)
            selection[k] = v = event.set(v, pf, pfunction(pf_value, *args))

    return selection

def replace(selection, pfield_index_list, pgenerator, *args):
    '''Replaces pfield values in selection using a supplied pgenerator,
    function or method.
    
    This will overwrite and existing value, numeric or not, in a
    pfield, including elements such as carry statements and
    expressions.
    
    Use this function instead of operate_numeric() when you want to
    create new data, instead of altering existing pfield data. This
    works wells with python objects that have a persistant state.
    
    
    
    Example::
        
        >>> def return_something(x):
        ...     return x
        ... 
        >>> selection.replace({0: 'i 1 0 4 1.0 440'}, 5, return_something, '$foo')
        {0: 'i 1 0 4 1.0 $foo'}
        
    See :term:`pfield_index_list`, :term:`pgenerator`, :term:`selection`
    '''
    
    pfield_index_list = __pfield_index_to_list(pfield_index_list)

    # Operate on all events in selection.  Sorted is a must.
    for k, v in sorted(selection.iteritems()):
        
        # Operate on each pfield
        for pf in pfield_index_list:
            selection[k] = v = event.set(v, pf, pgenerator(*args))

    return selection

def swap(selection, pfield_index_a, pfield_index_b):
    '''Returns a copy of selection with swapped pfield columns.

    Example::
        
        >>> selection.swap({0: 'i 1 0 4 440 1.0', 1: 'i 1 4 4 880 0.5'}, 4, 5)
        {0: 'i 1 0 4 1.0 440', 1: 'i 1 4 4 0.5 880'}

    
    See :term:`selection`, :term:`pfield_index`
           
    '''
    
    for k, v in selection.iteritems():
        selection[k] = event.swap(v, pfield_index_a, pfield_index_b)
    
    return selection

