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

    kenv linseg 0, 0.001, 1, 0.25, 0.4, 2, 0.1, 0, 0.1
    kenvgate linseg, 1, idur - 0.125, 1, 0.125, 0, 0, 0
    kenv = kenv * kenvgate

    a1 vco2 1, ifreq * 2, 0 
    a2 vco2 1, ifreq, 2, 0.6 + birnd(0.1)

    ival1 = 7000 + rnd(3000)
    ival2 = 7000 + rnd(3000)
    kenv2 expseg 16000 + rnd(2000), 2, ival1, 4, 2000, 0, 2000
    kenv3 expseg 16000 + rnd(2000), 2, ival2, 4, 2000, 0, 2000

    amix = a1 * 0.4 + a2 + 0.6
    amix = amix * kenv * iamp

    afilter1 moogladder amix, kenv2, 0.4 + rnd(0.1)
    afilter2 moogladder amix, kenv3, 0.4 + rnd(0.1)
    ;afilter1 moogvcf2 amix, kenv2, 0.5 + rnd(0.1)
    ;afilter2 moogvcf2 amix, kenv3, 0.5 + rnd(0.1)

    outs afilter1, afilter2

    chnmix afilter1, "left"
    chnmix afilter2, "right"
endin

instr 2
    iamp = p4
    idelay_left = p5
    idelay_right = p6
    iroom_size = p7
    iHFDamp = p8

    a1 chnget "left"
    a2 chnget "right"

    a1 delay a1, idelay_left
    a2 delay a2, idelay_right

    a1, a2 freeverb a2, a1, iroom_size, iHFDamp
    outs a1 * iamp, a2 * iamp

    chnclear "left"
    chnclear "right"
endin

instr 3
    prints "\nMeasure %d\n", p4
endin

</CsInstruments>
<CsScore bin="python">
'''Invention No. 1 by J.S. Bach'''

from csd.pysco import PythonScore
from random import random

def advance(m):
    with measure(m): score.write("a 0 0 {0}".format(cue.now()))

def pch_split(pch):
    octave, note = "{0:.2f}".format(pch).split('.')
    return int(octave), int(note.zfill(2))
    
def measure(t):
    beats = (t - 1) * 4.0
    score.i(3, beats, 1, t)
    return cue(beats)

def random_tempo(minimum, maximum):
    '''Change tempo randomly over time'''

    L = ["t"]
    counter = 0
    while counter < 88:
        L.append(str(counter))
        L.append(str(minimum + random() * (maximum - minimum))) 
        counter += random() * 3.0 + 1.0
    score.write(" ".join(L))

def arpeggiate(inc=0.06):
    offset = 0;
    while True:
        yield offset
        offset += inc

def well_temperament(p):
    '''Well Tempered

    # http://www.larips.com/
    '''

    ratios = [5.9, 3.9, 2, 3.9, -2, 7.8, 2, 3.9, 3.9, 0, 3.9, 0]
    octave, note = pch_split(p)
    pitch = 415 * 2 ** (((octave - 8) * 12 + (note - 9)) / 12.0)
    return pitch * 2 ** ((ratios[int(note)]) / 1200.0)

def harpsichord(start, dur, pitch):
    score.i(1, start, dur, 0.5, well_temperament(transpose_cpspch(pitch, -1)))

def reverb(dur, amp, delay_left, delay_right, room_size, damp):
    score.i(2, 0, dur, amp, delay_left, delay_right, room_size, damp)

score = PythonScore()
cue = score.cue
random_tempo(80, 85)
reverb(90, 2.333, 0.0223, 0.0213, 0.4, 0.3)
top = harpsichord
bottom = harpsichord

def transpose_cpspch(p, halfstep):
    halfstep = -12
    octave, note = pch_split(p) 
    note += halfstep

    if note < 0:
        octave = octave - abs(int(note + 1)) / 12 - 1
    else:
        octave += int(note / 12.0)

    note = int(note) % 12
    return octave + note * 0.01 + 1
    
def mordant(halfstep, instr, start, dur, pch):
    instr(start, dur * 0.25, pch)

with measure(1):
    top(0.25, 0.25, 8.00)
    top(0.50, 0.25, 8.02)
    top(0.75, 0.25, 8.04)
    top(1.00, 0.25, 8.05)
    top(1.25, 0.25, 8.02)
    top(1.50, 0.25, 8.04)
    top(1.75, 0.25, 8.00)
    top(2.00, 0.5, 8.07)
    top(2.50, 0.5, 9.00)
    mordant(-2, top, 3.00, 0.125, 8.11)
    #top(3.00, 0.125, 8.11)
    #top(3.125, 0.125, 8.09)
    #top(3.25, 0.25, 8.11)
    top(3.50, 0.5, 9.00)

    bottom(2.25, 0.25, 7.00)
    bottom(2.50, 0.25, 7.02)
    bottom(2.75, 0.25, 7.04)
    bottom(3.00, 0.25, 7.05)
    bottom(3.25, 0.25, 7.02)
    bottom(3.50, 0.25, 7.04)
    bottom(3.75, 0.25, 7.00)

with measure(2):
    top(0.00, 0.25, 9.02)
    top(0.25, 0.25, 8.07)
    top(0.50, 0.25, 8.09)
    top(0.75, 0.25, 8.11)
    top(1.00, 0.25, 9.00)
    top(1.25, 0.25, 8.09)
    top(1.50, 0.25, 8.11)
    top(1.75, 0.25, 8.07)
    top(2.00, 0.5, 9.02)
    top(2.50, 0.5, 9.07)
    top(3.00, 0.125, 9.05)
    top(3.125, 0.125, 9.04)
    top(3.25, 0.25, 9.05)
    top(3.50, 0.5, 9.07)

    bottom(0.00, 0.5, 7.07)
    bottom(0.50, 0.5, 6.07)
    bottom(2.25, 0.25, 7.07)
    bottom(2.50, 0.25, 7.09)
    bottom(2.75, 0.25, 7.11)
    bottom(3.00, 0.25, 8.00)
    bottom(3.25, 0.25, 7.09)
    bottom(3.50, 0.25, 7.11)
    bottom(3.75, 0.25, 7.07)

with measure(3):
    top(0.00, 0.25, 9.04)
    top(0.25, 0.25, 9.09)
    top(0.50, 0.25, 9.07)
    top(0.75, 0.25, 9.05)
    top(1.00, 0.25, 9.04)
    top(1.25, 0.25, 9.07)
    top(1.50, 0.25, 9.05)
    top(1.75, 0.25, 9.09)
    top(2.00, 0.25, 9.07)
    top(2.25, 0.25, 9.05)
    top(2.50, 0.25, 9.04)
    top(2.75, 0.25, 9.02)
    top(3.00, 0.25, 9.00)
    top(3.25, 0.25, 9.04)
    top(3.50, 0.25, 9.02)
    top(3.75, 0.25, 9.05)

    bottom(0.00, 0.5, 8.00)
    bottom(0.50, 0.5, 7.11)
    bottom(1.00, 0.5, 8.00)
    bottom(1.50, 0.5, 8.02)
    bottom(2.00, 0.5, 8.04)
    bottom(2.50, 0.5, 7.07)
    bottom(3.00, 0.5, 7.09)
    bottom(3.50, 0.5, 7.11)

with measure(4):
    top(0.00, 0.25, 9.04)
    top(0.25, 0.25, 9.02)
    top(0.50, 0.25, 9.00)
    top(0.75, 0.25, 8.11)
    top(1.00, 0.25, 8.09)
    top(1.25, 0.25, 9.00)
    top(1.50, 0.25, 8.11)
    top(1.75, 0.25, 9.02)
    top(2.00, 0.25, 9.00)
    top(2.25, 0.25, 8.11)
    top(2.50, 0.25, 8.09)
    top(2.75, 0.25, 8.07)
    top(3.00, 0.25, 8.06)
    top(3.25, 0.25, 8.09)
    top(3.50, 0.25, 8.07)
    top(3.75, 0.25, 8.11)

    bottom(0.00, 0.5, 8.00)
    bottom(0.50, 0.5, 7.04)
    bottom(1.00, 0.5, 7.06)
    bottom(1.50, 0.5, 7.07)
    bottom(2.00, 0.5, 7.09)
    bottom(2.50, 0.5, 7.11)
    bottom(3.00, 1.25, 8.00)

with measure(5):
    top(0.00, 0.5, 8.09)
    top(0.50, 0.5, 8.02)
    top(1.00, 0.125, 9.00)
    top(1.125, 0.125, 8.11)
    top(1.25, 0.5, 9.00)
    top(1.75, 0.25, 9.02)
    top(2.00, 0.25, 8.11)
    top(2.25, 0.25, 8.09)
    top(2.50, 0.25, 8.07)
    top(2.75, 0.25, 8.06)
    top(3.00, 0.25, 8.04)
    top(3.25, 0.25, 8.07)
    top(3.50, 0.25, 8.06)
    top(3.75, 0.25, 8.09)

    bottom(0.25, 0.25, 7.02)
    bottom(0.50, 0.25, 7.04)
    bottom(0.75, 0.25, 7.06)
    bottom(1.00, 0.25, 7.07)
    bottom(1.25, 0.25, 7.04)
    bottom(1.50, 0.25, 7.06)
    bottom(1.75, 0.25, 7.02)
    bottom(2.00, 0.5, 7.07)
    bottom(2.50, 0.5, 6.11)
    bottom(3.00, 0.5, 7.00)
    bottom(3.50, 0.5, 7.02)

with measure(6):
    top(0.00, 0.25, 8.07)
    top(0.25, 0.25, 8.11)
    top(0.50, 0.25, 8.09)
    top(0.75, 0.25, 9.00)
    top(1.00, 0.25, 8.11)
    top(1.25, 0.25, 9.02)
    top(1.50, 0.25, 9.00)
    top(1.75, 0.25, 9.04)
    top(2.00, 0.25, 9.02)
    top(2.25, 0.125, 8.11)
    top(2.375, 0.125, 9.00)
    top(2.50, 0.25, 9.02)
    top(2.75, 0.25, 9.07)
    top(3.00, 0.125, 8.11)
    top(3.125, 0.125, 8.09)
    top(3.25, 0.25, 8.11)
    top(3.50, 0.25, 8.09)
    top(3.75, 0.25, 8.07)

    bottom(0.00, 0.5, 7.04)
    bottom(0.50, 0.5, 7.06)
    bottom(1.00, 0.5, 7.07)
    bottom(1.50, 0.5, 7.04)
    bottom(2.00, 0.75, 6.11)
    bottom(2.75, 0.25, 7.00)
    bottom(3.00, 0.5, 7.02)
    bottom(3.50, 0.5, 6.02)

with measure(7):
    top(0.00, 0.5, 8.07)
    top(2.25, 0.25, 8.07)
    top(2.50, 0.25, 8.09)
    top(2.75, 0.25, 8.11)
    top(3.00, 0.25, 9.00)
    top(3.25, 0.25, 8.09)
    top(3.50, 0.25, 8.11)
    top(3.75, 0.25, 8.07)

    bottom(0.25, 0.25, 6.07)
    bottom(0.50, 0.25, 6.09)
    bottom(0.75, 0.25, 6.11)
    bottom(1.00, 0.25, 7.00)
    bottom(1.25, 0.25, 6.09)
    bottom(1.50, 0.25, 6.11)
    bottom(1.75, 0.25, 6.07)
    bottom(2.00, 0.5, 7.02)
    bottom(2.50, 0.5, 7.07)
    bottom(3.00, 0.5, 7.06)
    bottom(3.50, 0.5, 7.07)

with measure(8):
    top(0.00, 0.125, 8.06)
    top(0.125, 0.125, 8.04)
    top(0.25, 0.25, 8.06)
    top(2.25, 0.25, 8.09)
    top(2.50, 0.25, 8.11)
    top(2.75, 0.25, 9.00)
    top(3.00, 0.25, 9.02)
    top(3.25, 0.25, 8.11)
    top(3.50, 0.25, 9.00)
    top(3.75, 0.25, 8.09)

    bottom(0.00, 0.25, 7.09)
    bottom(0.25, 0.25, 7.02)
    bottom(0.50, 0.25, 7.04)
    bottom(0.75, 0.25, 7.06)
    bottom(1.00, 0.25, 7.07)
    bottom(1.25, 0.25, 7.04)
    bottom(1.50, 0.25, 7.06)
    bottom(1.75, 0.25, 7.02)
    bottom(2.00, 0.5, 7.09)
    bottom(2.50, 0.5, 8.02)
    bottom(3.00, 0.5, 8.00)
    bottom(3.50, 0.5, 8.02)

with measure(9):
    top(0.00, 0.5, 8.11)
    top(2.25, 0.25, 9.02)
    top(2.50, 0.25, 9.00)
    top(2.75, 0.25, 8.11)
    top(3.00, 0.25, 8.09)
    top(3.25, 0.25, 9.00)
    top(3.50, 0.25, 8.11)
    top(3.75, 0.25, 9.02)

    bottom(0.00, 0.25, 7.07)
    bottom(0.25, 0.25, 8.07)
    bottom(0.50, 0.25, 8.05)
    bottom(0.75, 0.25, 8.04)
    bottom(1.00, 0.25, 8.02)
    bottom(1.25, 0.25, 8.05)
    bottom(1.50, 0.25, 8.04)
    bottom(1.75, 0.25, 8.07)
    bottom(2.00, 0.5, 8.05)
    bottom(2.50, 0.5, 8.04)
    bottom(3.00, 0.5, 8.05)
    bottom(3.50, 0.5, 8.02)

with measure(10):
    top(0.00, 0.5, 9.00)
    top(2.25, 0.25, 9.04)
    top(2.50, 0.25, 9.02)
    top(2.75, 0.25, 9.00)
    top(3.00, 0.25, 8.11)
    top(3.25, 0.25, 9.02)
    top(3.50, 0.25, 9.01)
    top(3.75, 0.25, 9.04)

    bottom(0.00, 0.25, 8.04)
    bottom(0.25, 0.25, 8.09)
    bottom(0.50, 0.25, 8.07)
    bottom(0.75, 0.25, 8.05)
    bottom(1.00, 0.25, 8.04)
    bottom(1.25, 0.25, 8.07)
    bottom(1.50, 0.25, 8.05)
    bottom(1.75, 0.25, 8.09)
    bottom(2.00, 0.5, 8.07)
    bottom(2.50, 0.5, 8.05)
    bottom(3.00, 0.5, 8.07)
    bottom(3.50, 0.5, 8.04)

with measure(11):
    top(0.00, 0.5, 9.02)
    top(0.50, 0.5, 9.01)
    top(1.00, 0.5, 9.02)
    top(1.50, 0.5, 9.04)
    top(2.00, 0.5, 9.05)
    top(2.50, 0.5, 8.09)
    top(3.00, 0.5, 8.11)
    top(3.50, 0.5, 9.01)

    bottom(0.00, 0.25, 8.05)
    bottom(0.25, 0.25, 8.10)
    bottom(0.50, 0.25, 8.09)
    bottom(0.75, 0.25, 8.07)
    bottom(1.00, 0.25, 8.05)
    bottom(1.25, 0.25, 8.09)
    bottom(1.50, 0.25, 8.07)
    bottom(1.75, 0.25, 8.10)
    bottom(2.00, 0.25, 8.09)
    bottom(2.25, 0.25, 8.07)
    bottom(2.50, 0.25, 8.05)
    bottom(2.75, 0.25, 8.04)
    bottom(3.00, 0.25, 8.02)
    bottom(3.25, 0.25, 8.05)
    bottom(3.50, 0.25, 8.04)
    bottom(3.75, 0.25, 8.07)

with measure(12):
    top(0.00, 0.5, 9.02)
    top(0.50, 0.5, 8.06)
    top(1.00, 0.5, 8.08)
    top(1.50, 0.5, 8.09)
    top(2.00, 0.5, 8.11)
    top(2.50, 0.5, 9.00)
    top(3.00, 1.25, 9.02)

    bottom(0.00, 0.25, 8.05)
    bottom(0.25, 0.25, 8.04)
    bottom(0.50, 0.25, 8.02)
    bottom(0.75, 0.25, 8.00)
    bottom(1.00, 0.25, 7.11)
    bottom(1.25, 0.25, 8.02)
    bottom(1.50, 0.25, 8.00)
    bottom(1.75, 0.25, 8.04)
    bottom(2.00, 0.25, 8.02)
    bottom(2.25, 0.25, 8.00)
    bottom(2.50, 0.25, 7.11)
    bottom(2.75, 0.25, 7.09)
    bottom(3.00, 0.25, 7.08)
    bottom(3.25, 0.25, 7.11)
    bottom(3.50, 0.25, 7.09)
    bottom(3.75, 0.25, 8.00)

with measure(13):
    top(0.25, 0.25, 8.04)
    top(0.50, 0.25, 8.06)
    top(0.75, 0.25, 8.08)
    top(1.00, 0.25, 8.09)
    top(1.25, 0.25, 8.06)
    top(1.50, 0.25, 8.08)
    top(1.75, 0.25, 8.04)
    top(2.00, 0.25, 9.04)
    top(2.25, 0.25, 9.02)
    top(2.50, 0.25, 9.00)
    top(2.75, 0.25, 9.04)
    top(3.00, 0.25, 9.02)
    top(3.25, 0.25, 9.00)
    top(3.50, 0.25, 8.11)
    top(3.75, 0.25, 9.02)
   
    bottom(0.00, 0.5, 7.11)
    bottom(0.50, 0.5, 7.04)
    bottom(1.00, 0.125, 8.02)
    bottom(1.125, 0.125, 8.04)
    bottom(1.25, 0.5, 8.02)
    bottom(1.75, 0.25, 8.04)
    bottom(2.00, 0.25, 8.00)
    bottom(2.25, 0.25, 7.11)
    bottom(2.50, 0.25, 7.09)
    bottom(2.75, 0.25, 7.07)
    bottom(3.00, 0.25, 7.06)
    bottom(3.25, 0.25, 7.09)
    bottom(3.50, 0.25, 7.08)
    bottom(3.75, 0.25, 7.11)

with measure(14):
    top(0.00, 0.25, 9.00)
    top(0.25, 0.25, 9.09)
    top(0.50, 0.25, 9.08)
    top(0.75, 0.25, 9.11)
    top(1.00, 0.25, 9.09)
    top(1.25, 0.25, 9.04)
    top(1.50, 0.25, 9.05)
    top(1.75, 0.25, 9.02)
    top(2.00, 0.25, 8.08)
    top(2.25, 0.25, 9.05)
    top(2.50, 0.25, 9.04)
    top(2.75, 0.25, 9.02)
    top(3.00, 0.5, 9.00)
    top(3.50, 0.25, 8.11)
    top(3.75, 0.25, 8.09)

    bottom(0.00, 0.25, 7.09)
    bottom(0.25, 0.25, 8.00)
    bottom(0.50, 0.25, 7.11)
    bottom(0.75, 0.25, 8.02)
    bottom(1.00, 0.25, 8.00)
    bottom(1.25, 0.25, 8.04)
    bottom(1.50, 0.25, 8.02)
    bottom(1.75, 0.25, 8.05)
    bottom(2.00, 0.5, 8.04)
    bottom(2.50, 0.5, 7.09)
    bottom(3.00, 0.5, 8.04)
    bottom(3.50, 0.5, 7.04)

with measure(15):
    top(0.00, 0.25, 8.09)
    top(0.25, 0.25, 9.09)
    top(0.50, 0.25, 9.07)
    top(0.75, 0.25, 9.05)
    top(1.00, 0.25, 9.04)
    top(1.25, 0.25, 9.07)
    top(1.50, 0.25, 9.05)
    top(1.75, 0.25, 9.09)
    top(2.00, 2.25, 9.07)

    bottom(0.00, 0.5, 7.09)
    bottom(0.50, 0.5, 6.09)
    bottom(2.25, 0.25, 8.04)
    bottom(2.50, 0.25, 8.02)
    bottom(2.75, 0.25, 8.00)
    bottom(3.00, 0.25, 7.11)
    bottom(3.25, 0.25, 8.02)
    bottom(3.50, 0.25, 8.01)
    bottom(3.75, 0.25, 8.04)

with measure(16):
    top(0.25, 0.25, 9.04)
    top(0.50, 0.25, 9.05)
    top(0.75, 0.25, 9.07)
    top(1.00, 0.25, 9.09)
    top(1.25, 0.25, 9.05)
    top(1.50, 0.25, 9.07)
    top(1.75, 0.25, 9.04)
    top(2.00, 2.25, 9.05)

    bottom(0.00, 2.25, 8.02)
    bottom(2.25, 0.25, 7.09)
    bottom(2.50, 0.25, 7.11)
    bottom(2.75, 0.25, 8.00)
    bottom(3.00, 0.25, 8.02)
    bottom(3.25, 0.25, 7.11)
    bottom(3.50, 0.25, 8.00)
    bottom(3.75, 0.25, 7.09)

with measure(17):
    top(0.25, 0.25, 9.07)
    top(0.50, 0.25, 9.05)
    top(0.75, 0.25, 9.04)
    top(1.00, 0.25, 9.02)
    top(1.25, 0.25, 9.05)
    top(1.50, 0.25, 9.04)
    top(1.75, 0.25, 9.07)
    top(2.00, 2.25, 9.05)

    bottom(0.00, 2.25, 7.11)
    bottom(2.25, 0.25, 8.02)
    bottom(2.50, 0.25, 8.00)
    bottom(2.75, 0.25, 7.11)
    bottom(3.00, 0.25, 7.09)
    bottom(3.25, 0.25, 8.00)
    bottom(3.50, 0.25, 7.11)
    bottom(3.75, 0.25, 8.02)

with measure(18):
    top(0.25, 0.25, 9.02)
    top(0.50, 0.25, 9.04)
    top(0.75, 0.25, 9.05)
    top(1.00, 0.25, 9.07)
    top(1.25, 0.25, 9.04)
    top(1.50, 0.25, 9.05)
    top(1.75, 0.25, 9.02)
    top(2.00, 2.25, 9.04)

    bottom(0.00, 2.25, 8.00)
    bottom(2.25, 0.25, 7.07)
    bottom(2.50, 0.25, 7.09)
    bottom(2.75, 0.25, 7.10)
    bottom(3.00, 0.25, 8.00)
    bottom(3.25, 0.25, 7.09)
    bottom(3.50, 0.25, 7.10)
    bottom(3.75, 0.25, 7.07)

with measure(19):
    top(0.25, 0.25, 9.00)
    top(0.50, 0.25, 9.02)
    top(0.75, 0.25, 9.04)
    top(1.00, 0.25, 9.05)
    top(1.25, 0.25, 9.02)
    top(1.50, 0.25, 9.04)
    top(1.75, 0.25, 9.00)
    top(2.00, 0.25, 9.02)
    top(2.25, 0.25, 9.04)
    top(2.50, 0.25, 9.05)
    top(2.75, 0.25, 9.07)
    top(3.00, 0.25, 9.09)
    top(3.25, 0.25, 9.05)
    top(3.50, 0.25, 9.07)
    top(3.75, 0.25, 9.04)

    bottom(0.00, 0.5, 7.09)
    bottom(0.50, 0.5, 7.10)
    bottom(1.00, 0.5, 7.09)
    bottom(1.50, 0.5, 7.07)
    bottom(2.00, 0.5, 7.05)
    bottom(2.50, 0.5, 8.02)
    bottom(3.00, 0.5, 8.00)
    bottom(3.50, 0.5, 7.10)

with measure(20):
    top(0.00, 0.25, 9.05)
    top(0.25, 0.25, 9.07)
    top(0.50, 0.25, 9.09)
    top(0.75, 0.25, 9.11)
    top(1.00, 0.25, 10.00)
    top(1.25, 0.25, 9.09)
    top(1.50, 0.25, 9.11)
    top(1.75, 0.25, 9.07)
    top(2.00, 0.5, 10.00)
    top(2.50, 0.5, 9.07)
    top(3.00, 0.5, 9.04)
    top(3.50, 0.25, 9.02)
    top(3.75, 0.25, 9.00)

    bottom(0.00, 0.5, 7.09)
    bottom(0.50, 0.5, 8.05)
    bottom(1.00, 0.5, 8.04)
    bottom(1.50, 0.5, 8.02)
    bottom(2.00, 0.25, 8.04)
    bottom(2.25, 0.25, 8.02)
    bottom(2.50, 0.25, 8.04)
    bottom(2.75, 0.25, 8.05)
    bottom(3.00, 0.25, 8.07)
    bottom(3.25, 0.25, 8.04)
    bottom(3.50, 0.25, 8.05)
    bottom(3.75, 0.25, 8.02)

with measure(21):
    top(0.00, 0.25, 9.00)
    top(0.25, 0.25, 8.10)
    top(0.50, 0.25, 8.09)
    top(0.75, 0.25, 8.07)
    top(1.00, 0.25, 8.05)
    top(1.25, 0.25, 8.09)
    top(1.50, 0.25, 8.07)
    top(1.75, 0.25, 8.10)
    top(2.00, 0.25, 8.09)
    top(2.25, 0.25, 8.11)
    top(2.50, 0.25, 9.00)
    top(2.75, 0.25, 8.04)
    top(3.00, 0.25, 8.02)
    top(3.25, 0.25, 9.00)
    top(3.50, 0.25, 8.05)
    top(3.75, 0.25, 8.11)

    bottom(0.00, 0.5, 7.04)
    bottom(0.50, 0.5, 7.00)
    bottom(1.00, 0.5, 7.02)
    bottom(1.50, 0.5, 7.04)
    bottom(2.00, 0.25, 7.05)
    bottom(2.25, 0.25, 7.02)
    bottom(2.50, 0.25, 7.04)
    bottom(2.75, 0.25, 7.05)
    bottom(3.00, 0.5, 7.07)
    bottom(3.50, 0.5, 6.07)

with measure(22):
    arp = arpeggiate()
    score.p_callback('i', 1, 2, lambda x: arp.next())
    bottom(0, 0.25, 6.00)
    bottom(0, 0.25, 7.00)
    top(0, 0.25, 8.04)
    top(0, 0.25, 8.07)
    top(0, 0.25, 9.00)
    del arp

score.pmap('i', 1, 2, lambda x: x + random() * 0.05)
score.pmap('i', 1, 3, lambda x: x + random() * 0.05)
score.pmap('i', 1, 4, lambda x: x * 0.25)
score.end()

</CsScore>
</CsoundSynthesizer>
