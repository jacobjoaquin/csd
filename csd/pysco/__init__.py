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

'''Python Score. Currently unstable.'''


#!/usr/bin/python
import sys
from sys import argv
from itertools import imap
from itertools import chain
import csd
import atexit

class PCallback(object):

    def __init__(self, statement, identifier, pfield, function, *args,
                 **kwargs):
        self.statement = statement
        self.identifier = identifier
        self.pfield = pfield
        self.function = function
        self.args = args
        self.kwargs = kwargs
        

class PythonScore(object):
    # TODO: 
    # Add reset()
    # Output thus far feature
    
    def __init__(self):
        self.cue = Cue(self)
        self._p_call_backs = [[]]
        self._score_list = []

    def f(self, *args):
        self._score_list.append(chain('f', args))

    def i(self, *args):
        args = list(args)

        # Apply callbacks
        for L in self._p_call_backs:
            for cb in L:
                if cb.identifier == args[0]:
                    # 'i' not yet added, so offset is necessary
                    pf = cb.pfield - 1
                    args[pf] = cb.function(args[pf], *cb.args, **cb.kwargs)

        args[1] += self.cue.now()
        self._score_list.append(chain('i', args))

    def t(self, *args):
        self._score_list.append(chain('t 0', args))

    def p_callback(self, statement, identifier, pfield, func, *args, **kwargs):
        self._p_call_backs[-1].append(PCallback(statement, identifier, pfield,
                                    func, *args, **kwargs))

    def pmap(self, statement, identifier, pfield, func, *args, **kwargs):
        if not isinstance(statement, list):
            statement = [statement]

        if not isinstance(identifier, list):
            identifier = [identifier]

        if not isinstance(pfield, list):
            pfield = [pfield]

        # Handle multiple statments, tooooo
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
        self.translation = 0;

    def __call__(self, translate=0, scale=1):
        self._translate = translate
        return self

    def __enter__(self):
        self._stack.append(self._translate)
        self._parent._p_call_backs.append([])
        self.translation = sum(self._stack)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._stack.pop()
        self._parent._p_call_backs.pop()
        self.translation = sum(self._stack)
        return False

    def now(self):
        return self.translation


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
