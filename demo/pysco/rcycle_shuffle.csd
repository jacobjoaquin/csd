<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 2
0dbfs = 1.0

instr 1
    idur = p3   ; Duration
    iamp = p4   ; Amplitude
    ifreq = p5  ; Frequency
    ipan = p6   ; Pan

    kenv line iamp, idur, 0
    a1 vco2 kenv, ifreq, 12, 0.5
    outs a1 * sqrt(ipan), a1 * sqrt(1 - ipan)
endin

instr 2
    idur = p3   ; Duration
    iamp = p4   ; Amplitude
    ifreq = p5  ; Frequency
    ipan = p6   ; Pan

    kenv line 1, idur, 0
    a2 oscils 1, 1, 0.25
    a1 repluck 0.9, kenv, ifreq, 0.5, 0.1, a2
    a1 limit a1, -1, 1
    aenv linseg 0, 0.005, 1, idur - 0.01, 1, 0.005, 0
    a1 = a1 * aenv * iamp
    outs a1 * sqrt(ipan), a1 * sqrt(1 - ipan)
endin

</CsInstruments>
<CsScore bin="python pysco.py">

from math import sin
from math import pi
from random import choice
from random import random
from types import GeneratorType

def swing_it(x):
    int, frac = divmod(x, 1)
    return int + sin(frac * (pi / 2.0))

def rcycle(values):
    pos = 0
    while True:
        v = values[pos]
        if isinstance(v, GeneratorType):
            yield v.next()
        else:
            yield v
        pos = (pos + 1) % len(values)  

bass = rcycle([6.02, 7.02, rcycle([6.02, 6.09, 5.09]), 6.00]);
melody = rcycle([8.04, 8.02, 8.05, 8.11, 8.09,
                 rcycle([8.04, 8.02, 8.05, 8.11, 8.09])]);
rhythm = rcycle([1, 0.5, 0.5,
                 rcycle([1, 1, 0.5, 1, 0.5, 1.5, 1.0, 0.5])]);

score('t 0 144')
score_duration = 256

# Generate Bassline
for t in range(0, score_duration, 64):
    with cue(t):
        with cue(0):
            for i in range(32):
                with cue(i):
                    event_i(1, 0, 1, 0.3, cpspch(bass.next()), 0.5)

        with cue(32):
            for i in range(0, 32, 2):
                with cue(i):
                    event_i(1, 0, 1, 0.3, cpspch(bass.next()), 0.5)

with cue(score_duration):
    event_i(1, 0, 4, 0.3, cpspch(bass.next()), 0.5)

# Generate Melody
counter = 0
while counter < score_duration:
    with cue(counter):
        freq = cpspch(melody.next())
        r = rhythm.next()
        duration = r * choice([1, 1, 0.5, 1.5])
        for i in range(4):
            f = freq * (0.99 + random() * 0.02)
            event_i(2, 0, duration, 0.15, f, random())
        counter += r

with cue(score_duration):
    freq = cpspch(melody.next())
    for i in range(4):
        f = freq * (0.99 + random() * 0.02)
        event_i(2, 0, 4, 0.15, f, random())

pmap('i', 2, 2, swing_it)

</CsScore>
</CsoundSynthesizer>
