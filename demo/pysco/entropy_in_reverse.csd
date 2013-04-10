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

    aenv linseg	0, idur * 0.125, iamp, idur * 0.875, 0
    aosc oscils 1, ifreq, 0
    aosc = aosc * aenv
    outs aosc * sqrt(1 - ipan), aosc * sqrt(ipan)
endin

</CsInstruments>
<CsScore bin="python pysco.py">

from itertools import cycle
from random import randrange

def relative_harmonic(freq, h, dest, bend):
    return freq * bend * (randrange(dest) + 1) / (randrange(h) + 1.0)

pan = cycle(p / 15.0 for p in xrange(16))
harmbend = 1

for t in xrange(1000):
    with cue(t * 0.075):
        freq = 200
        amp = 0.03125

        for v in xrange(128):
            event_i(1, 0, 3, amp, freq, pan.next())
            freq = relative_harmonic(freq, 2, 3, harmbend)
            amp *= 0.9

            if not 20 < freq < 22050:
                break

        harmbend += 0.001

</CsScore>
</CsoundSynthesizer>
