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

def measure(t):
    return cue((t - 1) * 4.0)

def multiply(x, y):
    return x * y

def kick():
    sample = choice([0, 0.5, 4, 4.5])
    event_i(1, 0, 0.5, 0.707, sample, 1)

def snare():
    sample = choice([1, 3, 5, 7])
    event_i(1, 0, 0.5, 0.707, sample, 1)

def hat():
    sample = choice([1.5, 2, 2.5, 6.5, 7.5])
    event_i(1, 0, 0.35, 0.707, sample, 1)

def drum_pattern():
    with cue(0.0): kick()
    with cue(1.0): snare()
    with cue(2.5): kick()
    with cue(3.0): snare()

def drum_pattern_8th_hats():
    drum_pattern()

    for t in range(8):
        with cue(t / 2.0): hat()

score('t 0 170')

with measure(1): drum_pattern()
with measure(2): drum_pattern_8th_hats()
with measure(3): drum_pattern()
with measure(4): drum_pattern_8th_hats()

pmap('i', 1, 4, multiply, 0.707)

</CsScore>
</CsoundSynthesizer>
