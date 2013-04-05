<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 4410
ksmps = 10
nchnls = 1
0dbfs = 1.0

instr 1
    idur = p3          ; Duration
    iamp = p4          ; Amplitude
    ipch = cpspch(p5)  ; Pitch

    kenv line iamp, idur, 0      ; Line envelope
    a1 vco2 kenv, ipch, 12, 0.5  ; Triangle wave
    out a1
endin

</CsInstruments>
<CsScore bin="python">

import sys
sys.path.append('.')
import pysco

pysco.begin()

import csd.pysco.inline

score('''
f 1 0 8192 10 1
t 0 189

i 1 0 0.5 0.707 9.02
i 1 + .   .     8.07
i 1 + .   .     8.09
i 1 + .   .     8.11
i 1 + .   .     9.00
i 1 + .   .     8.09
i 1 + .   .     8.11
i 1 + .   .     8.07
''')

</CsScore>
</CsoundSynthesizer>
