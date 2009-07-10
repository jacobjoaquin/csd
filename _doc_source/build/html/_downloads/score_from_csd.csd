<CsoundSynthesizer>
<CsInstruments>
sr     = 44100
kr     = 4410
ksmps  = 10
nchnls = 1

0dbfs = 1.0

instr 1
    iamp = p4
    ipitch = cpspch(p5)
    itable = p6
    
    asig oscil iamp, ipitch, itable, -1
    out asig
endin
    
</CsInstruments>
<CsScore>
f 1 0 8192 10 1  ; Sinewave

i 1 0 0.125 1 8.00 1
i 1 + .     . 8.07 .
i 1 + .     . 8.04 .
i 1 + .     . 8.00 .
i 1 + .     . 8.07 .
i 1 + .     . 8.04 .
i 1 + .     . 8.00 .
i 1 + .     . 8.07 .
i 1 + .     . 8.04 .
i 1 + .     . 8.00 .
i 1 + .     . 8.07 .
i 1 + .     . 8.04 .
i 1 + .     . 8.00 .
i 1 + .     . 8.07 .
i 1 + .     . 8.04 .
i 1 + .     . 8.00 .

e
</CsScore>
</CsoundSynthesizer>

