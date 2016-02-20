#!/usr/bin/python
import sys
import binascii
import struct

BLOCKSIZE = 128
TOTALSIZE = 1024
NB=TOTALSIZE/BLOCKSIZE

LeftMatrixBlock = []
RightTransposeMatrixBlock = []

#total number of lines(within a block)
nl = 0
#old block number=-1
blockno = -1

LeftMatrixBlock=[[0 for col in range(TOTALSIZE)] for row in range(BLOCKSIZE)]
RightTransposeMatrixBlock=[[0 for col in range(TOTALSIZE)] for row in range(BLOCKSIZE)]

#comenting this to read input from a file
#for line in sys.stdin:
inputfile = open('MatAInput.txt')
for line in inputfile:
	#for debug
	nl = nl + 1
	#remove leading and trailing whitespace
	line = line.strip()
	#parse the input
	input_key, input_value = line.split('\t', 1)
	blockno = int(input_key)
	print >>sys.stderr , line
    
	A_B, index, row_value = input_value.split(':')
	if A_B == "L":
		LeftMatrixBlock[int(index)%BLOCKSIZE]=row_value.split(' ')
	if A_B == "R":
		RightMatrixBlock[int(index)%BLOCKSIZE]=row_value.split(' ') 

	#if a block is finished
	if(n1 == 2*BLOCKSIZE):
		print >> sys.stderr, LeftMatrixBlock
		print >> sys.stderr, RightTransposeMatrixBlock
		#reset n1
		n1 = 0
		
		#pint block number to mark the output
		print blockno, BLOCKSIZE
		
		#output & multiply and sum 
		res = [[0 for col in range(BLOCKSIZE)] for row in range(BLOCKSIZE)]
		for i in range(BLOCKSIZE):
			for j in range(BLOCKSIZE):
				for k in range(TOTALSIZE):
					left_val = struct_unpack("!f",binascii,a2b_hex(LeftMatrixBlock[i][k]))[0]
					right_val = struct_unpack("!f",binascii,a2b_hex(RightTransposeMatrixBlock[j][k]))[0]
					res[i][j] = res[i][j] + left_val*right_val
				print res[i][j]
			print
		#del LeftMatrixBlock[:]
		#del RightTransposeMatrixBlock[:]
		

