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

def grain_gen(time, dur):
	end_time = time + dur
	base_freq = random() * 100 + 200

	while time < end_time:
		grain_dur = random() * 0.1 + 0.02
		amp = random() * 0.0125
		freq = base_freq * (3 ** (int(random() * 26) / 13.0) )
		i_event(2, time, grain_dur, amp, freq)
		time += random() * 0.1 + 0.01

score('''
f 1 0 8192 10 1
t 0 120

i 1 0 0.5 -3 9.02
i 1 + .   .  8.07
i 1 + .   .  8.09
i 1 + .   .  8.11
i 1 + .   .  9.00
i 1 + .   .  8.09
i 1 + .   .  8.11
i 1 + .   .  8.07
''')

for i_ in range(5):
	 grain_gen(i_ * 3, 2)

pmap('i', 1, 4, dB)
pmap('i', 1, 5, cpspch)

</CsScore>
</CsoundSynthesizer>
