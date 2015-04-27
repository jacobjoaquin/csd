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


import atexit
from sys import argv
from collections import namedtuple
from csd.sco.event import get_pfield_list


class StackMatrix:
    '''It's a stack. It's a Matrix.  It's a stack-matrix.'''
    
    def __init__(self):
        self._layers = [[]]

    def push_matrix(self):
        self._layers.append([])

    def pop_matrix(self, append=False):
        layer = self._layers.pop() 
        if append:
            self._layers[-1] += layer
        return layer

    def replace_layer(self, item):
        self._layers[-1] = item

    def push(self, item):
        self._layers[-1].append(item) 
        
    def pop(self):
        return self._layers[-1].pop()

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
        return iter(self._flatten_list(self._layers))

    def itercurrent(self):
        return iter(self._layers[-1])


class PythonScore(object):
    # TODO: 
    # Add reset()
    # Output thus far feature
   
    def __init__(self):
        self.cue = Cue(self)
        self._prefilter_matrix = StackMatrix()
        self._score_matrix = StackMatrix()

    def f(self, *args):
        '''Input an f-table function'''

        self._insert_time_event('f', *args)

    def i(self, *args):
        '''Input an i-event'''

        self._insert_time_event('i', *args)

    def t(self, *args):
        '''Input a t-event'''

        self._score_matrix.push(['t', 0] + list(args))

    def prefilter(self, statement, identifier, pfield, func, *args, **kwargs):
        '''Push a score data function onto the current prefilter matrix'''

        self._prefilter_matrix.push(
            _Filter(statement, identifier, pfield, func, args, kwargs)
        )

    def postfilter(self, statement, identifier, pfield, func, *args, **kwargs):
        '''Filter the score data in the current layer of the score matrix'''

        if not isinstance(statement, list):
            statement = [statement]

        if not isinstance(identifier, list):
            identifier = [identifier]

        if not isinstance(pfield, list):
            pfield = [pfield]

        # TODO: Is there an iterable solution here?
        this_layer = list(self._score_matrix.itercurrent())
        for i, line in enumerate(this_layer):
            if line[0] in statement and line[1] in identifier:
                for pf in pfield:
                    line[pf] = func(line[pf], *args, **kwargs)
            this_layer[i] = line
        self._score_matrix.replace_layer(this_layer)

    def make_score(self):
        '''Convert the score data into a classical Csound score'''

        return '\n'.join(' '.join(map(str, i))
                          for i in self._score_matrix.pop_matrix())

    def write(self, score_input):
        '''Converts a classical Csound score string to PythonScore data'''

        output = []
        for line in [L.strip() for L in score_input.splitlines() if L.strip()]:
            event = get_pfield_list(line)
            if event[0] in ('i', 'f'):
                event[2] = float(event[2]) + self.cue.now()
            self._score_matrix.push(pf for pf in event)

    def _apply_prefilter(self, statement, args):
        for f in [the_filter for the_filter in self._prefilter_matrix.iterall()
                  if the_filter[0] == statement]:
            args[f.pfield] = f[3](args[f.pfield], *f[4], **f[5])

    def _insert_time_event(self, statement, *args):
        pfields = [statement] + list(args)

        for f in [the_filter for the_filter in self._prefilter_matrix.iterall()
                  if the_filter[0] == statement]:
            pfields[f.pfield] = f[3](pfields[f.pfield], *f[4], **f[5])
        pfields[2] += self.cue.now()
        self._score_matrix.push(pfields)


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
        self._parent._prefilter_matrix.push_matrix()
        self._parent._score_matrix.push_matrix()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._stack.pop()
        self._translation = sum(self._stack)
        self._parent._prefilter_matrix.pop_matrix()
        self._parent._score_matrix.pop_matrix(append=True)
        return False

    def now(self):
        return self._translation


class PythonScoreBin(PythonScore):

    def __init__(self):
        super(PythonScoreBin, self).__init__()   
        atexit.register(self._bin_end_score)

    def _bin_end_score(self):
        output = self.make_score() 
        with open(argv[1], 'w') as f:
        	f.write(output)
        with open('.pysco_generated_score.sco', 'w') as f:
        	f.write(output)
            

_Filter = namedtuple('Filter', [
    'statement', 'identifier', 'pfield', 'function', 'args', 'kwargs'])
