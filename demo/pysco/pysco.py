#!/usr/bin/python
from sys import argv
from convert import *
import csd
from csd import sco
from random import random

class t(object):
	stack = []

	def __init__(self, when):
		self.when = when

	def __enter__(self):
		t.stack.append(self.when)

		return self

	def __exit__(self, *exc):
		t.stack.pop()

		return False
	
def debug(m, v=''):
	print m + ': ' + str(v),

def i_event(*args):
	global _sco

	output = ['i']

	for arg in args:
		output.append(str(arg))

	score(' '.join(output))

def pmap(statement, identifier, pfield, formula):
	global _sco

	_sco = [csd.sco.map_("\n".join(_sco), {0: statement, 1: identifier}, pfield, formula)]

def score(s):
	global _sco

	selected = sco.select(s, {0: 'i'})
	op = sco.selection.operate_numeric(selected, 2, lambda x: x + sum(t.stack))
	s = sco.merge(s, op)
	_sco.append(s)

# Globals
_sco = []

def main():
	# Execute CsScore
	execfile(argv[1], globals())

	# Create score string
	sco_output = "/n".join(_sco)

	# Write score used by Csound
	with open(argv[2], 'w') as f:
		f.write(sco_output)

	# Additional file for development testing
	with open('current.sco', 'w') as f:
		f.write(sco_output)

if __name__ == '__main__':
	main()
