#!/usr/bin/python
from sys import argv
from convert import *
import csd
import re
from csd import sco
from random import random
import StringIO
from StringIO import StringIO
import sys

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
	debug('score()', s)
	selected = sco.select(s, {0: 'i'})
	op = sco.selection.operate_numeric(selected, 2, lambda x: x + sum(t.stack))
	s = sco.merge(s, op)

	debug('score() merged', s)
	_sco.append(s)

	debug('_sco', _sco)

# Globals
_sco = []

# Begin
def main():
	# Execute CsScore
	execfile(argv[1], globals())

	# Clean output
	clean_split = _sco[0].splitlines()
	clean = []


	for L in clean_split:
		clean.append(L.strip())

	clean = _sco

	debug("\n_sco final\n", clean)

	# Output preprocessed score
	output = open(argv[2], 'w')
	output.write("\n".join(clean))
	output.close

	# Print to extra file for testing purposes
	output = open('current.sco', 'w')
	output.write("\n".join(clean))
	output.close

	# End
	debug('--- End pysco ---')

if __name__ == '__main__':
	main()
else:
	main()
