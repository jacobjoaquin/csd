<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 2
0dbfs = 1.0

; Uses one of the millions of Amen loops by the Winstons. Originally, that is.
gS_loop = "Amenbreak.aif"
gisr filesr gS_loop
gilength filelen gS_loop
gibeats = 64 

instr 1
    p3 = 0.13
    iamp = p4
    ibeat = p5
    ipos = ((ibeat / gibeats) * gilength)

    aenv linseg iamp, p3 * 0.85, iamp, p3 * 0.15, 0
    a1, a2 diskin2 gS_loop, 1.5, ipos
    out a1 * aenv, a2 * aenv
endin

</CsInstruments>
<CsScore bin="./pysco.py">

# Import choice from python library
from random import choice
from random import random

# Create wrapper functions for instruments.
def kick(amp=1):
    event_i(1, 0, 1, amp, choice([0, 0.5, 4, 8, 16]))

def snare(amp=1):
    event_i(1, 0, 1, amp, choice([1, 5, 9, 11.5]))

def hat(amp=1):
    event_i(1, 0, 1, amp, choice([3.5, 7.5, 10, 11, 19.5]))


class Markov:
    
    def __init__(self):
        self.time = 0
        self.next_node = None
        self.duration = None

    def begin(self, node, duration):
        self.next_node = node
        self.duration = duration
        self.go()
 
    def go(self):
        if self.time < self.duration:
            self.next_node.play()

    def node(self):
        return MarkovNode(self)


class MarkovNode:

    def __init__(self, parent):
        self.duration = None
        self.action_func = None
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
            self.action_func()

        self.parent.time += self.duration
        self.parent.next_node = self._select_next()
        self.parent.go()


markov = Markov()
node = markov.node()
node_2 = markov.node()
node_3 = markov.node()

node.duration = 0.5
node.action(kick)
node.edge(node, 1)
node.edge(node_2, 1)
node.edge(node_3, 1)
 
node_2.duration = 0.5
node_2.action(snare)
node_2.edge(node, 1)
node_2.edge(node_2, 1)
node_2.edge(node_3, 1)

node_3.duration = 0.25
node_3.action(hat)
node_3.edge(node, 1)
node_3.edge(node_2, 1)
node_3.edge(node_3, 1)

markov.begin(node, 128)

score('t 0 170')

pmap('i', 1, 4, lambda x: x * 0.707)

</CsScore>
</CsoundSynthesizer>
