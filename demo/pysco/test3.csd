<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 4410
ksmps = 10
nchnls = 1
0dbfs = 1.0

instr 1
    idur = p3   ; Duration
    iamp = p4   ; Amplitude
    ifreq = p5  ; Frequency

    kenv line iamp, idur, 0       ; Line envelope
    a1 vco2 kenv, ifreq, 12, 0.5  ; Triangle wave
    out a1
endin

</CsInstruments>
<CsScore bin="./pysco.py">

# Test using score method.
score('''
t 0 189

i 1 0 0.5 -3 9.02
i 1 + .   .  8.07
i 1 + .   .  8.09
i 1 + .   .  8.11
i 1 + .   .  9.00
i 1 + .   .  8.09
i 1 + .   .  8.11
i 1 + .   .  8.07
''')

pmap('i', 1, 4, dB)
pmap('i', 1, 5, cpspch)

</CsScore>
</CsoundSynthesizer>
