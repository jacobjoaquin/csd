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

instr 2
    idur = p3   ; Duration
    iamp = p4   ; Amplitude
	ifreq = p5  ; Frequency

    aenv linseg 0, idur * 0.5, 1, idur * 0.5, 0
    a1 oscil aenv, ifreq, 1
    out a1
endin

instr 3
    idur = p3   ; Duration
    iamp = p4   ; Amplitude
	ifreq = p5  ; Frequency

    a1 oscil iamp, ifreq, 1
    out a1
endin

</CsInstruments>
<CsScore bin="./pysco.py">

# Test using score method.
def dusty_vinyl(dur, amp, freq_min, freq_max, density):
	for i in range(int(density * dur)):
		freq = random() * (freq_max - freq_min) + freq_min
		t = random() * dur 
		event_i(3, t, 1 / freq, amp, freq)
		
def phrase():
	score('''
	i 1 0 0.5 -7 9.02
	i 1 + .   .  8.07
	i 1 + .   .  8.09
	i 1 + .   .  8.11
	i 1 + .   .  9.00
	i 1 + .   .  8.09
	i 1 + .   .  8.11
	i 1 + .   .  8.07
	''')

score('''
f 1 0 8192 10 1
t 0 120
''')

dusty_vinyl(2, 0.5, 8000, 9000, 50)
with t(3): dusty_vinyl(2, 0.5, 8000, 9000, 15)
with t(6): phrase()

pmap('i', 1, 4, dB)
pmap('i', 1, 5, cpspch)
</CsScore>
</CsoundSynthesizer>
