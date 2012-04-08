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

def add(x, y):
    return x + y

def transpose(x, y):
    return x * 2 ** (y / 12.0)

# Bind with additional arg
def p_transpose(y):
    p_callback('i', 1, 5, transpose, y)

phrase = '''
i 1 0 0.5 0 110
i 1 + .   0 220
i 1 + .   0 330
i 1 + .   0 440
i 1 + .   0 550
i 1 + .   0 660
i 1 + .   0 770
i 1 + .   0 880
'''

score('''
f 1 0 8192 10 1
t 0 180
''')

with cue(0):
    score(phrase)

with cue(4):
    p_transpose(17)
    score(phrase)

with cue(8):
    score(phrase)

with cue(12):
    p_transpose(17)
    score(phrase)

# pmap with additional arg
pmap('i', 1, 4, add, -3)

# Convert dB
pmap('i', 1, 4, dB)

</CsScore>
</CsoundSynthesizer>
