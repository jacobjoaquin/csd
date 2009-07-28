#!/usr/bin/env csound -g -odac

Tests if expressions are carried, or if the values they produce are
carried.

Conclusion:

Only the values are carried.  To evalute an expression for each
i-event, you must explicitly write the expression and not use the carry
preprocessor.

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
    
    asig oscils iamp, ifreq, 0
    out asig
endin
    
</CsInstruments>
<CsScore>
i 1 0 0.125 1 [~ * 440 + 440]
i 1 + .     . .
i 1 + .     . .
i 1 + .     . [~ * 440 + 440]
i 1 + .     . .
i 1 + .     . .
i 1 + .     . [~ * 440 + 440]
i 1 + .     . .
i 1 + .     . .

e
</CsScore>
</CsoundSynthesizer>

