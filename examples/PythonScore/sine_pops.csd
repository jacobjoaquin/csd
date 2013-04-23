<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 2
0dbfs = 1.0

instr 1
    p3 = p4     ; Time in seconds
    iamp = p5
    ifreq = p6
    ipan = p7

    a1 oscils iamp, ifreq, 0
    outs a1 * sqrt(ipan), a1 * sqrt(1 - ipan)
endin

</CsInstruments>
<CsScore bin="python">

from csd.pysco import PythonScoreBin
from math import log
from random import choice
from random import random
from random import uniform

def exprand(a, b):
    return a * 2 ** (log(b / float(a)) / log(2) * random())

def sine_pops(start, dur, amp, freq_min, freq_max, density):
    for i in xrange(int(density * dur)):
        freq = exprand(freq_min, freq_max)
        duration = 1 / freq
        freq *= choice([1, -1])
        time = uniform(start, start + dur)
        pan = random()
        score.i(1, time, 1, duration, uniform(0, amp), freq, pan)

score = PythonScoreBin()
sine_pops(0, 10, 0.5, 1000, 20000, 60)

</CsScore>
</CsoundSynthesizer>
