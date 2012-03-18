#!/usr/bin/python

def cpspch(p):
    octave, note = divmod(p, 1)
    return 440 * 2 ** (((octave - 8) * 12 + ((note * 100) - 9)) / 12.0)

def dB(x):
	return 10 ** (x / 20.0)






