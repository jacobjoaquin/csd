<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 4410
ksmps = 10
nchnls = 1
0dbfs = 1.0

sr = 44100
kr = 44100
ksmps = 1
nchnls = 2

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

duration = 3
amp = 0.03125
ampslope = 0.9
freq = 200
pan = 0.5
voices = 128
harmmin = 2
harmmax = 3
harmbend = 1

event_i(1, 0, 0.2, 0.707, 440, 0.5)
p = panner()

for t in xrange(3):
    with cue(t * 0.075):
        f = freq
        a = amp

        for v in xrange(voices):
            if not 20 < f < 22050:
                break

            f = harmonic(f, harmmin, harmmax, harmbend)

            event_i(1, 0, duration, a, f, p.next())
            a *= ampslope

</CsScore>
</CsoundSynthesizer>













