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
	i 1 0 0.5 -3 8.00
	i 1 + .   .  8.03
	i 1 + .   .  8.07
	i 1 + .   .  8.08
	i 1 + .   .  8.07
	i 1 + .   .  8.03
	i 1 + .   .  7.11
	''')

def phrase_2():
	@0: score('i 1 0 2 -6 7.07')
	@1: score('i 1 0 2 -6 8.07')

score('t 0 90')

@[0, 2]: phrase_2()
@[0, 4]: phrase()

pmap('i', 1, 4, dB)
pmap('i', 1, 5, cpspch)
</CsScore>
</CsoundSynthesizer>
