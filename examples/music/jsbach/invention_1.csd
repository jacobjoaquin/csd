<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 2
0dbfs = 1.0

instr 1
    p3 = p3 + 0.125
    idur = p3
    iamp = p4
    ipch = cpspch(p5)

    kenv adsr 0.01, 0.125, 0.5, 1
    a1 vco2 kenv, ipch * 2, 0 
    a2 vco2 kenv, ipch, 2, 0.3  ; Triangle wave

    afilter moogladder a1 * 0.4 + a2 * 0.6, 15000, 0.4
    outs afilter, afilter

    chnmix afilter, "h_out"
endin

instr 2
    imix = 2.5
    a1 chnget "h_out"
    a1 delay a1, 0.0233
    a1, a2 freeverb a1, a1, 0.4, 0.3
    outs a1 * imix, a2 * imix
    chnclear "h_out"
endin

</CsInstruments>
<CsScore bin="python">

from csd.pysco import PythonScore

score = PythonScore()
cue = score.cue

# Invention No. 1 (excerpt) by J.S. Bach

def measure(t):
    return cue((t - 1) * 4.0)

def harpsichord(dur, pitch):
    score.i(1, 0, dur, 0.5, pitch)

score.write('t 0 160')

score.i(2, 0, 60)

with measure(1):
    with cue(0.5): harpsichord(0.5, 8.00)
    with cue(1.0): harpsichord(0.5, 8.02)
    with cue(1.5): harpsichord(0.5, 8.04)
    with cue(2.0): harpsichord(0.5, 8.05)
    with cue(2.5): harpsichord(0.5, 8.02)
    with cue(3.0): harpsichord(0.5, 8.04)
    with cue(3.5): harpsichord(0.5, 8.00)

with measure(2):
    score.write('''
    i 1 0 1    0.5 8.07
    i 1 + .    .   9.00
    i 1 + 0.25 .   8.11
    i 1 + 0.25 .   8.09
    i 1 + 0.5  .   8.11
    i 1 + .    .   9.00

    i 1 0.5 0.5 0.5 7.00
    i 1 +   .   .   7.02
    i 1 +   .   .   7.04
    i 1 +   .   .   7.05
    i 1 +   .   .   7.02
    i 1 +   .   .   7.04
    i 1 +   .   .   7.00
    ''')

with measure(3):
    score.write('''
    i 1 0 0.5 0.5 9.02
    i 1 + .   .   8.07
    i 1 + .   .   8.09
    i 1 + .   .   8.11
    i 1 + .   .   9.00
    i 1 + .   .   8.09
    i 1 + .   .   8.11
    i 1 + .   .   8.07

    i 1 0 1 0.5 7.07
    i 1 + . 0.5 6.07
    ''')

with measure(4):
    score.write('''
    i 1 0 1    0.5 9.02
    i 1 + .    .   9.07
    i 1 + 0.25 .   9.05
    i 1 + 0.25 .   9.04
    i 1 + 0.5  .   9.05
    i 1 + .    .   9.07

    i 1 0.5 0.5 0.5 7.07
    i 1 +   .   .   7.09
    i 1 +   .   .   7.11
    i 1 +   .   .   8.00
    i 1 +   .   .   7.09
    i 1 +   .   .   7.11
    i 1 +   .   .   7.07
    ''')

with measure(5):
    score.write('''
    i 1 0 0.5 0.5 9.04
    i 1 + .   .   9.09
    i 1 + .   .   9.07
    i 1 + .   .   9.05
    i 1 + .   .   9.04
    i 1 + .   .   9.07
    i 1 + .   .   9.05
    i 1 + .   .   9.09

    i 1 0 1 0.5 8.00
    i 1 + . .   7.11
    i 1 + . .   8.00
    i 1 + . .   8.02
    ''')

with measure(6):
    score.write('''
    i 1 0 0.5 0.5 9.07
    i 1 + .   .   9.05
    i 1 + .   .   9.04
    i 1 + .   .   9.02
    i 1 + .   .   9.00
    i 1 + .   .   9.04
    i 1 + .   .   9.02
    i 1 + .   .   9.05

    i 1 0 1 0.5 8.04
    i 1 + . .   7.07
    i 1 + . .   7.09
    i 1 + . .   7.11
    ''')

with measure(7):
    score.write('''
    i 1 0 0.5 0.5 9.04
    i 1 + .   .   9.02
    i 1 + .   .   9.00
    i 1 + .   .   8.11
    i 1 + .   .   8.09
    i 1 + .   .   9.00
    i 1 + .   .   8.11
    i 1 + .   .   9.02

    i 1 0 1 0.5 8.00
    i 1 + . .   7.04
    i 1 + . .   7.06
    i 1 + . .   7.07
    ''')

with measure(8):
    score.write('''
    i 1 0 0.5 0.5 9.00
    i 1 + .   .   8.11
    i 1 + .   .   8.09
    i 1 + .   .   8.07
    i 1 + .   .   8.06
    i 1 + .   .   8.09
    i 1 + .   .   8.07
    i 1 + .   .   8.11

    i 1 0 0.5   0.5 7.09
    i 1 1 .   .   7.11
    i 1 2 2.5 .   8.00
    ''')

with measure(9):
    score.write('''
    i 1 0 1    0.5 8.09
    i 1 + .    .   8.02
    i 1 + 0.25 .   9.00
    i 1 + 0.25 .   8.11
    i 1 + 1    .   9.00
    i 1 + 0.5  .   9.02

    i 1 0.5 0.5 0.5 7.02
    i 1 +   .   .   7.04
    i 1 +   .   .   7.06
    i 1 +   .   .   7.07
    i 1 +   .   .   7.04
    i 1 +   .   .   7.06
    i 1 +   .   .   7.02
    ''')

with measure(10):
    score.write('''
    i 1 0 0.5 0.5 8.11
    i 1 + .   .   8.09
    i 1 + .   .   8.07
    i 1 + .   .   8.06
    i 1 + .   .   8.04
    i 1 + .   .   8.07
    i 1 + .   .   8.06
    i 1 + .   .   8.09

    i 1 0 1 0.5 7.07
    i 1 + . .   6.11
    i 1 + . .   7.00
    i 1 + . .   7.02
    ''')

with measure(11):
    score.write('''
    i 1 0 0.5 0.5 8.07
    i 1 + .   .   8.11
    i 1 + .   .   8.09
    i 1 + .   .   9.00
    i 1 + .   .   8.11
    i 1 + .   .   9.02
    i 1 + .   .   9.00
    i 1 + .   .   9.04

    i 1 0 1 0.5 7.04
    i 1 + . .   7.06
    i 1 + . .   7.07
    i 1 + . .   7.04
    ''')

with measure(12):
    score.write('''
    i 1 0 0.5  0.5 9.02
    i 1 + 0.25 .   8.11
    i 1 + .    .   9.00
    i 1 + 0.5  .   9.02
    i 1 + .    .   9.07
    i 1 + 0.25 .   8.11
    i 1 + .    .   9.00
    i 1 + 0.5  .   8.11
    i 1 + .    .   8.09
    i 1 + .    .   8.07

    i 1 0 1.5 0.5 7.11
    i 1 + 0.5 .   8.00
    i 1 + 1   .   8.02
    i 1 + .   .   7.02
    ''')

with measure(13):
    score.write('''
    i 1 0 1 0.5 8.07

    i 1 0 1 0.5 7.07
    ''')

score.end()

</CsScore>
</CsoundSynthesizer>
