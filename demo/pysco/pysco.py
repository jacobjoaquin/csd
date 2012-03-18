#!/usr/bin/python
from sys import argv
from convert import *
import csd
import re
from csd import sco
from random import random

# Stores score output
_sco = []

def debug_m(m, v=''):
	print m + ': '
	print v
	print

def i_event(*args):
	global _sco

	output = ['i']

	for arg in args:
		output.append(str(arg))

	output.append("\n")
	_sco.append(' '.join(output))

def pmap(statement, identifier, pfield, formula):
	global _sco
	_sco = [csd.sco.map_("\n".join(_sco), {0: statement, 1: identifier}, pfield, formula)]

# Begin
debug_m('--- Begin pysco ---')

# Read template from <CsScore>
f = open(argv[1], 'r')

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

f.close();

debug_m('_sco', _sco)

# Output preprocessed score
output = open(argv[2], 'w')
output.write("\n".join(_sco))

# End
debug_m('--- End pysco ---')
