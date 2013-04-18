
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
    ienv_table = p6

    aenv oscil3 1, 1 / idur, ienv_table
    a1 oscils iamp, ifreq, 0

    agate linseg 0, 0.005, 1, idur - 0.01, 1, 0.005, 0

    out a1 * aenv * agate
endin

</CsInstruments>
<CsScore bin="python">

from csd.pysco import PythonScore
from itertools import cycle
from random import random

class LinearTableEnvelope:
    table_size = 512

    def __init__(self, f_index_start, f_index_end):
        self.table_cycler = cycle(xrange(f_index_start, f_index_end))

    def __call__(self, env_data, size=False):
        if not size:
            size = self.table_size

        for index, value in enumerate(env_data):
            if index % 2:
                env_data[index] = int(round(size * value))

        table_index = self.table_cycler.next()
        L = ["f", table_index, score.cue.now(), size, 7] + env_data
        score.write(" ".join(str(i) for i in L))

        return table_index

def note(dur, amp, freq, env_data):
    score.i(1, 0, dur, amp, freq, env(env_data))

def random_env(minimum=0.0, maximum=1.0):
    counter = 0.0;
    L = [0]

    while True:
        inc = random() * (maximum - minimum) + minimum
        if counter + inc > 1.0:
            L.append(1.0 - counter)
            L.append(0)
            break
        else:
            L.append(inc)
            L.append(random())
            counter += inc
    return L

score = PythonScore()
cue = score.cue
env = LinearTableEnvelope(100, 200)
score.write('t 0 120')
freq_cycle = cycle([300, 400, 500, 600, 700])

with cue(0): note(4, 0.707, 1000, [0, 0.9, 1, 0.1, 0])
with cue(4): note(1, 0.707, 700, [0, 0.1, 1, 0.9, 0])
with cue(5): note(1, 0.707, 400, [1, 1.0, 0])
with cue(6): note(1, 0.707, 100, [0, 0.1, 1, 0.4, 1, 0.5, 0])
with cue(7):
    note(1, 0.707, 200, [0, 0.5, 1, 0.5, 0])
    note(1, 0.207, 300, [0, 0.9, 1, 0.1, 0])
    note(1, 0.207, 700, [0, 0.1, 1, 0.9, 0])
with cue(8):
    note(8, 0.2, 200, random_env(0.01, 0.05))
    for i in xrange(16):
        with cue(i * 0.5):
            note(0.5, 0.5, freq_cycle.next(), random_env(0.1, 0.3))
with cue(16): note(1, 0.407, 100, [1, 1.0, 0])
with cue(16.01): note(1, 0.307, 200, [1, 1.0, 0])

score.end()

</CsScore>
</CsoundSynthesizer>
