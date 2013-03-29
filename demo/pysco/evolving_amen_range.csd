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

    a1, a2 loscilx iamp, itune, 1, 0, 1, ipos, 0
    outs a1, a2
endin

</CsInstruments>
<CsScore bin="python pysco.py">

def measure(t):
    return cue((t - 1) * 4.0)

def kick():
    event_i(1, 0, 0.5, 0.707, 0, 1)

def snare():
    event_i(1, 0, 0.5, 0.707, 1, 1)

def drum_pattern():
    with cue(0.0): kick()
    with cue(1.0): snare()
    with cue(2.5): kick()
    with cue(3.0): snare()

score('t 0 170')

for m in range(1, 5):
    with measure(m): drum_pattern()

</CsScore>
</CsoundSynthesizer>
