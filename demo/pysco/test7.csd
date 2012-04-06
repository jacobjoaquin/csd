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

def phrase():
    score('''
    i 1 0 0.5 -9 9.02
    i 1 + .   .  8.07
    i 1 + .   .  8.09
    i 1 + .   .  8.11
    i 1 + .   .  9.00
    i 1 + .   .  8.09
    i 1 + .   .  8.11
    i 1 + .   .  8.07
    ''')

def phrase_2():
    score('''
    i 1 0 0.5 -9 8.07
    i 1 + .   .  8.02
    i 1 + .   .  8.05
    i 1 + .   .  8.09
    i 1 + .   .  8.03
    i 1 + .   .  8.11
    i 1 + .   .  8.07
    i 1 + .   .  9.02
    ''')

score('t 0 120')

with cue(0):
    for i in range(0, 16):
        with cue(i): score('i 1 0 0.25 -9 8.02')

with cue(0):
    for i in [0, 0.505, 1.333]:
        with cue(i): phrase()

with cue(8):
    for i in [0, 0.505, 1.333]:
        with cue(i): phrase_2()

pmap('i', 1, 4, dB)
pmap('i', 1, 5, cpspch)

</CsScore>
</CsoundSynthesizer>
