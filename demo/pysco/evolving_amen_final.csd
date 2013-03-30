<CsoundSynthesizer>
<CsInstruments>

sr = 44100
kr = 44100
ksmps = 1
nchnls = 2
0dbfs = 1.0

gS_loop = "samples/Amenbreak.aif"
gisr filesr gS_loop
gilength filelen gS_loop
gibeats = 64 
gi_sampleleft ftgen 1, 0, 0, 1, gS_loop, 0, 4, 0

instr 1
    idur = p3
    iamp = p4
    ibeat = p5
    itune = p6
    ipos = ibeat / gibeats * gilength * gisr

    aenv linseg iamp, idur - 0.01, iamp, 0.01, 0
    a1, a2 loscilx aenv, itune, 1, 0, 1, ipos, 0
    outs a1, a2
endin

</CsInstruments>
<CsScore bin="python pysco.py">

from random import choice
from random import random

def measure(t):
    return cue((t - 1) * 4.0)

def multiply(x, y):
    return x * y

def transpose(halfstep, value=1):
    return value * 2 ** (halfstep / 12.0)

def kick(dur=1, amp=1, tune=1):
    dur = dur * 0.5
    amp = amp * 0.707

    sample = choice([0, 0.5, 4, 4.5])
    event_i(1, 0, dur, amp, sample, tune)

def snare(dur=1, amp=1, tune=1):
    dur = dur * 0.5
    amp = amp * 0.707

    sample = choice([1, 3, 5, 7])
    event_i(1, 0, dur, amp, sample, tune)

def hat(dur=1, amp=1, tune=1):
    dur = dur * 0.35
    amp = amp * 0.707

    sample = choice([1.5, 2, 2.5, 6.5, 7.5])
    event_i(1, 0, dur, amp, sample, tune)

def swell(instr, phrase_dur, note_dur, n_beats, start_amp, end_amp, tune=1):
    inc = (end_amp - start_amp) / (n_beats + 1.0)

    for t in xrange(n_beats):
        with cue(t / float(n_beats) * phrase_dur):
            instr(note_dur, start_amp + t * inc, tune)

def drum_pattern():
    with cue(0.0): kick()
    with cue(1.0): snare()
    with cue(2.5): kick()
    with cue(3.0): snare()

def drum_pattern_2():
    for t in range(4):
        with cue(t): kick(tune=transpose(-5))

def drum_pattern_8th_hats():
    drum_pattern()

    for t in range(8):
        with cue(t / 2.0): hat()

def drum_pattern_flair(r=0):
    drum_pattern()

    times = [0.5, 0.75, 1.5, 2, 2.75, 3.5, 3.75]
    instrs = [kick, snare, hat, hat, hat]

    for time in times:
        if random() < r:
            with cue(time):
                instr = choice(instrs)
                instr(amp=random() * 0.75 + 0.125)

def intro():
    with measure(1):
        swell(kick, 4, 1, 4, 0.3, 1, transpose(-3))

    with measure(2):
        swell(kick, 4, 1, 4, 0.3, 1, transpose(-3))
        swell(hat, 2, 1, 4, 1.0, 0.5)
        with cue(2.0): swell(hat, 2, 1, 4, 0.5, 1.0)

    with measure(3):
        swell(kick, 4, 1, 4, 0.3, 1, transpose(-3))
        swell(hat, 2, 1, 4, 1.0, 0.5)
        with cue(2.0): swell(hat, 2, 1, 4, 0.5, 1.0)
        swell(snare, 4, 0.5, 16, 0.4, 0.05, transpose(7))

    with measure(4):
        swell(kick, 4, 1, 8, 0.3, 1)
        swell(hat, 2, 1, 4, 1.0, 0.5)
        with cue(2.0): swell(hat, 2, 1, 4, 0.5, 1.0)
        swell(snare, 4, 1, 16, 0.05, 0.7, transpose(7))

def section_a():
    for m in range(1, 16, 4):
        with measure(m):
            with measure(1): drum_pattern()
            with measure(2): drum_pattern_flair(0.25)
            with measure(3): drum_pattern_8th_hats()
            with measure(4): drum_pattern_flair(1)

def section_b():
    for m in range(1, 17):
        with measure(m): drum_pattern_flair(1)

    with measure(9): swell(snare, 16, 1, 64, 0.2, 0.1, transpose(7))
    with measure(13): swell(snare, 12, 1, 48, 0.1, 0.2, transpose(7))
    with measure(16): swell(snare, 4, 1, 16, 0.2, 0.6, transpose(7))

def section_c():
    with measure(1): swell(kick, 4, 1, 8, 1.1, 0.4, transpose(-3))
    with measure(2): swell(kick, 20, 1, 8 * 5, 0.4, 0.4, transpose(-3))
    with measure(7): swell(kick, 8, 1, 16, 0.4, 1, transpose(-3))
    with measure(1): 
        with cue(1): swell(hat, 32, 1, 16, 1, 1) 
    with measure(5): swell(snare, 15, 1, 60, 0.2, 0.3, transpose(7))
    with measure(8):
        with cue(3): swell(snare, 1, 1, 4, 0.1, 0.8, transpose(7))

p_callback('i', 1, 6, multiply, transpose(7))
p_callback('i', 1, 3, multiply, 1 / transpose(7))

score('t 0 170')

#with measure(1): section_c()
#with measure(1): section_c()
#with measure(9): section_b()

if True:
    with measure(1): intro()
    with measure(5): section_a()
    with measure(21): section_b()
    with measure(37): section_a()
    with measure(53): section_c()
    with measure(61): section_a()
    with measure(77): section_b()

pmap('i', 1, 4, multiply, 0.707)

</CsScore>
</CsoundSynthesizer>
