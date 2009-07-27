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

def __create_pattern(tag_name):
    '''Generates a regular expression string for pulling data from
    inbetween markup tags.'''
    
    return '<' + tag_name + '>.*?\n(.*)<\/' + tag_name + '>'
    
def get_base64(csd):
    '''Not implemented.'''

    pass

def get_csound(csd):
    '''Not implemented.'''

    pass

def get_license(csd):
    '''Not implemented.'''

    pass
    
def get_midi_base64(csd):
    '''Not implemented.'''

    pass    
    
def get_options(csd):
    '''Not implemented.'''

    pass
    
def get_orchestra(csd):
    '''Returns the orchestra from a Csound CSD.'''
    
    p = re.compile(__create_pattern('CsInstruments'), re.DOTALL)
    return ''.join(p.findall(csd))

def get_sample_base64(csd):
    '''Not implemented.'''

    pass

def get_score(csd):
    '''Returns the score from a Csound CSD.'''
    
    p = re.compile(__create_pattern('CsScore'), re.DOTALL)
    return ''.join(p.findall(csd))

def get_version(csd):
    '''Not implemented.'''

    pass
    
def overwrite_score(csd, sco):
    '''Returns a new csd string with a new score.'''
    
    pre = re.compile('(.*<CsScore>.*?\n)', re.DOTALL)
    post = re.compile(r'(</CsScore>.*)', re.DOTALL)
    
    output = []
    output.append(''.join(pre.findall(csd)))
    output.append(sco)

    # Assert there is a newline between sco and closing CsScore tag
    if not sco.endswith('\n'):
        output.append('\n')

    output.append(''.join(post.findall(csd)))
    
    return ''.join(output)

