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
<CsScore bin="python pysco.py">

p_callback('i', 1, 4, dB)
p_callback('i', 1, 5, cpspch)

phrase = '''
i 1 0 0.5 -3 9.02
i 1 + .   .  8.07
i 1 + .   .  8.09
i 1 + .   .  8.11
i 1 + .   .  9.00
i 1 + .   .  8.09
i 1 + .   .  8.11
i 1 + .   .  8.07
'''

score('t 0 120')

with cue(0):
    score(phrase)

with cue(4):
    p_callback('i', 1, 3, lambda x: x * 2.0)
    p_callback('i', 1, 5, lambda x: x / 2.0)
    score(phrase)

with cue(12):
    score(phrase)

</CsScore>
</CsoundSynthesizer>
