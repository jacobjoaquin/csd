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

    a1 oscil iamp, ifreq, 1
    outs a1 * sqrt(1 - ipan), a1 * sqrt(ipan)
endin

</CsInstruments>
<CsScore bin="./pysco.py">

def dusty_vinyl(dur, amp, freq_min, freq_max, density):
	for i in range(int(density * dur)):
		freq = random() * (freq_max - freq_min) + freq_min
		t = random() * dur 
		event_i(1, t, 1 / freq, amp, freq, random())
		
score(' f 1 0 8192 10 1')

with cue(0):
	dusty_vinyl(4, 0.5, 8000, 9000, 50)

with cue(4):
	dusty_vinyl(4, 0.5, 4000, 10000, 15)

with cue(8):
	dusty_vinyl(4, 0.5, 1000, 12000, 5)

with cue(12):
	dusty_vinyl(4, 0.5, 500, 16000, 55)

</CsScore>
</CsoundSynthesizer>
