Example inspired by CMask "Lists"

CMask is a stochastic event generator for Csound
written by Andre Bartetzki
http://www.bartetzki.de/en/software.html

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

    kenv line iamp, idur, 0       ; Line envelope
    a1 vco2 kenv, ifreq, 12, 0.5  ; Triangle wave

    outs a1 * sqrt(1 - ipan), a1 * sqrt(ipan)
endin

</CsInstruments>
<CsScore bin="python pysco.py">

from random import choice
from random import random

def cycle(values):
    pos = 0
    while True:
        yield values[pos]
        pos = (pos + 1) % len(values)  

def swing(values):
    values += values[-2:0:-1]
    pos = 0
    while True:
        yield values[pos]
        pos = (pos + 1) % len(values)  

def heap(values):
    current = list(values)
    while True:
        yield current.pop(int(random() * len(current)));
        if len(current) == 0:
            current = list(values)

# Convert pch notation to Hz
p_callback('i', 1, 5, cpspch)

score('t 0 120')

# Create generators
cycle_d_min = cycle([7.02, 7.05, 7.09, 8.02]);
swing_g_min = swing([7.07, 7.10, 8.02, 8.07]);
heap_c_maj = heap([7.00, 7.04, 7.07, 8.00]);

# Chord used with Python's choice function
a_min = [7.09, 8.00, 8.04, 8.09];

# Cycle through D minor chord
with cue(0):
    event_i(1, 0.0, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 0.5, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 1.0, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 1.5, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 2.0, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 2.5, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 3.0, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 3.5, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 4.0, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 4.5, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 5.0, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 5.5, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 6.0, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 6.5, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 7.0, 0.5, 0.707, cycle_d_min.next(), 0.5)
    event_i(1, 7.5, 0.5, 0.707, cycle_d_min.next(), 0.5)

# Swing through G minor chord
with cue(8):
    event_i(1, 0.0, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 0.5, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 1.0, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 1.5, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 2.0, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 2.5, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 3.0, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 3.5, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 4.0, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 4.5, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 5.0, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 5.5, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 6.0, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 6.5, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 7.0, 0.5, 0.707, swing_g_min.next(), 0.5)
    event_i(1, 7.5, 0.5, 0.707, swing_g_min.next(), 0.5)

# Heap through C Major chord
with cue(16):
    event_i(1, 0.0, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 0.5, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 1.0, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 1.5, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 2.0, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 2.5, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 3.0, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 3.5, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 4.0, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 4.5, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 5.0, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 5.5, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 6.0, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 6.5, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 7.0, 0.5, 0.707, heap_c_maj.next(), 0.5)
    event_i(1, 7.5, 0.5, 0.707, heap_c_maj.next(), 0.5)

# Choice through A minor chord
# In CMask, this was called random. This already exists
# in Python as choice, hence the reason that it wasn't
# implemented as a custom generator like the other 3.
with cue(24):
    event_i(1, 0.0, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 0.5, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 1.0, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 1.5, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 2.0, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 2.5, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 3.0, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 3.5, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 4.0, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 4.5, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 5.0, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 5.5, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 6.0, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 6.5, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 7.0, 0.5, 0.707, choice(a_min), 0.5)
    event_i(1, 7.5, 0.5, 0.707, choice(a_min), 0.5)
</CsScore>
</CsoundSynthesizer>
