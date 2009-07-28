#!/usr/bin/env csound -g -odac

Tests if the blank i-event in the Csound manual really does what is
advertised. 

    i1   0    .5        100
    i .  +
    i

Should translate to this:

    i1   0         .5        100
    i1   .5        .5        100
    i1   1         .5        100

Conclusion:

Just sent this to the list and waiting for a response.  However, it
seems that the translation does not match what is written in the
manual.


<CsoundSynthesizer>
<CsInstruments>
sr     = 44100
kr     = 4410
ksmps  = 10
nchnls = 1

instr 1
    ; do nothing
endin
    
</CsInstruments>
<CsScore>
i1   0    .5        100
i .  +
i

</CsScore>
</CsoundSynthesizer>

