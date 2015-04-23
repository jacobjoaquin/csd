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

'''These methods operate on multiple score events at a time. Generally
speaking, these methods specifically deal with columns, where
csd.sco.event deals with rows.

'''

from csd.sco import event
from csd.sco import element
from csd.sco import selection

def __flatten_list(parent_list):
    '''Returns a list with all embedded lists brought to the
    surface.'''
    
    this_list = []
    child_list = []

    if not isinstance(parent_list, list):
        return [parent_list]
        
    for i in parent_list:
        if isinstance(i, list):
            child_list = __flatten_list(i)
            for j in child_list:
                this_list.append(j)
        else:
            this_list.append(i)

    return this_list

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

    # Merge flattened selection with the score list    
    for k, v in selection.iteritems():
        s_list[k] = '\n'.join(__flatten_list(v))

    output = '\n'.join(s_list)

    # Appends an empty event in case of newline
    if score.endswith('\n'):
        output = output + '\n'

    return output      
    
def map_(score, pattern, pfield_index_list, pfunction, *args):
    '''Performs a pfunction on multiple pfields in a score, returning
    a new score.
    
    Example:
        
        >>> def add(x, y):
        ...     return x + y
        ... 
        >>> sco.map_("""
        ... i 1 0 4 1.0 440
        ... i 1 4 4 0.5 880""", {0: 'i'}, 5, add, 777)
        '\\ni 1 0 4 1.0 1217\\ni 1 4 4 0.5 1657'
    
    Example using lambda function::
        
        >>> sco.map_("""
        ... i 1 0 4 1.0 440
        ... i 1 4 4 0.5 880""", {0: 'i'}, 5, lambda x: x * 3)
        '\\ni 1 0 4 1.0 1320\\ni 1 4 4 0.5 2640'

    See :term:`pattern`, :term:`pfield_index_list`, :term:`pfunction`,
    :term:`score`

    '''
    
    selection_ = select(score, pattern)
    selection_ = selection.operate_numeric(selection_, pfield_index_list,
                                           pfunction, *args)
    return merge(score, selection_)
    
def select(score, pattern):
    '''Returns a selection from a score.
    
    Example::

        >>> sco.select(
        ... """f 1 0 8192 10 1
        ... i 1 0 4 1.0 440
        ... i 1 4 4 0.5 880"""
        ... , {0: 'i'})
        {1: 'i 1 0 4 1.0 440', 2: 'i 1 4 4 0.5 880'}
        
    See :term:`pattern`, :term:`score`, :term:`selection`
    
    '''

    # Convert score string to list    
    s_list = score.splitlines()
    
    # Return matched events
    return {i: e for i, e in enumerate(s_list) if event.match(e, pattern)}

def select_all(score):
    '''Returns a selection of all events in a score.

    Example::

        >>> sco.select_all(
        ... """f 1 0 8192 10 1
        ... i 1 0 4 1.0 440
        ... i 1 4 4 0.5 880""")
        {0: 'f 1 0 8192 10 1', 1: 'i 1 0 4 1.0 440', 2: 'i 1 4 4 0.5 880'}
        
    See :term:`score`, :term:`selection`

    '''

    # Convert score string to list
    s_list = score.splitlines()
    
    # Dictionary to store all events.  {index_of_event: event}
    selection_ = {}
    
    # Append each event
    for i, e in enumerate(s_list):
        selection_[i] = e
    
    # Appends an empty event in case of newline
    if score.endswith('\n'):
        selection_[i + 1] = ''

    return selection_

