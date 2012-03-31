<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
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

with t(0): score('i 1 0 0.5 -7 9.02')
with t(0.02): score('i 1 0 0.5 -7 10.02')



pmap('i', 1, 4, dB)
pmap('i', 1, 5, cpspch)

</CsScore>
</CsoundSynthesizer>
