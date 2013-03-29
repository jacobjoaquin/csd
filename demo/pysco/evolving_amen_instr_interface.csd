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

def kick(amp=1, tune=1):
    event_i(1, 0, 0.5, amp, 0, tune)

def snare(amp=1, tune=1):
    event_i(1, 0, 0.5, amp, 1, tune)

def hat(amp=1, tune=1):
    event_i(1, 0, 0.5, amp, 3.5, tune)

score('t 0 170')

with measure(1):
    with cue(0): kick()
    with cue(1): snare()
    with cue(2.5): kick()
    with cue(3): snare()

with measure(2):
    with cue(0): kick()
    with cue(1): snare()
    with cue(2.5): kick()
    with cue(3): snare()

with measure(3):
    with cue(0): kick()
    with cue(1): snare()
    with cue(2.5): kick()
    with cue(3): snare()

with measure(4):
    with cue(0): kick()
    with cue(1): snare()
    with cue(2.5): kick()
    with cue(3): snare()

</CsScore>
</CsoundSynthesizer>
