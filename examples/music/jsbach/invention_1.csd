<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 2
0dbfs = 1.0

instr 1
    p3 = p3 + 0.125
    idur = p3
    iamp = p4
    ifreq = p5

    kenv adsr 0.11, 0.125, 0.4, 1
    ;kenv adsr 0.05, 0.05, 0.2, 1
    ;kenv linseg 1, 0.1, 0.4, idur - (0.1 + 0.125), 0.2, 0.125, 0, 0, 0
    a1 vco2 1, ifreq * 2, 0 
    a2 vco2 1, ifreq, 2, 0.6 + birnd(0.1)

    kenv2 expseg 16000 + rnd(2000), idur, 8000 + rnd(3000)
    kenv3 expseg 15000 + rnd(2000), idur, 8000 + rnd(3000)

    amix = a1 * 0.4 + a2 + 0.6
    amix = amix * kenv * iamp

    ;afilter1 moogladder amix, kenv2, 0.4 + rnd(0.1)
    ;afilter2 moogladder amix, kenv3, 0.4 + rnd(0.1)
    afilter1 moogvcf2 amix, kenv2, 0.5 + rnd(0.1)
    afilter2 moogvcf2 amix, kenv3, 0.5 + rnd(0.1)

    outs afilter1, afilter2

    chnmix afilter1, "left"
    chnmix afilter2, "right"
endin

instr 2
    imix = 2.5
    a1 chnget "left"
    a2 chnget "right"

    a1 delay a1, 0.0233
    a2 delay a2, 0.0231

    a1, a2 freeverb a2, a1, 0.4, 0.3
    outs a1 * imix, a2 * imix

    chnclear "left"
    chnclear "right"
endin

</CsInstruments>
<CsScore bin="python">

from csd.pysco import PythonScore
from random import random

score = PythonScore()
cue = score.cue

# Invention No. 1 (excerpt) by J.S. Bach

def measure(t):
    return cue((t - 1) * 4.0)

def harpsichord(dur, pitch):
    score.i(1, 0, dur, 0.5, well_temper(pitch))

def well_temper(p):
    '''Well Tempered

    # http://www.larips.com/
    '''

    well_tempered = [5.9, 3.9, 2, 3.9, -2, 7.8, 2, 3.9, 3.9, 0, 3.9, 0]
    octave, note = divmod(p, 1)
    note *= 100
    et = 432 * 2 ** (((octave - 8) * 12 + (note - 9)) / 12.0)
    et *= 2 ** ((well_tempered[int(note)]) / 1200.0)
    return et

treble = harpsichord
bass = harpsichord

#score.write('t 0 90')

# Broke Baroque Tempp
L = []
counter = 0
while counter < 60:
    L.append(str(counter))
    L.append(str(85 + (random() * 2.0 - 1.0) * 5)) 
    counter += random() * 3.0 + 1.0

score.write("t" + " ".join(L))

with measure(1):
    with cue(0.25): treble(0.25, 8.00)
    with cue(0.50): treble(0.25, 8.02)
    with cue(0.75): treble(0.25, 8.04)
    with cue(1.00): treble(0.25, 8.05)
    with cue(1.25): treble(0.25, 8.02)
    with cue(1.50): treble(0.25, 8.04)
    with cue(1.75): treble(0.25, 8.00)
    with cue(2.00): treble(0.5, 8.07)
    with cue(2.50): treble(0.5, 9.00)
    with cue(3.00): treble(0.125, 8.11)
    with cue(3.125): treble(0.125, 8.09)
    with cue(3.25): treble(0.25, 8.11)
    with cue(3.50): treble(0.5, 9.00)

    with cue(2.25): bass(0.25, 7.00)
    with cue(2.50): bass(0.25, 7.02)
    with cue(2.75): bass(0.25, 7.04)
    with cue(3.00): bass(0.25, 7.05)
    with cue(3.25): bass(0.25, 7.02)
    with cue(3.50): bass(0.25, 7.04)
    with cue(3.75): bass(0.25, 7.00)

with measure(2):
    with cue(0.00): treble(0.25, 9.02)
    with cue(0.25): treble(0.25, 8.07)
    with cue(0.50): treble(0.25, 8.09)
    with cue(0.75): treble(0.25, 8.11)
    with cue(1.00): treble(0.25, 9.00)
    with cue(1.25): treble(0.25, 8.09)
    with cue(1.50): treble(0.25, 8.11)
    with cue(1.75): treble(0.25, 8.07)
    with cue(2.00): treble(0.5, 9.02)
    with cue(2.50): treble(0.5, 9.07)
    with cue(3.00): treble(0.125, 9.05)
    with cue(3.125): treble(0.125, 9.04)
    with cue(3.25): treble(0.25, 9.05)
    with cue(3.50): treble(0.5, 9.07)

    with cue(0.00): bass(0.5, 7.07)
    with cue(0.50): bass(0.5, 6.07)
    with cue(2.25): bass(0.25, 7.07)
    with cue(2.50): bass(0.25, 7.09)
    with cue(2.75): bass(0.25, 7.11)
    with cue(3.00): bass(0.25, 8.00)
    with cue(3.25): bass(0.25, 7.09)
    with cue(3.50): bass(0.25, 7.11)
    with cue(3.75): bass(0.25, 7.07)

with measure(3):
    with cue(0.00): treble(0.25, 9.04)
    with cue(0.25): treble(0.25, 9.09)
    with cue(0.50): treble(0.25, 9.07)
    with cue(0.75): treble(0.25, 9.05)
    with cue(1.00): treble(0.25, 9.04)
    with cue(1.25): treble(0.25, 9.07)
    with cue(1.50): treble(0.25, 9.05)
    with cue(1.75): treble(0.25, 9.09)
    with cue(2.00): treble(0.25, 9.07)
    with cue(2.25): treble(0.25, 9.05)
    with cue(2.50): treble(0.25, 9.04)
    with cue(2.75): treble(0.25, 9.02)
    with cue(3.00): treble(0.25, 9.00)
    with cue(3.25): treble(0.25, 9.04)
    with cue(3.50): treble(0.25, 9.02)
    with cue(3.75): treble(0.25, 9.05)

    with cue(0.00): bass(0.5, 8.00)
    with cue(0.50): bass(0.5, 7.11)
    with cue(1.00): bass(0.5, 8.00)
    with cue(1.50): bass(0.5, 8.02)
    with cue(2.00): bass(0.5, 8.04)
    with cue(2.50): bass(0.5, 7.07)
    with cue(3.00): bass(0.5, 7.09)
    with cue(3.50): bass(0.5, 7.11)

with measure(4):
    with cue(0.00): treble(0.25, 9.04)
    with cue(0.25): treble(0.25, 9.02)
    with cue(0.50): treble(0.25, 9.00)
    with cue(0.75): treble(0.25, 8.11)
    with cue(1.00): treble(0.25, 8.09)
    with cue(1.25): treble(0.25, 9.00)
    with cue(1.50): treble(0.25, 8.11)
    with cue(1.75): treble(0.25, 9.02)
    with cue(2.00): treble(0.25, 9.00)
    with cue(2.25): treble(0.25, 8.11)
    with cue(2.50): treble(0.25, 8.09)
    with cue(2.75): treble(0.25, 8.07)
    with cue(3.00): treble(0.25, 8.06)
    with cue(3.25): treble(0.25, 8.09)
    with cue(3.50): treble(0.25, 8.07)
    with cue(3.75): treble(0.25, 8.11)

    with cue(0.00): bass(0.5, 8.00)
    with cue(0.50): bass(0.5, 7.04)
    with cue(1.00): bass(0.5, 7.06)
    with cue(1.50): bass(0.5, 7.07)
    with cue(2.00): bass(0.5, 7.09)
    with cue(2.50): bass(0.5, 7.11)
    with cue(3.00): bass(1.25, 8.00)

with measure(5):
    with cue(0.00): treble(0.5, 8.09)
    with cue(0.50): treble(0.5, 8.02)
    with cue(1.00): treble(0.125, 9.00)
    with cue(1.125): treble(0.125, 8.11)
    with cue(1.25): treble(0.5, 9.00)
    with cue(1.75): treble(0.25, 9.02)
    with cue(2.00): treble(0.25, 8.11)
    with cue(2.25): treble(0.25, 8.09)
    with cue(2.50): treble(0.25, 8.07)
    with cue(2.75): treble(0.25, 8.06)
    with cue(3.00): treble(0.25, 8.04)
    with cue(3.25): treble(0.25, 8.07)
    with cue(3.50): treble(0.25, 8.06)
    with cue(3.75): treble(0.25, 8.09)

    with cue(0.25): bass(0.25, 7.02)
    with cue(0.50): bass(0.25, 7.04)
    with cue(0.75): bass(0.25, 7.06)
    with cue(1.00): bass(0.25, 7.07)
    with cue(1.25): bass(0.25, 7.04)
    with cue(1.50): bass(0.25, 7.06)
    with cue(1.75): bass(0.25, 7.02)
    with cue(2.00): bass(0.5, 7.07)
    with cue(2.50): bass(0.5, 6.11)
    with cue(3.00): bass(0.5, 7.00)
    with cue(3.50): bass(0.5, 7.02)

with measure(6):
    with cue(0.00): treble(0.25, 8.07)
    with cue(0.25): treble(0.25, 8.11)
    with cue(0.50): treble(0.25, 8.09)
    with cue(0.75): treble(0.25, 9.00)
    with cue(1.00): treble(0.25, 8.11)
    with cue(1.25): treble(0.25, 9.02)
    with cue(1.50): treble(0.25, 9.00)
    with cue(1.75): treble(0.25, 9.04)
    with cue(2.00): treble(0.25, 9.02)
    with cue(2.25): treble(0.125, 8.11)
    with cue(2.375): treble(0.125, 9.00)
    with cue(2.50): treble(0.25, 9.02)
    with cue(2.75): treble(0.25, 9.07)
    with cue(3.00): treble(0.125, 8.11)
    with cue(3.125): treble(0.125, 8.09)
    with cue(3.25): treble(0.25, 8.11)
    with cue(3.50): treble(0.25, 8.09)
    with cue(3.75): treble(0.25, 8.07)

    with cue(0.00): bass(0.5, 7.04)
    with cue(0.50): bass(0.5, 7.06)
    with cue(1.00): bass(0.5, 7.07)
    with cue(1.50): bass(0.5, 7.04)
    with cue(2.00): bass(0.75, 6.11)
    with cue(2.75): bass(0.25, 7.00)
    with cue(3.00): bass(0.5, 7.02)
    with cue(3.50): bass(0.5, 6.02)    

with measure(7):
    with cue(0.00): treble(0.5, 8.07)
    with cue(2.25): treble(0.25, 8.07)
    with cue(2.50): treble(0.25, 8.09)
    with cue(2.75): treble(0.25, 8.11)
    with cue(3.00): treble(0.25, 9.00)
    with cue(3.25): treble(0.25, 8.09)
    with cue(3.50): treble(0.25, 8.11)
    with cue(3.75): treble(0.25, 8.07)

    with cue(0.25): bass(0.25, 6.07)
    with cue(0.50): bass(0.25, 6.09)
    with cue(0.75): bass(0.25, 6.11)
    with cue(1.00): bass(0.25, 7.00)
    with cue(1.25): bass(0.25, 6.09)
    with cue(1.50): bass(0.25, 6.11)
    with cue(1.75): bass(0.25, 6.07)
    with cue(2.00): bass(0.5, 7.02)
    with cue(2.50): bass(0.5, 7.07)
    with cue(3.00): bass(0.5, 7.06)
    with cue(3.50): bass(0.5, 7.07)

with measure(8):
    with cue(0.00): treble(0.125, 8.06)
    with cue(0.125): treble(0.125, 8.04)
    with cue(0.25): treble(0.25, 8.06)
    with cue(2.25): treble(0.25, 8.09)
    with cue(2.50): treble(0.25, 8.11)
    with cue(2.75): treble(0.25, 9.00)
    with cue(3.00): treble(0.25, 9.02)
    with cue(3.25): treble(0.25, 8.11)
    with cue(3.50): treble(0.25, 9.00)
    with cue(3.75): treble(0.25, 8.09)

    with cue(0.00): bass(0.25, 7.09)
    with cue(0.25): bass(0.25, 7.02)
    with cue(0.50): bass(0.25, 7.04)
    with cue(0.75): bass(0.25, 7.06)
    with cue(1.00): bass(0.25, 7.07)
    with cue(1.25): bass(0.25, 7.04)
    with cue(1.50): bass(0.25, 7.06)
    with cue(1.75): bass(0.25, 7.02)
    with cue(2.00): bass(0.5, 7.09)
    with cue(2.50): bass(0.5, 8.02)
    with cue(3.00): bass(0.5, 8.00)
    with cue(3.50): bass(0.5, 8.02)

with measure(9):
    with cue(0.00): treble(0.5, 8.11)
    with cue(2.25): treble(0.25, 9.02)
    with cue(2.50): treble(0.25, 9.00)
    with cue(2.75): treble(0.25, 8.11)
    with cue(3.00): treble(0.25, 8.09)
    with cue(3.25): treble(0.25, 9.00)
    with cue(3.50): treble(0.25, 8.11)
    with cue(3.75): treble(0.25, 9.02)

    with cue(0.00): bass(0.25, 7.07)
    with cue(0.25): bass(0.25, 8.07)
    with cue(0.50): bass(0.25, 8.05)
    with cue(0.75): bass(0.25, 8.04)
    with cue(1.00): bass(0.25, 8.02)
    with cue(1.25): bass(0.25, 8.05)
    with cue(1.50): bass(0.25, 8.04)
    with cue(1.75): bass(0.25, 8.07)
    with cue(2.00): bass(0.5, 8.05)
    with cue(2.50): bass(0.5, 8.04)
    with cue(3.00): bass(0.5, 8.05)
    with cue(3.50): bass(0.5, 8.02)

with measure(10):
    with cue(0.00): treble(0.5, 9.00)
    with cue(2.25): treble(0.25, 9.04)
    with cue(2.50): treble(0.25, 9.02)
    with cue(2.75): treble(0.25, 9.00)
    with cue(3.00): treble(0.25, 8.11)
    with cue(3.25): treble(0.25, 9.02)
    with cue(3.50): treble(0.25, 9.01)
    with cue(3.75): treble(0.25, 9.04)

    with cue(0.00): bass(0.25, 8.04)
    with cue(0.25): bass(0.25, 8.09)
    with cue(0.50): bass(0.25, 8.07)
    with cue(0.75): bass(0.25, 8.05)
    with cue(1.00): bass(0.25, 8.04)
    with cue(1.25): bass(0.25, 8.07)
    with cue(1.50): bass(0.25, 8.05)
    with cue(1.75): bass(0.25, 8.09)
    with cue(2.00): bass(0.5, 8.07)
    with cue(2.50): bass(0.5, 8.05)
    with cue(3.00): bass(0.5, 8.07)
    with cue(3.50): bass(0.5, 8.04)

with measure(11):
    with cue(0.00): treble(0.5, 9.02)
    with cue(0.50): treble(0.5, 9.01)
    with cue(1.00): treble(0.5, 9.02)
    with cue(1.50): treble(0.5, 9.04)
    with cue(2.00): treble(0.5, 9.05)
    with cue(2.50): treble(0.5, 8.09)
    with cue(3.00): treble(0.5, 8.11)
    with cue(3.50): treble(0.5, 9.01)

    with cue(0.00): bass(0.25, 8.05)
    with cue(0.25): bass(0.25, 8.10)
    with cue(0.50): bass(0.25, 8.09)
    with cue(0.75): bass(0.25, 8.07)
    with cue(1.00): bass(0.25, 8.05)
    with cue(1.25): bass(0.25, 8.09)
    with cue(1.50): bass(0.25, 8.07)
    with cue(1.75): bass(0.25, 8.10)
    with cue(2.00): bass(0.25, 8.09)
    with cue(2.25): bass(0.25, 8.07)
    with cue(2.50): bass(0.25, 8.05)
    with cue(2.75): bass(0.25, 8.04)
    with cue(3.00): bass(0.25, 8.02)
    with cue(3.25): bass(0.25, 8.05)
    with cue(3.50): bass(0.25, 8.04)
    with cue(3.75): bass(0.25, 8.07)

with measure(12):
    with cue(0.00): treble(0.5, 9.02)
    with cue(0.50): treble(0.5, 8.06)
    with cue(1.00): treble(0.5, 8.08)
    with cue(1.50): treble(0.5, 8.09)
    with cue(2.00): treble(0.5, 8.11)
    with cue(2.50): treble(0.5, 9.00)
    with cue(3.00): treble(1.25, 9.02)

    with cue(0.00): bass(0.25, 8.05)
    with cue(0.25): bass(0.25, 8.04)
    with cue(0.50): bass(0.25, 8.02)
    with cue(0.75): bass(0.25, 8.00)
    with cue(1.00): bass(0.25, 7.11)
    with cue(1.25): bass(0.25, 8.02)
    with cue(1.50): bass(0.25, 8.00)
    with cue(1.75): bass(0.25, 8.04)
    with cue(2.00): bass(0.25, 8.02)
    with cue(2.25): bass(0.25, 8.00)
    with cue(2.50): bass(0.25, 7.11)
    with cue(2.75): bass(0.25, 7.09)
    with cue(3.00): bass(0.25, 7.08)
    with cue(3.25): bass(0.25, 7.11)
    with cue(3.50): bass(0.25, 7.09)
    with cue(3.75): bass(0.25, 8.00)

with measure(13):
    with cue(0.25): treble(0.25, 8.04)
    with cue(0.50): treble(0.25, 8.06)
    with cue(0.75): treble(0.25, 8.08)
    with cue(1.00): treble(0.25, 8.09)
    with cue(1.25): treble(0.25, 8.06)
    with cue(1.50): treble(0.25, 8.08)
    with cue(1.75): treble(0.25, 8.04)
    with cue(2.00): treble(0.25, 9.04)
    with cue(2.25): treble(0.25, 9.02)
    with cue(2.50): treble(0.25, 9.00)
    with cue(2.75): treble(0.25, 9.04)
    with cue(3.00): treble(0.25, 9.02)
    with cue(3.25): treble(0.25, 9.00)
    with cue(3.50): treble(0.25, 8.11)
    with cue(3.75): treble(0.25, 9.02)
   
    with cue(0.00): bass(0.5, 7.11)
    with cue(0.50): bass(0.5, 7.04)
    with cue(1.00): bass(0.125, 8.02)
    with cue(1.125): bass(0.125, 8.04)
    with cue(1.25): bass(0.5, 8.02)
    with cue(1.75): bass(0.25, 8.04)
    with cue(2.00): bass(0.25, 8.00)
    with cue(2.25): bass(0.25, 7.11)
    with cue(2.50): bass(0.25, 7.09)
    with cue(2.75): bass(0.25, 7.07)
    with cue(3.00): bass(0.25, 7.06)
    with cue(3.25): bass(0.25, 7.09)
    with cue(3.50): bass(0.25, 7.08)
    with cue(3.75): bass(0.25, 7.11)

with measure(14):
    with cue(0.00): treble(0.25, 9.00)
    with cue(0.25): treble(0.25, 9.09)
    with cue(0.50): treble(0.25, 9.08)
    with cue(0.75): treble(0.25, 9.11)
    with cue(1.00): treble(0.25, 9.09)
    with cue(1.25): treble(0.25, 9.04)
    with cue(1.50): treble(0.25, 9.05)
    with cue(1.75): treble(0.25, 9.02)
    with cue(2.00): treble(0.25, 8.08)
    with cue(2.25): treble(0.25, 9.05)
    with cue(2.50): treble(0.25, 9.04)
    with cue(2.75): treble(0.25, 9.02)
    with cue(3.00): treble(0.5, 9.00)
    with cue(3.50): treble(0.25, 8.11)
    with cue(3.75): treble(0.25, 8.09)

    with cue(0.00): bass(0.25, 7.09)
    with cue(0.25): bass(0.25, 8.00)
    with cue(0.50): bass(0.25, 7.11)
    with cue(0.75): bass(0.25, 8.02)
    with cue(1.00): bass(0.25, 8.00)
    with cue(1.25): bass(0.25, 8.04)
    with cue(1.50): bass(0.25, 8.02)
    with cue(1.75): bass(0.25, 8.05)
    with cue(2.00): bass(0.5, 8.04)
    with cue(2.50): bass(0.5, 7.09)
    with cue(3.00): bass(0.5, 8.04)
    with cue(3.50): bass(0.5, 7.04)

with measure(15):
    with cue(0.00): treble(0.25, 8.09)
    with cue(0.25): treble(0.25, 9.09)
    with cue(0.50): treble(0.25, 9.07)
    with cue(0.75): treble(0.25, 9.05)
    with cue(1.00): treble(0.25, 9.04)
    with cue(1.25): treble(0.25, 9.07)
    with cue(1.50): treble(0.25, 9.05)
    with cue(1.75): treble(0.25, 9.09)
    with cue(2.00): treble(2.25, 9.07)

    with cue(0.00): bass(0.5, 7.09)
    with cue(0.50): bass(0.5, 6.09)
    with cue(2.25): bass(0.25, 8.04)
    with cue(2.50): bass(0.25, 8.02)
    with cue(2.75): bass(0.25, 8.00)
    with cue(3.00): bass(0.25, 7.11)
    with cue(3.25): bass(0.25, 8.02)
    with cue(3.50): bass(0.25, 8.01)
    with cue(3.75): bass(0.25, 8.04)

with measure(16):
    with cue(0.25): treble(0.25, 9.04)
    with cue(0.50): treble(0.25, 9.05)
    with cue(0.75): treble(0.25, 9.07)
    with cue(1.00): treble(0.25, 9.09)
    with cue(1.25): treble(0.25, 9.05)
    with cue(1.50): treble(0.25, 9.07)
    with cue(1.75): treble(0.25, 9.04)
    with cue(2.00): treble(2.25, 9.05)

    with cue(0.00): bass(2.25, 8.02)
    with cue(2.25): bass(0.25, 7.09)
    with cue(2.50): bass(0.25, 7.11)
    with cue(2.75): bass(0.25, 8.00)
    with cue(3.00): bass(0.25, 8.02)
    with cue(3.25): bass(0.25, 7.11)
    with cue(3.50): bass(0.25, 8.00)
    with cue(3.75): bass(0.25, 7.09)

with measure(17):
    with cue(0.25): treble(0.25, 9.07)
    with cue(0.50): treble(0.25, 9.05)
    with cue(0.75): treble(0.25, 9.04)
    with cue(1.00): treble(0.25, 9.02)
    with cue(1.25): treble(0.25, 9.05)
    with cue(1.50): treble(0.25, 9.04)
    with cue(1.75): treble(0.25, 9.07)
    with cue(2.00): treble(2.25, 9.05)

    with cue(0.00): bass(2.25, 7.11)
    with cue(2.25): bass(0.25, 8.02)
    with cue(2.50): bass(0.25, 8.00)
    with cue(2.75): bass(0.25, 7.11)
    with cue(3.00): bass(0.25, 7.09)
    with cue(3.25): bass(0.25, 8.00)
    with cue(3.50): bass(0.25, 7.11)
    with cue(3.75): bass(0.25, 8.02)

with measure(18):
    with cue(0.25): treble(0.25, 9.02)
    with cue(0.50): treble(0.25, 9.04)
    with cue(0.75): treble(0.25, 9.05)
    with cue(1.00): treble(0.25, 9.07)
    with cue(1.25): treble(0.25, 9.04)
    with cue(1.50): treble(0.25, 9.05)
    with cue(1.75): treble(0.25, 9.02)
    with cue(2.00): treble(2.25, 9.04)

    with cue(0.00): bass(2.25, 8.00)
    with cue(2.25): bass(0.25, 7.07)
    with cue(2.50): bass(0.25, 7.09)
    with cue(2.75): bass(0.25, 7.10)
    with cue(3.00): bass(0.25, 8.00)
    with cue(3.25): bass(0.25, 7.09)
    with cue(3.50): bass(0.25, 7.10)
    with cue(3.75): bass(0.25, 7.07)

with measure(19):
    with cue(0.25): treble(0.25, 9.00)
    with cue(0.50): treble(0.25, 9.02)
    with cue(0.75): treble(0.25, 9.04)
    with cue(1.00): treble(0.25, 9.05)
    with cue(1.25): treble(0.25, 9.02)
    with cue(1.50): treble(0.25, 9.04)
    with cue(1.75): treble(0.25, 9.00)
    with cue(2.00): treble(0.25, 9.02)
    with cue(2.25): treble(0.25, 9.04)
    with cue(2.50): treble(0.25, 9.05)
    with cue(2.75): treble(0.25, 9.07)
    with cue(3.00): treble(0.25, 9.09)
    with cue(3.25): treble(0.25, 9.05)
    with cue(3.50): treble(0.25, 9.07)
    with cue(3.75): treble(0.25, 9.04)

    with cue(0.00): bass(0.5, 7.09)
    with cue(0.50): bass(0.5, 7.10)
    with cue(1.00): bass(0.5, 7.09)
    with cue(1.50): bass(0.5, 7.07)
    with cue(2.00): bass(0.5, 7.05)
    with cue(2.50): bass(0.5, 8.02)
    with cue(3.00): bass(0.5, 8.00)
    with cue(3.50): bass(0.5, 7.10)

with measure(19): score.write("a 0 0 {0}".format(cue.now()))

score.i(2, 0, 90)

score.pmap('i', 1, 2, lambda x: x + random() * 0.05)
score.pmap('i', 1, 3, lambda x: x + random() * 0.05)
score.pmap('i', 1, 4, lambda x: x * 0.5)
score.end()

</CsScore>
</CsoundSynthesizer>
