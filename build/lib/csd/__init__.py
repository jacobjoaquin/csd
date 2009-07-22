'''Parses Unified Csound CSD code.'''

import re

def get_base64(csd):
    pass

def get_csound(csd):
    pass

def get_midi_base64(csd):
    pass    
    
def get_options(csd):
    pass
    
def get_orchestra(csd):
    pass

def get_sample_base64(csd):
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
    pass
    
def get_license(csd):
    pass
