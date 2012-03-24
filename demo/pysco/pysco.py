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

# Stores score output
_sco = []
exec_block = []
time_stack = [0]
f = ''

def debug_m(m, v=''):
	print m + ': '
	print v

def do_exec(code, g={}, l={}):
	'''Ugly. Picks between eval and exec.'''

	redirect_out = StringIO()
	stdout_temp = sys.stdout
	sys.stdout = redirect_out
	try:
		return eval(code, g, l)
	except:
		try:
			exec(code, g, l)
		except:
			pass

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
	debug_m('score(): ', s)
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


def _parse_timestack():
	global f
	global exec_block

	debug_m('inside _parse_timestack')

	for line in f.readlines():
		debug_m('line', line)
		tokens = line.split()

		if tokens and tokens[0][0] == '@':
			debug_m('exec timestack', exec_block)

			# Execute Python code in exec buffer
			exec("\n".join(exec_block))
			exec_block = []

			# Get position of ':'
			stripped = line.strip()
			pos = stripped.index(':')
			debug_m('@ var', stripped[1:pos])
				



			e = do_exec(stripped[1:pos])
			debug_m('do_exec', e)
			debug_m('type(e)', type(e))

			if type(e) in [int, float]:
				debug_m('type int/float', e)
				time_stack.append(float(e))
				exec(stripped[pos + 1:].strip())
				time_stack.pop()
			elif type(e) == list:
				debug_m('type list', e)
				for _i in e:
					time_stack.append(float(_i))
					exec(stripped[pos + 1:].strip())
					time_stack.pop()

		else:
			debug_m('exec_block', exec_block)
			exec_block.append(line)


# Begin
def main():
	global f
	global exec_block
	debug_m('--- Begin pysco ---')

	f = open(argv[1], 'r')


	debug_m('pre _parse_timestack')
	_parse_timestack()
	debug_m('post _parse_timestack')

	if len(exec_block) >= 1:
		debug_m('exec final block', exec_block)
		exec("\n".join(exec_block))
		exec_block = []

	f.close();


	debug_m('final _sco:', _sco)
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

if __name__ == '__main__':
	main()
else:
	main()
