<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 2
0dbfs = 1.0

instr 1
	p3 = 0.35
	idur = p3
	iamp = p4 * 0.478

	kenv1 expseg 900, 0.01, 50, idur - 0.01, 44
	asig1 oscil3 1, kenv1, 1
	kenv2 line 1, idur, 0
	asig1 = asig1 * kenv2

	asig2 gauss 1
	kenv5 expseg 800, 0.1, 50, idur - 0.1, 44
	asig2 tone asig2, kenv5
	
	amix = asig1 + asig2
	
	kenv5 expseg 500, 0.05, 60, idur - 0.05, 44
	amix rezzy amix, kenv5, 10

	kenv6 linseg 55, idur, 44
	aosc oscil3 1, kenv6, 1

	kenv4 expon 2, idur, 1
	kenv4 = kenv4 - 1

	amix = (amix * 0.8 + aosc * 1.2) * kenv4 * iamp
	outs amix, amix
endin

instr 2
	p3 = 0.15
	idur = p3
	iamp = p4 * 0.358
	ivalue = p4 * 0.308
	
	atri oscil3 1, 111 + ivalue * 5, 2	
	areal, aimag hilbert atri

	ifshift = 175
	asin oscil3 1, ifshift, 1	
	acos oscil3 1, ifshift, 1, .25	
	amod1 = areal * acos
	amod2 = aimag * asin
	ashift1 = (amod1 + amod2) * 0.7

	ifshift2 = 224
	asin oscil3 1, ifshift2, 1	
	acos oscil3 1, ifshift2, 1, .25	
 	amod1 = areal * acos
	amod2 = aimag * asin
	ashift2 = (amod1 + amod2) * 0.7
	
	kenv1 line 1, 0.15, 0
	ashiftmix = (ashift1 + ashift2) * kenv1
	
	aosc1 oscil3 1, 180, 1
	aosc2 oscil3 1, 330, 1
	kenv2 linseg 1, 0.08, 0, idur - 0.08, 0
	aoscmix = (aosc1 + aosc2) * kenv2

	anoise gauss 1
	anoise butterhp anoise, 2000
	anoise butterlp anoise, 3000 + ivalue * 3000
	anoise butterbr anoise, 4000, 200
	kenv3 expon 2, 0.15, 1
	anoise = anoise * (kenv3 - 1)
	
	amix = aoscmix + ashiftmix + anoise * 4
	amix = amix * iamp 
	out amix, amix
endin

instr 3 
	p3 = 0.07
	idur = p3
	iamp = p4
	ivalue = p4

	ifreq = 125 + ( 2 * ivalue )
	a1 oscil 1, ifreq * 1, 5
	a2 oscil 1, ifreq * 2.333, 5
	a3 oscil 1, ifreq * 3.578, 5
	a4 oscil 1, ifreq * 5.123, 5
	a5 oscil 1, ifreq * 7.632, 5
	a6 oscil 1, ifreq * 9.843, 5
	amix1 = a1 + a2 + a5	
	amix2 = a3 + a4 + a6

	idecay1 = 0.08 + (0.03 * (1 - ivalue))
	kenv1 expseg 2, 0.01, 2, 0, 1.6, idecay1, 1, idur - idecay1 - 0.01, 1
	kenv1 = kenv1 - 1
	amix1 = amix1 * kenv1
	amix2 = amix2 * kenv1
	
	idecay2 = 0.11 + 0.05 * ivalue
	kenv2 linseg 1, idecay2, 0, idur - idecay2, 0
	anoise gauss 1

	amix1 = (anoise * kenv2) + amix1 * 0.5
	amix1 butterhp amix1, 7000	
	amix1 butterlp amix1, 9000 + ivalue * 3000

	amix2 = (anoise * kenv2) + amix2 * 0.5
	amix2 butterhp amix2, 7000	
	amix2 butterlp amix2, 9000 + ivalue * 3000
	
	amix1 = amix1 * iamp
	amix2 = amix2 * iamp
	out amix1, amix2
endin

</CsInstruments>
<CsScore bin="./pysco.py">

# Import choice from python library
from random import choice
from math import sin
from math import pi

# Create wrapper functions for instruments.
def kick(amp=0.25): score('i 1 0 1 %f' % amp)
def snare(amp=0.25): score('i 2 0 1 %f' % amp)
def hat(amp=0.15): score('i 3 0 1 %f' % amp)

def pattern(r=0.0):
	'''Simple drum pattern'''

	with cue(0): kick()
	with cue(1): snare()
	with cue(2.5): kick()
	with cue(3): snare()

	for i in range(8):
		amp = i % 2 * 0.1 + 0.05
		with cue(i * 0.5): hat(amp)

	# Algorithmic sugar
	for t in [0.5, 0.75, 1.5, 2, 3.5, 3.75]:
		if random() < r:
			with cue(t):
				instr = choice([kick, snare])
				instr(random() * 0.25)

def section():
	'''A 4-bar section'''

	with cue(0): pattern()
	with cue(4): pattern(0.25)
	with cue(8): pattern()
	with cue(12): pattern(0.9)

def swing_test(x):
	int, frac = divmod(x, 1)
	return int + sin(frac * (pi / 2.0))

# "Turn it up!" - Abe Simpson
# Bind amplitude processors callbacks to mix instruments.
bind('a', 'i', 1, 4, lambda x: x * 2.5)
bind('b', 'i', 2, 4, lambda x: x * 2.0)
bind('c', 'i', 3, 4, lambda x: x * 1.5)

# f-tables and tempo
score('''
f 1 0 [2^16+1] 10 1
f 2 0 8192 -7 -1 4096 1 4096 -1
f 5 0 8192 -7 1 200 1 0 -1 7912 -1
t 0 120
''')

for i in range(0, 256, 16):
	with cue(i): section()

# Swing it!
pmap('i', [1, 2, 3], 2, swing_test)
</CsScore>
</CsoundSynthesizer>
