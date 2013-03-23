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

from random import random

def harmonic(freq, h, dest, bend):
    if h == 0:
        h = 1
    if dest == 0:
        dest = 1

    return (freq * bend *
        int(random() * dest + 1) / float(int(random() * h + 1)))

def panner():
    pos = 1
    while True:
        yield pos / 15.0
        pos = (pos + 1) % 16

p = panner()
harmbend = 1

for t in xrange(1000):
    with cue(t * 0.075):
        freq = 200
        amp = 0.03125

        score("; voice " + str(t))
        for v in xrange(128):
            if not 20 < freq < 22050:
                break
            event_i(1, 0, 3, amp, freq, p.next())
            freq = harmonic(freq, 2, 3, harmbend)
            amp *= 0.9

        harmbend += 0.001

</CsScore>
</CsoundSynthesizer>













