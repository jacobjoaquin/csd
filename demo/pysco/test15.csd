<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 4410
ksmps = 10
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

def pan_cycle(x):
    global positions
    global pos
    pos = (pos + 1) % len(positions)  
    return positions[pos]

def phrase_delay(phrase, delay_time=0.75, feedback=0.8):
    if not isinstance(delay_time, list):
        delay_time = [delay_time]

    f = feedback
    score(phrase)

    for d in delay_time:
        with cue(d):
            bind('temp', 'i', 1, 4, lambda x: x * f)
            score(phrase)
            bind_enabled('temp', False)

        f *= feedback

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

pos = 0
positions = [0.0, 0.333, 0.75, 0.5, 0.25, 0.666, 1.0]
times = [0.05, 0.75, 1.333, 1.75]

score('t 0 90')

with cue(8):
    for t in xrange(0, 16, 8):
        with cue(t):
            score(my_phrase)

with cue(24):
    for t in xrange(0, 32, 8):
        with cue(t):
            phrase_delay(my_phrase, times, 0.45)

for t in xrange(0, 64, 1):
    with cue(t):
        score('i 1 0 0.5 0.5 7.00 0.4')
        score('i 1 0 0.5 0.5 6.00 0.4')

pmap('i', 1, 4, lambda x: x * 0.707)
pmap('i', 1, 5, cpspch)
pmap('i', 1, 5, lambda x: x * (random() * 0.015 + 0.992))
pmap('i', 1, 6, pan_cycle)

</CsScore>
</CsoundSynthesizer>
