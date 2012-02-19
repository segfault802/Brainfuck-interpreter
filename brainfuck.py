#!/usr/bin/python2
#a brainfuck interpreter written in python
import sys


#initially, just prcess symbols from stdin until an exit symbol is read
def run(stream):
	tape = [0]
	head = 0
	iptr = 0
	keepAlive = True
	while(keepAlive):
		output = ''
		#sys.stdout.write('> ')
		symbol = raw_input('> ')
		#print len(symbol)
		#symbol = symbol[2:-1]		
		#print symbol
		#symbol = symbol.rstrip()
		if(symbol == '>'):
			head += 1
			if(head >= len(tape)):
				tape.append(0)
		elif(symbol == '<'):
			head -= 1
			if(head < 0):
				head = 0	
		elif(symbol == '+'):
			tape[head] += 1
			if(tape[head] > 255):
				tape[head] = tape[head] % 255 #overflow
		elif(symbol == '-'):
			tape[head] -= 1
			if(tape[head] < 0):
				tape[head] = 0
		elif(symbol == 	'.'):
			c = chr(tape[head])
			sys.stdout.write(c)
		elif(symbol == ','):
			c = raw_input()
			tape[head] = ord(c)		
		elif(symbol == 'x'):
			keepAlive = False
		else:		
			print 'Symbol not recognized'
			keepAlive = False
		iptr += 1		
		print tape


run(sys.stdin)

