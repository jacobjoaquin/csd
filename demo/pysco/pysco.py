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

class TimeStack:
	def __init__(self):
		self.stack = []
		self.indent = ''
	
	def pop(self):
		self.stack.pop()

	def append(self, t):
		self.stack.append(t)

	def time(self):
		return sum(self.stack)

def debug(m, v=''):
	print m + ': ' + str(v),

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
	global _sco
	global time_stack
	#selected = sco.select_all(s)
	selected = sco.select(s, {0: 'i'})
	print s
	print time_stack
	print selected
	foo = sco.selection.operate_numeric(selected, 2, lambda x: x + time_stack.time())
	s = sco.merge(s, foo)
	_sco.append(s)

def append_score(when, what, indent=''):
	line = []

	if type(when) in [int, float]:
		line.append('time_stack.append(' + str(when) + ')')
		line.append(what.strip())
		line.append('time_stack.pop()')

		for L in line:
			debug('REPL', indent + L + "\n")
			exec_block.append(indent + L + "\n")

	elif type(when) == list:
		for i in when:
			append_score(i, what)

def _parse_timestack():
	global f
	global exec_block

	for line in f.readlines():
		debug('line', line)
		tokens = line.strip().split()

		if tokens and tokens[0][0] == '@':
			# <WHITESPACE>@<WHEN>: <WHAT> 
			pattern = re.compile("(\s*)@(.+):(.+)")
			match = pattern.match(line)
	
			if match:
				indent = match.group(1)
				when = eval(match.group(2))
				what = match.group(3)
				append_score(when, what, indent)
			else:
				debug('WARNING', 'No match found')

		else:
			exec_block.append(line)


# Stores score output
_sco = []
exec_block = []
time_stack = TimeStack() 
f = ''

# Begin
def main():
	global f
	global exec_block
	debug('Begin pysco.py')

	f = open(argv[1], 'r')
	_parse_timestack()

	if len(exec_block) >= 1:
		#debug('exec final block', exec_block)
		exec("\n".join(exec_block))
		exec_block = []

	f.close();

	debug('final _sco:', _sco)
	# Output preprocessed score
	output = open(argv[2], 'w')
	output.write("\n".join(_sco))
	output.close

	# Print to extra file for testing purposes
	output = open('current.sco', 'w')
	output.write("\n".join(_sco))
	output.close

	# End
	debug('--- End pysco ---')

if __name__ == '__main__':
	main()
else:
	main()
