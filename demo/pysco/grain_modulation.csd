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

    a1 oscil 0.5, ifreq, 1, 0.76
;    a1 init 1
    chnmix a1 + 0.5, "mod"
endin

instr 2
    idur = p3
    iamp = p4
    ifreq = p5
    indx = p6

    amod chnget "mod"
    a1 oscil iamp, ifreq + ifreq * amod * indx, 1
    outs a1, a1
endin

instr 3
    chnclear "mod"
endin

</CsInstruments>
<CsScore bin="python pysco.py">

from random import random

def single_cycle_generator(dur, amp, freq_min, freq_max, density):
    for i in range(int(density * dur)):
        freq = random() * (freq_max - freq_min) + freq_min
        t = random() * dur
        event_i(1, t, 1 / freq, amp, freq, random())

score('''
f 1 0 8192 10 1
i 2 0 16 0.707 40 16
i 3 0 16
''')

with cue(0):
    single_cycle_generator(16, 1, 5, 40, 60)

</CsScore>
</CsoundSynthesizer>
