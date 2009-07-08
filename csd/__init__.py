import re

def check():
    print 'check()', __file__
    
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

