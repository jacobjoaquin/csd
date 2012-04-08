<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 2
0dbfs = 1.0

instr 1
    idur = p3   ; Duration
    iamp = p4   ; Amplitude
    ifreq = p5  ; Frequency
    ipan = p6   ; Pan

    kenv line iamp, idur, 0       ; Line envelope
    a1 vco2 kenv, ifreq, 12, 0.5  ; Triangle wave

    outs a1 * sqrt(1 - ipan), a1 * sqrt(ipan)
endin

</CsInstruments>
<CsScore bin="./pysco.py">

from random import random

def pan_cycle(x):
    global positions
    global pos
    pos = (pos + 1) % len(positions)  
    return positions[pos]

def phrase_delay(phrase, delay_time=1, feedback=0.5):
    if not isinstance(delay_time, list):
        delay_time = [delay_time]

    f = feedback
    score(phrase)

    for d in delay_time:
        with cue(d):
            p_callback('i', 1, 4, lambda x: x * f)
            score(phrase)

        f *= feedback

# Conver pch notation to Hz
p_callback('i', 1, 5, cpspch)

# My musical phrase
my_phrase = '''
i 1 0 1.5  0.707 8.00 0.5
i 1 + 0.5  .     7.07 0.5
i 1 + 1.5  .     8.02 0.5
i 1 + 0.5  .     8.03 0.5
i 1 + 1    .     7.08 0.5
i 1 + 0.25 .     7.07 0.5
i 1 + 0.25 .     7.11 0.5
i 1 + 0.25 .     8.03 0.5
i 1 + 1.25 .     8.04 0.5
i 1 + 1    .     8.07 0.5
'''

score('t 0 90')

# Bass line
with cue(0):
    for t in xrange(0, 64, 1):
        with cue(t):
            score('i 1 0.01 0.66  0.8 6.00 0.5')
            score('i 1 0    0.125 0.8 7.00 0.5')

# Phrase without event delay effect
with cue(8):
    for t in xrange(0, 16, 8):
        with cue(t):
            score(my_phrase)

# Phrase with event delay effect
with cue(24):
    # Taps for event delay
    times = [0.05, 0.75, 1.333, 1.75]

    for t in xrange(0, 16, 8):
        with cue(t):
            phrase_delay(my_phrase, times, 0.65)

# Phrase with event delay effect plus voice 1 octave lower
with cue(40):
    # Taps for event delay
    fib = map(lambda x: x * 0.1618, [1, 2, 3, 5, 8, 13])

    for t in xrange(0, 16, 8):
        # Create a second voice 1 octave lower with reduced amplitude
        with cue(t):
            p_callback('i', 1, 4, lambda x: x * 0.45)
            p_callback('i', 1, 5, lambda x: x / 2.0)
            score(my_phrase)

        with cue(t):
            phrase_delay(my_phrase, fib, 0.75)

# Bring down volume to prevent clipping
pmap('i', 1, 4, lambda x: x * 0.5)

# Randomize frequencies ever so slightly
pmap('i', 1, 5, lambda x: x * (random() * 0.015 + 0.992))

# Pan cycler
pos = 0
positions = [0.0, 0.333, 0.75, 0.5, 0.25, 0.666, 1.0]
pmap('i', 1, 6, pan_cycle)

</CsScore>
</CsoundSynthesizer>
