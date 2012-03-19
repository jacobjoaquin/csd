#!/usr/bin/python
import re

def cpspch(p):
    octave, note = divmod(p, 1)
    return 440 * 2 ** (((octave - 8) * 12 + ((note * 100) - 9)) / 12.0)

def dB(x):
	return 10 ** (x / 20.0)

def conv_to_hz(x):
	return midi_to_hz(conv_to_midi(x))

def conv_to_midi(note):
	'''Conventional Notation to MIDI'''

	accident = 0
	values = dict(zip('CDEFGAB', [0, 2, 4, 5, 7, 9, 11]))
	m = re.match(r"([A-G])(bb|b|##|#)?(\d+){1,2}", note)	
	
	if m.group(1) and m.group(3):
		if m.group(2):
			if m.group(2)[0] == 'b':
				accident = len(m.group(2)) * -1
			else:
				accident = len(m.group(2))

	return values[m.group(1)] + (int(m.group(3)) + 1) * 12 + accident

def midi_to_hz(x):
	'''MIDI to hz'''
	
	return 440 * 2 ** ((x - 69.0) / 12.0)
