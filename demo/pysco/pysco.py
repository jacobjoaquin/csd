#!/usr/bin/python
import inspect
import sys
from sys import argv
from itertools import imap
from itertools import chain
from convert import *
import csd
from csd import sco


class PCallback():

    def __init__(self, statement, identifier, pfield, function, *args,
                 **kwargs):
        self.statement = statement
        self.identifier = identifier
        self.pfield = pfield
        self.function = function
        self.args = args
        self.kwargs = kwargs
        

class Slipmat():

    def __init__(self):
        self.slipcue = Slipcue(self)
        self.score_data = []
        self.p_callbacks = [[]]

    def _map_process(self, data, statement, identifier, pfield, function,
                     *args, **kwargs):
        convert_numeric = True
        sco_statements_enabled = True

        # Convert pfield to list if it isn't one
        if not isinstance(pfield, list):
            pfield = [pfield]

        selection = sco.select(data, {0: statement, 1: identifier})

        for k, v in selection.iteritems():
            for p in pfield:
                element = sco.event.get(v, p)

                # Bypass if score statement like carry
                # TODO: ^+x, npx, ppx, etc...
                if sco_statements_enabled and element in ['.', '+', '<', '!']:
                    break

                # Convert value to float
                if convert_numeric:
                    try:
                        element = float(element)
                    except Exception:
                        pass

                deez_args = (element,) + args
                selection[k] = sco.event.set(v, p,
                                             function(*deez_args, **kwargs))

        return sco.merge(data, selection)

    def end_score(self):
        # TODO: This shouldn't run under certain circumstances
    	with open(argv[1], 'w') as f:
    		f.write("\n".join(self.score_data))

    def event_i(self, *args):
        self.score(' '.join(chain('i', imap(str, args)))) 

    def p_callback(self, statement, identifier, pfield, func, *args, **kwargs):
        self.p_callbacks[-1].append(PCallback(statement, identifier, pfield,
                                    func, *args, **kwargs))

    def pmap(self, statement, identifier, pfield, func, *args, **kwargs):
        data = "\n".join(self.score_data)
        self.score_data = [self._map_process(data, statement, identifier,
                           pfield, func, *args, **kwargs)]

    def score(self, data):
        # Apply pfield callbacks
        for L in self.p_callbacks:
            for cb in L:
                data = self._map_process(data, cb.statement, cb.identifier,
                                         cb.pfield, cb.function, *cb.args,
                                         **cb.kwargs)

        # Apply time stack
        selected = sco.select(data, {0: 'i'})
        op = sco.selection.operate_numeric(selected, 2,
                                           lambda x: x + self.slipcue.now())
        self.score_data.append(sco.merge(data, op))


class Slipcue(object):

    def __init__(self, parent):
        self.stack = []
        self.parent = parent

    def __call__(self, when):
        self.when = when
        return self

    def __enter__(self):
        self.stack.append(self.when)
        self.parent.p_callbacks.append([])
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stack.pop()
        self.parent.p_callbacks.pop()
        return False

    def now(self):
        return sum(self.stack)


def debug(m, v=''):
    print m + ': ' + str(v) + "\n",

# Globals
slipmat = Slipmat()
cue = slipmat.slipcue
score = slipmat.score
pmap = slipmat.pmap
p_callback = slipmat.p_callback
event_i = slipmat.event_i
end = slipmat.end_score

def begin():
    global slipmat
    f = sys._current_frames().values()[0]
    name = f.f_back.f_globals['__name__']
    m = sys.modules[name]
    setattr(m, 'score', slipmat.score)
    setattr(m, 'score_data', slipmat.score_data)
    setattr(m, 'cue', slipmat.slipcue)
    setattr(m, 'pmap', slipmat.pmap)
    setattr(m, 'p_callback', slipmat.p_callback)
    setattr(m, 'event_i', slipmat.event_i)
    setattr(m, 'end', slipmat.end_score)

def main():
    # Execute CsScore
    execfile(argv[1], globals())

    # Create score string
    sco_output = "\n".join(slipmat.score_data)

    # Write score used by Csound
    with open(argv[2], 'w') as f:
        f.write(sco_output)

    # Additional file for development testing
    with open('_pysco.sco', 'w') as f:
        f.write(sco_output)

if __name__ == '__main__':
    main()
