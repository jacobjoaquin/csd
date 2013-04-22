
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
'''Arbitrary number of envelope segments in an instrument event.'''

from csd.pysco import PythonScoreBin
from itertools import cycle

class LinearTableEnvelope:
    table_size = 512

    def __init__(self, f_index_start, f_index_end):
        self.table_cycler = cycle(xrange(f_index_start, f_index_end))

    def __call__(self, env_data, size=False):
        if not size:
            size = self.table_size

        ftable_index = self.table_cycler.next()
        ftable = [ftable_index, score.cue.now(), size, -7]

        for index, value in enumerate(env_data):
            if index % 2:
                value = int(round(size * value))
            ftable.append(value)
            
        score.f(*ftable) 
        return ftable_index

def note(dur, amp, freq, env_data):
    score.i(1, 0, dur, amp, freq, env(env_data))

score = PythonScoreBin()
cue = score.cue
env = LinearTableEnvelope(100, 120)

score.t(120)
with cue(0): note(2, 0.707, 220, [1, 1, 0])
with cue(2): note(2, 0.707, 440, [0, 0.1, 1, 0.9, 0])
with cue(4): note(2, 0.707, 660, [0, 0.1, 1, 0.2, 0.3, 0.7, 0])
with cue(6): note(2, 0.707, 880, [0, 0.1, 1, 0.2, 0.3, 0.4, 0.3, 0.3, 0])

</CsScore>
</CsoundSynthesizer>
