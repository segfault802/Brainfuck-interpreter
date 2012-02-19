#!/usr/bin/python2
#a brainfuck interpreter written in python
import sys




def run(instr):
	tape = [0]
	head = 0
	iptr = 0
	keepAlive = True
	symbol = instr[0]
	while(keepAlive and symbol):
		#sys.stdout.write('> ')
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
		elif(symbol == '['):
			if(tape[head] == 0):
				while(symbol != ']'):
					iptr += 1
					symbol = instr[ptr]
		elif(symbol == ']'):
			if(tape[head] != 0):
				while(symbol != '['):
					iptr -= 1
					symbol = instr[iptr]					
		elif(symbol == 'x'):
			keepAlive = False
		else:		
			print 'Symbol not recognized, ignoring'
		iptr += 1
		if(iptr == len(instr)):
			keepAlive = False
		else:
			symbol = instr[iptr]		
		#print tape


f = open('hello.txt','r')
instructions = []
for byte in f.read():
	instructions.append(byte)
#print instructions
run(instructions)

