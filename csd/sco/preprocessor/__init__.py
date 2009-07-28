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
#from csd.sco import element
#from csd.sco import selection

def carry_to_value(score):
    '''Not implemented.'''
    
    pass
    
def value_to_carry(score):
    '''Replaces subsequent repeated values with a carry (.)'''
    
    event_list = score.splitlines(True)    
    last_identifier = None
    last_values = []
    output = []

    # Explicitly state pfield 3 instead a magic number.  Carry
    # statements only substitute for pfields 3 or higher.
    pfield_3 = 3
    
    for e in event_list:
        if event.match(e, {0: 'i', 1: last_identifier}):
            for i in range(pfield_3, event.number_of_pfields(e)):
                if event.match(e, {i: last_values[i]}):
                    e = event.set(e, i, '.')
                    
                else:
                    last_values[i] = event.get(e, i)
                    
            output.append(e)
            
#        elif event.get(e, 0) == None:
#            output.append(e)

        else:
#            last_identifier = ''
            last_identifier = event.get(e, 1)
#            last_values = []
            last_values = event.get_pfield_list(e)
            output.append(e)
        
    return ''.join(output)
    

