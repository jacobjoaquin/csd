#!/usr/bin/python
from sys import argv
from convert import *
import csd
from csd import sco
from random import random

class Slipmat():
	def __init__(self):
		self.slipcue = Slipcue()
		self.score_data = []
		self.callback_dict = {}

	def event_i(self, *args):
		output = ['i']

		for arg in args:
			output.append(str(arg))

		self.score(' '.join(output))

	def pmap(self, statement, identifier, pfield, formula):
		self.score_data = [csd.sco.map_("\n".join(self.score_data), {0: statement, 1: identifier}, pfield, formula)]

	def score(self, data):
		for k, v in self.callback_dict.iteritems():
			data = csd.sco.map_(data, {0: v['statement'], 1: v['identifier']}, v['pfield'], v['func'])

		selected = sco.select(data, {0: 'i'})
		op = sco.selection.operate_numeric(selected, 2, lambda x: x + self.slipcue.now())

		self.score_data.append(sco.merge(data, op))

	def bind(self, name, statement, identifier, pfield, func):
		self.callback_dict[name] = {
			'statement' : statement,
			'identifier' : identifier,
			'pfield' : pfield,
			'func' : func
		}

class Slipcue(object):
	def __init__(self):
		self.stack = []

	def __call__(self, when):
		self.when = when
		return self

	def __enter__(self):
		self.stack.append(self.when)
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.stack.pop()
		return False

	def now(self):
		return sum(self.stack)

def debug(m, v=''):
	print m + ': ' + str(v),


# Globals
slipmat = Slipmat()
cue = slipmat.slipcue
score = slipmat.score
pmap = slipmat.pmap
bind = slipmat.bind
event_i = slipmat.event_i

def main():
	# Execute CsScore
	execfile(argv[1], globals())

	# Create score string
	sco_output = "\n".join(slipmat.score_data)

	# Write score used by Csound
	with open(argv[2], 'w') as f:
		f.write(sco_output)

	# Additional file for development testing
	with open('dev.sco', 'w') as f:
		f.write(sco_output)

if __name__ == '__main__':
	main()
