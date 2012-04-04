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

	def __map_process(self, data, statement, identifier, pfield, func, *args, **kwargs):
		convert_numeric = True
		sco_statements_enabled = True

		# Convert pfield to list if it isn't one
		if type(pfield) != list:
			pfield = [pfield]

		selection = sco.select(data, {0: statement, 1: identifier})

		for k, v in selection.iteritems():
			for p in pfield:
				element = sco.event.get(v, p)

				# Bypass if score statement like carry
				# TODO: ^+x, npx, ppx, etc...
				if sco_statements_enabled and element in ['.', '+', '<', '!']:
					break

				# Convert value to float
				if convert_numeric:
					try:
						element = float(element)
					except:
						pass

				deez_args = (element,) + args
				selection[k] = sco.event.set(v, p, func(*deez_args, **kwargs))

		return sco.merge(data, selection)

	def bind(self, name, statement, identifier, pfield, func, *args, **kwargs):
		self.callback_dict[name] = {
			'statement' : statement,
			'identifier' : identifier,
			'pfield' : pfield,
			'func' : func,
			'args' : args,
			'kwargs' : kwargs,
			'enabled' : True
		}

	def bind_enabled(self, name, value):
		if name in self.callback_dict:
			self.callback_dict[name]['enabled'] = value

	def event_i(self, *args):
		output = ['i']

		for arg in args:
			output.append(str(arg))

		self.score(' '.join(output))

	def pmap(self, statement, identifier, pfield, func, *args, **kwargs):
		data = "\n".join(self.score_data)
		self.score_data = [self.__map_process(data, statement, identifier, pfield, func, *args, **kwargs)]

	def score(self, data):
		# Apply callbacks
		for k, v in self.callback_dict.iteritems():
			if v['enabled']:
				data = self.__map_process(data, v['statement'], v['identifier'], v['pfield'], v['func'], *v['args'], **v['kwargs'])

		# Apply time stack
		selected = sco.select(data, {0: 'i'})
		op = sco.selection.operate_numeric(selected, 2, lambda x: x + self.slipcue.now())
		self.score_data.append(sco.merge(data, op))

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
	print m + ': ' + str(v) + "\n",

# Globals
slipmat = Slipmat()
cue = slipmat.slipcue
score = slipmat.score
pmap = slipmat.pmap
bind = slipmat.bind
bind_enabled = slipmat.bind_enabled
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
