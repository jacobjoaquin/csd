<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 1
0dbfs = 1.0

instr 1
    idur = p3   ; Duration
    iamp = p4   ; Amplitude
    ifreq = p5  ; Frequency

    kenv line iamp, idur, 0       ; Line envelope
    a1 vco2 kenv, ifreq, 12, 0.5  ; Triangle wave
    out a1
endin

</CsInstruments>
<CsScore bin="./pysco.py">

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
        # Ugly stuff gonna happen
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
        with cue(self.parent.time):
            self.action_func(*self.args)

        self.parent.time += self.duration
        self.parent.next_node = self._select_next()


def note(dur, amp, pch):
    event_i(1, 0, dur, amp, cpspch(pch))

# Create markov object
markov = Markov()

# Create nodes and set parameters
node_0 = markov.node(1.0, note, 1.0, 1.0, 8.00)
node_1 = markov.node(0.5, note, 0.5, 1.0, 8.02)
node_2 = markov.node(1.0, note, 1.0, 1.0, 8.03)
node_3 = markov.node(0.5, note, 0.5, 1.0, 8.05)
node_4 = markov.node(1.0, note, 1.0, 1.0, 8.07)
node_5 = markov.node(1.5, note, 1.5, 1.0, 8.10)
node_6 = markov.node(1.0, note, 1.0, 1.0, 8.09)
node_7 = markov.node(0.5, note, 0.5, 1.0, 9.00)

# Connect nodes and set probablity
node_0.edge(node_1, 1)
node_1.edge(node_0, 1)
node_1.edge(node_2, 1)
node_2.edge(node_0, 1)
node_2.edge(node_3, 1)
node_3.edge(node_0, 1)
node_3.edge(node_3, 4)
node_3.edge(node_4, 1)
node_4.edge(node_5, 1)
node_5.edge(node_4, 1)
node_5.edge(node_6, 2)
node_6.edge(node_4, 1)
node_6.edge(node_7, 2)
node_7.edge(node_4, 1)
node_7.edge(node_7, 4)
node_7.edge(node_0, 2)

# Play
score('t 0 120')
markov.begin(node_0, 128)

# Change amplitude
pmap('i', 1, 4, lambda x: x * 0.707)

</CsScore>
</CsoundSynthesizer>
