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

'''Parses Unified Csound CSD code.'''

import re

def get_base64(csd):
    '''Not implemented.'''

    pass

def get_csound(csd):
    '''Not implemented.'''

    pass

def get_midi_base64(csd):
    '''Not implemented.'''

    pass    
    
def get_options(csd):
    '''Not implemented.'''

    pass
    
def get_orchestra(csd):
    '''Not implemented.'''

    pass

def get_sample_base64(csd):
    '''Not implemented.'''

    pass
    
def get_score(csd):
    '''Pulls score data from inbetween the <CsScore> markup tags in a
    Csound csd.
    
    .. note:: This should really reside somewhere else, such as a
        csdparse module.
    
    .. note:: There is an issue with an extra leading and extra
        trailing newline being introduced.
    '''
    
    p = re.compile('<CsScore>(.*)<\/CsScore>', re.DOTALL)
    return ''.join(p.findall(csd))

def get_version(csd):
    '''Not implemented.'''

    pass
    
def get_license(csd):
    '''Not implemented.'''

    pass
    
def replace_score(csd, sco):
    '''Not implemented.'''

    pass
