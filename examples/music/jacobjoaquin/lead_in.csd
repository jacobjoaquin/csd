Lead-In
by Jacob Joaquin (2010)
jacobjoaquin@gmail.com
@jacobjoaquin

<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 1
0dbfs = 1.0

instr 1
    iamp = p4
    ifreq = p5

    a1 oscils iamp, ifreq, 0
    out a1
endin

instr 2
    idur = p3
    iamp = 1.0 / 1.44 * p4
    ifreq = p5
    ipeak = p6

    a1 oscils 1, ifreq, 0
    a2 oscils 0.1, ifreq * 3, 0
    a3 oscils 0.24, ifreq * 5, 0
    a4 oscils 0.1, ifreq * 1.15, 0
    a5 oscils 1, 1.003, 0

    aring = a1 + (a2 + a3 + a4) * a5
    aenv linseg 0, idur * ipeak, iamp, idur * (1.0 - ipeak), 0
    out aring * aenv
endin

instr 3
    idur = p3
    iamp = p4
    ifreq_1 = p5
    ifreq_2 = p6
    ipeak = p7

    a1 oscils iamp, ifreq_1, 0
    a2 oscils iamp, ifreq_2, 0
    aenv linseg 0, idur * ipeak, 1, idur * (1.0 - ipeak), 0
    out a1 * a2 * aenv
endin

instr 4
    idur = p3
    iamp = p4
    ifreq = p5

    a1 oscils iamp, ifreq, 0
    aenv linseg 1, idur, 0
    out a1 * aenv
endin

</CsInstruments>
<CsScore bin="python">

from csd.pysco import PythonScore
from random import random
from itertools import cycle

def cpspch(pch):
    octave, note = (int(x) for x in "{0:.2f}".format(pch).split('.'))
    return 440 * 2 ** (((octave - 8) * 12 + (note - 9)) / 12.0)

def dusty_vinyl(start, dur, amp, freq_min, freq_max, density):
    for i in xrange(int(density * dur)):
        freq = random() * (freq_max - freq_min) + freq_min
        t = random() * (dur - start) + start
        score.i(1, t, 1 / freq, amp * random(), freq)

def dirty_sine(start, dur, amp, freq, peak):
    score.i(2, start, dur, amp, freq, peak)

def ring_tine(start, dur, amp, freq_1, freq_2, peak):
    score.i(3, start, dur, amp, freq_1, freq_2, peak)

def sine_arp(start, bars, res, amp, note_list, decay):
    time = start
    pattern = cycle(note_list)
 
    for bar in range(bars):
        n = 0
        while n < 4.0 / res:
            note = cpspch(pattern.next())
            score.i(4, time, decay, amp, note)
            n += 1
            time = start + bar * 4 + n * res
    
score = PythonScore()
score.write('t 0 169')
note_pattern = [8.00, 8.03, 8.02, 8.07, 8.05, 8.10, 8.09, 9.00]    

dusty_vinyl(0, 80, 0.25, 1000, 10000, 30 * 60 / 169.0)
dirty_sine(6, 16, 0.15, cpspch(8.07), 0.95)
ring_tine(22, 4, 0.5, cpspch(10.10), 55, 0.0001)
sine_arp(22, 8, 0.25, 0.1, note_pattern, 0.8)
ring_tine(26, 9, 0.3, cpspch(9.03), 33, 0.9)
ring_tine(33, 9, 0.5, cpspch(8.10), 55, 0.001)
ring_tine(40, 9, 0.25, cpspch(7.00), 11, 0.0001)
ring_tine(54.5, 9, 0.3, cpspch(9.03), 33, 0.1)
ring_tine(54, 9, 0.5, cpspch(8.07), 44, 0.0001)
dirty_sine(54, 8, 0.15, cpspch(7.07), 0.1)
dirty_sine(60, 4, 0.15, cpspch(6.07), 0.1)

score.end()

</CsScore>
</CsoundSynthesizer>
