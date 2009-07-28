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

'''Preprocessor functions.'''

from csd.sco import event
from csd.sco import element
#from csd.sco import selection

def carry_to_value(score):
    '''Not implemented.'''
    
    pass
    
def value_to_carry(score):
    '''Replaces subsequent repeated values with a carry (.)
    
    Identical expressions do no carry, as a carry only copies the first
    value output from an expression.  This breaks the form when multiple
    random evaluations are part of the score.
    
    Macros do no carry as they may contain expressions.
    
    No-carries are not carried.
    '''
    
    event_list = score.splitlines(True)    
    last_identifier = None
    last_values = []
    output = []

    # Explicitly state pfield 3 instead a magic number.  Carry
    # statements only substitute for pfields 3 or higher.
    PFIELD_3 = 3

    size = 0
    
    # Excluded element token types
    elements = [element.EXPRESSION, element.MACRO, element.NO_CARRY];
    
    for e in event_list:
        if event.match(e, {0: 'i', 1: last_identifier}):
            lv = len(last_values)
            
            for i in range(PFIELD_3, max(event.number_of_pfields(e), lv)):
                this_pfield = event.get(e, i)

                if element.token_type(this_pfield) == element.NO_CARRY:
                    last_values[i] = this_pfield
                    break
                    
                elif element.token_type(last_values[i]) == element.NO_CARRY:
                    break
                    
                elif (this_pfield == last_values[i] and
                        element.token_type(this_pfield) not in elements):
                            
                    # Replace pfield with carry
                    e = event.set(e, i, '.')
                    
                elif this_pfield == None:
                    
                    # Add a carry if one does not exist
                    e = event.push(e, '.')
                    
                else:
                    last_values[i] = this_pfield

            output.append(e)
            
        else:
            last_identifier = event.get(e, 1)
            last_values = event.get_pfield_list(e)
            output.append(e)
        
    return ''.join(output)
        

