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
    ipch = cpspch(p5)  ; Frequency

    kenv line iamp, idur, 0      ; Line envelope
    a1 vco2 kenv, ipch, 12, 0.5  ; Triangle wave
    out a1
endin

</CsInstruments>
<CsScore bin="./pysco.py">

score('t 0 210')

def phrase():
    score('''
    i 1 0 1    0.5 8.07
    i 1 + .    .   9.00
    i 1 + 0.25 .   8.11
    i 1 + 0.25 .   8.09
    i 1 + 0.5  .   8.11
    i 1 + .    .   9.00
    ''')

with cue(0): phrase()
with cue(4): phrase()
with cue(8): phrase()
with cue(12): phrase()

</CsScore>
</CsoundSynthesizer>
