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
    ipch = cpspch(p5)

    kenv adsr 0.05, 0.125, 0.4, 1
    a1 vco2 kenv, ipch * 2, 0 
    a2 vco2 kenv, ipch, 2, 0.3 + birnd(0.1)

    kenv2 expseg 16000, idur, 9000
    afilter moogladder a1 * 0.4 + a2 * 0.6, kenv2, 0.4
    outs afilter, afilter

    chnmix afilter, "h_out"
endin

instr 2
    imix = 2.5
    a1 chnget "h_out"
    a1 delay a1, 0.0233
    a1, a2 freeverb a1, a1, 0.4, 0.3
    outs a1 * imix, a2 * imix
    chnclear "h_out"
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
    score.i(1, 0, dur, 0.5, pitch)

treble = harpsichord
bass = harpsichord
score.write('t 0 90')

score.i(2, 0, 27)

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

score.pmap('i', 1, 2, lambda x: x + random() * 0.04)
score.pmap('i', 1, 3, lambda x: x + random() * 0.04)
score.end()

</CsScore>
</CsoundSynthesizer>
