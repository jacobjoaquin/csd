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

from csd.pysco import PythonScore
from random import choice

score = PythonScore()
cue = score.cue

score.write('''
t 0 170

; Measure 1
i 1 0.0 0.5 0.707 0 1
i 1 1.0 0.5 0.707 1 1
i 1 2.5 0.5 0.707 0 1
i 1 3.0 0.5 0.707 1 1

; Measure 2
i 1 4.0 0.5 0.707 0 1
i 1 5.0 0.5 0.707 1 1
i 1 6.5 0.5 0.707 0 1
i 1 7.0 0.5 0.707 1 1

; Measure 3
i 1 8.0  0.5 0.707 0 1
i 1 9.0  0.5 0.707 1 1
i 1 10.5 0.5 0.707 0 1
i 1 11.0 0.5 0.707 1 1

; Measure 4
i 1 12.0 0.5 0.707 0 1
i 1 13.0 0.5 0.707 1 1
i 1 14.5 0.5 0.707 0 1
i 1 15.0 0.5 0.707 1 1
''')

score.end();

</CsScore>
</CsoundSynthesizer>
