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

# THIS EXAMPLE DOESN'T WORK
#print "\n\n\n\n\nTHIS EXAMPLE DOESN'T WORK\n\n\n\n"
#exit(1)

score('''
f 1 0 8192 10 1
t 0 120

i 1 0 0.5 -3 D5 
i 1 + .   .  G4 
i 1 + .   .  A4
i 1 + .   .  B4
i 1 + .   .  C5
i 1 + .   .  A4
i 1 + .   .  B4
i 1 + .   .  G5
''')

pmap('i', 1, 4, dB)

def pmap_string(statement, identifier, pfield, func, convert_numeric=True):
	global slipmat

	# Convert pfield to list if it isn't one
	if type(pfield) != list:
		pfield = [pfield]

	the_score = "\n".join(slipmat.score_data)
	debug('the_score', the_score)

	selection = sco.select(the_score, {0: statement, 1: identifier})
	debug('selection', selection)

	for k, v in selection.iteritems():
		debug('k, v', str(k) + ', ' + str(v))

		for p in pfield:
			element = sco.event.get(v, p)
			debug('element', element) 

			value = func(element)
			debug('value', value)

			new_event = sco.event.set(v, p, value)
			debug('new_event', new_event)

			selection[k] = new_event

	debug('selection processed', selection)

	merged = sco.merge(the_score, selection)
	debug('merged', merged)

	slipmat.score_data = [merged]

	


pmap_string('i', 1, 5, conv_to_hz)

#exit(1)
</CsScore>
</CsoundSynthesizer>
