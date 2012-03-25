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

instr 2
    idur = p3   ; Duration
    iamp = p4   ; Amplitude
	ifreq = p5  ; Frequency

    aenv linseg 0, idur * 0.5, 1, idur * 0.5, 0
    a1 oscil aenv, ifreq, 1
    out a1
endin

</CsInstruments>
<CsScore bin="./pysco.py">

score('''
f 1 0 8192 10 1
t 0 120

i 1 0 0.5 -3 D5 
i 1 + .   .  G4 
i 1 + .   .  A4
i 1 + .   .  B4
i 1 + .   .  C5
i 1 + .   .  A4
i 1 + .   .  B4
i 1 + .   .  G5
''')

pmap('i', 1, 4, dB)
pmap('i', 1, 5, conv_to_hz)

</CsScore>
</CsoundSynthesizer>
