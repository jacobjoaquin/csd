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

'''Csound Python Score'''


from sys import argv
from itertools import imap
from itertools import chain
import atexit


class Filter:

    def __init__(self, statement, identifier, pfield, function, *args,
                 **kwargs):
        self.statement = statement
        self.identifier = identifier
        self.pfield = pfield
        self.function = function
        self.args = args
        self.kwargs = kwargs


class StackMatrix:
    
    def __init__(self):
        self._block_stack = [[]]

    def push_layer(self):
        self._block_stack.append([])

    def pop_layer(self):
        self._block_stack.pop()

    def push(self, the_filter):
        self._block_stack[-1].append(the_filter) 
        
    def pop(self):
        self._block_stack[-1].pop()

    def _flatten_list(self, parent_list):
        '''Returns a list with all embedded lists brought to the
        surface.'''
        
        this_list = []
        child_list = []

        if not isinstance(parent_list, list):
            return [parent_list]
            
        for i in parent_list:
            if isinstance(i, list):
                child_list = self._flatten_list(i)
                for j in child_list:
                    this_list.append(j)
            else:
                this_list.append(i)

        return this_list

    # TODO: Is returning an iter necessary?
    def iterall(self):
        return iter(self._flatten_list(self._block_stack))

    def merge_down(self):
        pass

class PythonScore(object):
    # TODO: 
    # Add reset()
    # Output thus far feature
   
    # postfilter workings:
    #   only applies to current score matrix block
    #   when cue is popped, score data is merged with previous block

    def __init__(self):
        self.cue = Cue(self)
        self._score_list = []
        self._prefilter_matrix = StackMatrix()
        self._score_matrix = StackMatrix()

    def f(self, *args):
        self._score_list.append(chain('f', args))
        self._score_matrix.append(chain('f', args))

    def i(self, *args):
        args = list(args)

        # Apply filters
        for f in self._prefilter_matrix.iterall():
            if f.identifier == args[0]:
                # Offset necessary as 'i' not in list, yet
                pfield = f.pfield - 1
                args[pfield] = f.function(args[pfield], *f.args, **f.kwargs)

        args[1] += self.cue.now()
        self._score_list.append(chain('i', args))

    def t(self, *args):
        self._score_list.append(chain('t 0', args))

    def prefilter(self, statement, identifier, pfield, func, *args, **kwargs):
        self._prefilter_matrix.push(Filter(statement, identifier, pfield,
                                                  func, *args, **kwargs))

    def postfilter(self, statement, identifier, pfield, func, *args, **kwargs):
        if not isinstance(statement, list):
            statement = [statement]

        if not isinstance(identifier, list):
            identifier = [identifier]

        if not isinstance(pfield, list):
            pfield = [pfield]

        # TODO: Handle multiple statments, tooooo
        for i, line in enumerate(self._score_list):
            line = list(line)
            if line[0] in statement and line[1] in identifier:
                for pf in pfield:
                    line[pf] = func(line[pf], *args, **kwargs)
            self._score_list[i] = line


class Cue(object):

    def __init__(self, parent):
        self._stack = []
        self._parent = parent
        self._translation = 0;

    def __call__(self, translate=0, scale=1):
        self._translate = translate
        return self

    def __enter__(self):
        self._stack.append(self._translate)
        self._translation = sum(self._stack)
        self._parent._prefilter_matrix.push_layer()
        self._parent._score_matrix.push_layer()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._stack.pop()
        self._translation = sum(self._stack)
        self._parent._prefilter_matrix.pop_layer()
        self._parent._score_matrix.merge_down()
        return False

    def now(self):
        return self._translation


class PythonScoreBin(PythonScore):

    def __init__(self):
        super(PythonScoreBin, self).__init__()   
        atexit.register(self._bin_end_score)

    def _bin_end_score(self):
        output = '\n'.join([' '.join(imap(str, i)) for i in self._score_list])
        with open(argv[1], 'w') as f:
        	f.write(output)
        with open('.pysco_generated_score.sco', 'w') as f:
        	f.write(output)
