'''These methods operate on multiple score events at a time. Generally
speaking, these methods specifically deal with columns, where
csd.sco.event deals with rows.'''

from . import event

def swap(score, statement, identifier, a, b):
    '''Exchanges all score columns for a specified statement and
    identifier.
    '''
    
    score_output = []
    score_list = score.splitlines(True)
    
    for row in score_list:
        # Test statement type and statement identifier.
        if event.get(row, 0) is statement\
                and event.get(row, 1) == str(identifier):
                    
            # Check that pfields a and b are in range, return original if True.
            for pf in (a, b):
                if pf not in range(event.number_of_pfields(row)):
                    return score
                    
            # Swap pfields
            score_output.append(event.swap(row, a, b))
        else:
            score_output.append(row)
            
    return ''.join(score_output)
    

