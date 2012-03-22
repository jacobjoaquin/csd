#!/usr/bin/python
from sys import argv
from convert import *
import csd
import re
from csd import sco
from random import random

# Stores score output
_sco = []
time_stack = [0]



def debug_m(m, v=''):
	print m + ': '
	print v
	print

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
	global time_stack
	#selected = sco.select_all(s)
	selected = sco.select(s, {0: 'i'})
	print s
	print time_stack
	print selected
	foo = sco.selection.operate_numeric(selected, 2, lambda x: x + time_stack[-1])
	s = sco.merge(s, foo)
	_sco.append(s)

def _parse():
		exec_block = []

		for line in f.readlines():
			pfields = line.split()

			if len(pfields) and len(pfields[0]) == 1:
				print 'sco: ' + line
				_sco.append(line)

				if len(exec_block) >= 1:
					print exec_block
					exec("\n".join(exec_block))
					exec_block = []
			else:
				print 'py:  ' + line
				exec_block.append(line)

		if len(exec_block) >= 1:
			print exec_block
			exec("\n".join(exec_block))
			exec_block = []


# Begin
debug_m('--- Begin pysco ---')

f = open(argv[1], 'r')

foo = f.read()
exec(foo)

f.close();

debug_m('_sco', _sco)

# Output preprocessed score
output = open(argv[2], 'w')
output.write("\n".join(_sco))
output.close

# Print to extra file for testing purposes
output = open('current.sco', 'w')
output.write("\n".join(_sco))
output.close

# End
debug_m('--- End pysco ---')

