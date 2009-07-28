#!/usr/bin/env csound -g -odac

Tests if i-events auto carry without the carry preprocessor.

Conclusion:

When not using the no-carry, carry is implicit for everything except
for a blank i-event, i.e., 'i  ; nothing else'.  And, pfield 2 requires
at least one '+' in order to carry.

<CsoundSynthesizer>
<CsInstruments>
sr     = 44100
kr     = 4410
ksmps  = 10
nchnls = 1

0dbfs = 1.0

instr 1
    iamp = p4
    ifreq = p5
 
    aenv line iamp, p3, 0
    asig oscil aenv, ifreq, 1
    out asig
endin
    
</CsInstruments>
<CsScore>
f 1 0 8192 10 1

i 1 0 1 1 440
i 1 + . . .
i 1 . . .
i 1 . .
i 1 .
i 1
i .
i .
;i              ; breaks
s

i 1 0 1 1 880
i . +          ; At least on '+' required to implicitly carry
i .

</CsScore>
</CsoundSynthesizer>

