<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 2
0dbfs = 1.0

; Uses one of the millions of Amen loops by the Winstons. Originally, that is.
gS_loop = "Amenbreak.aif"
gisr filesr gS_loop
gilength filelen gS_loop
gibeats = 64 

instr 1
    p3 = 0.13
    iamp = p4
    ibeat = p5
    ipos = ((ibeat / gibeats) * gilength)

    aenv linseg iamp, p3 * 0.85, iamp, p3 * 0.15, 0
    a1, a2 diskin2 gS_loop, 1.5, ipos
    out a1 * aenv, a2 * aenv
endin

</CsInstruments>
<CsScore bin="./pysco.py">

# Import choice from python library
from random import choice
from random import random

# Create wrapper functions for instruments.
def kick(amp=1):
    event_i(1, 0, 1, amp, choice([0, 0.5, 4, 8, 16]))

def snare(amp=1):
    event_i(1, 0, 1, amp, choice([1, 5, 9, 11.5]))

def hat(amp=1):
    event_i(1, 0, 1, amp, choice([3.5, 7.5, 10, 11, 19.5]))

score('t 0 170')

def pattern(r=0):
    '''pattern plus extra random notes'''
    
    with cue(0): kick()
    with cue(1): snare()
    with cue(2.5): kick()
    with cue(3): snare()

    times = [0.5, 0.75, 1.5, 2, 2.75, 3.5, 3.75]
    instrs = [kick, snare, hat, hat, hat]

    for time in times:
        if random() < r:
            with cue(time):
                instr = choice(instrs)
                instr(random() * 0.75 + 0.125)

def section_a():
    with cue(0): pattern()
    with cue(4): pattern(0.25)
    with cue(8): pattern()
    with cue(12): pattern(0.95)

def section_b():
    with cue(0): pattern(1.0)
    with cue(4): pattern(1.0)
    with cue(8): pattern(1.0)
    with cue(12): pattern(1.0)

with cue(0):
    for t in xrange(4):
        with cue(t * 16):
            section_a()

with cue(64):
    for t in xrange(4):
        with cue(t * 16):
            section_b()

with cue(128):
    for t in xrange(4):
        with cue(t * 16):
            section_a()

with cue(192):
    for t in xrange(4):
        with cue(t * 16):
            section_b()

pmap('i', 1, 4, lambda x: x * 0.707)

</CsScore>
</CsoundSynthesizer>
