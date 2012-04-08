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

from math import sin, pi

def simulated_lfo(null, freq, min=0.0, max=1.0):
    v = (sin(cue.now() * freq * 2 * pi) + 1) / 2.0
    return v * (max - min) + min

p_callback('i', 1, 4, simulated_lfo, 0.666, 0.125, 0.75)
p_callback('i', 1, 5, simulated_lfo, 0.111, 110, 880)
p_callback('i', 1, 6, simulated_lfo, 0.333)

note_duration = 0.125
phrase_duration = 32
time = 0

while time < phrase_duration:
    with cue(time):
        event_i(1, 0, note_duration * 1.5, 0, 0, 0)

    time += note_duration

</CsScore>
</CsoundSynthesizer>
