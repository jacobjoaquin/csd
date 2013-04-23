<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 1
0dbfs = 1.0

instr 1
    idur = p3
    iamp = p4
    ifreq = p5

    kenv line iamp, idur, 0
    a1 vco2 kenv, ifreq, 12, 0.5
    out a1
endin

</CsInstruments>
<CsScore bin="python">

from csd.pysco import PythonScoreBin
from random import random

class Markov:
    
    def __init__(self):
        self.time = 0
        self.next_node = None
        self.duration = None

    def begin(self, node, duration):
        self.next_node = node
        self.duration = duration

        while self.time < self.duration:
            self.go()
 
    def go(self):
        if self.time < self.duration:
            self.next_node.play()

    def node(self, duration, func, *args):
        return MarkovNode(self, duration, func, *args)


class MarkovNode:

    def __init__(self, parent, duration, func, *args):
        self.duration = duration
        self.action_func = func
        self.args = args
        self.edges = []
        self.parent = parent

    def _select_next(self):
        total = 0
        table = []

        for i in self.edges:
            total += i[1]
            table.append([i[0], total])

        r = random() * total

        for i in table:
            if r < i[1]:
                return i[0]

    def action(self, func):
        self.action_func = func

    def edge(self, n, odds):
        self.edges.append([n, odds])

    def play(self):
        with score.cue(self.parent.time):
            self.action_func(*self.args)

        self.parent.time += self.duration
        self.parent.next_node = self._select_next()

def cpspch(p):
    octave, note = divmod(p, 1)
    return 440 * 2 ** (((octave - 8) * 12 + ((note * 100) - 9)) / 12.0)

def note(dur, amp, pch):
    score.i(1, 0, dur, amp * 0.707, cpspch(pch))

# Create markov object
markov = Markov()

# Create nodes and set parameters
state_0 = markov.node(1.0, note, 1.0, 1.0, 8.00)
state_1 = markov.node(0.5, note, 0.5, 1.0, 8.02)
state_2 = markov.node(1.0, note, 1.0, 1.0, 8.03)
state_3 = markov.node(0.5, note, 0.5, 1.0, 8.05)
state_4 = markov.node(1.0, note, 1.0, 1.0, 8.07)
state_5 = markov.node(1.5, note, 1.5, 1.0, 8.10)
state_6 = markov.node(1.0, note, 1.0, 1.0, 8.09)
state_7 = markov.node(0.5, note, 0.5, 1.0, 9.00)

# Connect nodes and set probability
state_0.edge(state_1, 1)
state_1.edge(state_0, 1)
state_1.edge(state_2, 1)
state_2.edge(state_0, 1)
state_2.edge(state_3, 1)
state_3.edge(state_0, 1)
state_3.edge(state_3, 4)
state_3.edge(state_4, 1)
state_4.edge(state_5, 1)
state_5.edge(state_4, 1)
state_5.edge(state_6, 2)
state_6.edge(state_4, 1)
state_6.edge(state_7, 2)
state_7.edge(state_4, 1)
state_7.edge(state_7, 4)
state_7.edge(state_0, 2)

# Score
score = PythonScoreBin()
score.t(120)
markov.begin(state_0, 128)

</CsScore>
</CsoundSynthesizer>
