<CsoundSynthesizer>
<CsInstruments>

sr = 44100
kr = 44100
ksmps = 1
nchnls = 2
0dbfs = 1.0

gS_loop = "amen_break.wav"
gisr filesr gS_loop
gilength filelen gS_loop
gibeats = 16 
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
<CsScore bin="python">

from csd.pysco import PythonScoreBin
from random import choice

def measure(t):
    return cue((t - 1) * 4.0)

def multiply(x, y):
    return x * y

def transpose(halfstep, value=1):
    return value * 2 ** (halfstep / 12.0)

def kick(dur=1, amp=1, tune=1):
    dur = dur * 0.5
    amp = amp * 0.707
    dur = dur * (1.0 / tune)

    sample = choice([0, 0.5, 4, 4.5])
    score.i(1, 0, dur, amp, sample, tune)

def snare(dur=1, amp=1, tune=1):
    dur = dur * 0.5
    amp = amp * 0.707
    dur = dur * (1.0 / tune)

    sample = choice([1, 3, 5, 7])
    score.i(1, 0, dur, amp, sample, tune)

def hat(dur=1, amp=1, tune=1):
    dur = dur * 0.35
    amp = amp * 0.707
    dur = dur * (1.0 / tune)

    sample = choice([1.5, 2, 2.5, 6.5, 7.5])
    score.i(1, 0, dur, amp, sample, tune)

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

score = PythonScoreBin()
cue = score.cue

score.prefilter('i', 1, 6, multiply, transpose(7))
score.prefilter('i', 1, 3, multiply, 1 / transpose(7))

score.t(170)

intro()

score.postfilter('i', 1, 4, multiply, 0.707)
 
</CsScore>
</CsoundSynthesizer>
