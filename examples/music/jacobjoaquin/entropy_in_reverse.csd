Entropy In Reverse
by Jacob Joaquin
jacobjoaquin@gmail.com
@jacobjoaquin

<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 4410
ksmps = 10
nchnls = 1
0dbfs = 1.0

instr 1
    idur = p3
    iamp = p4
    ifreq = p5
    ipan = p6

    aenv linseg 0, idur * 0.125, iamp, idur * 0.875, 0
    aosc oscils 1, ifreq, 0
    aosc = aosc * aenv
    outs aosc * sqrt(1 - ipan), aosc * sqrt(ipan)
endin

</CsInstruments>
<CsScore bin="python">

from csd.pysco import PythonScoreBin
from itertools import cycle
from random import randrange

def relative_harmonic(freq, relative, dest, bend):
    return freq * bend * (randrange(dest) + 1) / (randrange(relative) + 1.0)

def tone(amp, freq, pan):
    score.i(1, 0, 3, amp, freq, pan)

def harmonic_bend(start, inc):
    while True:
        yield start
        start += inc

score = PythonScoreBin()
n_clusters = 1000
harmbend = harmonic_bend(1, 1.0 / n_clusters)
pan = cycle(p / 15.0 for p in xrange(16))

for time in xrange(n_clusters):
    with score.cue(time * 0.075):
        freq = 200
        amp = 0.03125
        bend = harmbend.next()

        for v in xrange(128):
            tone(amp, freq, pan.next())
            freq = relative_harmonic(freq, 2, 3, bend)
            amp *= 0.9

            if not 20 < freq < 22050:
                break

</CsScore>
</CsoundSynthesizer>
