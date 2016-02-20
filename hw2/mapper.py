#!/usr/bin/env python
import sys

#BLOCKSIZE must be the integral power of two
BLOCKSIZE = 128
TOTALSIZE = 1024

#number of bloacks for Matrix A/B
NB = (int)(TOTALSIZE/BLOCKSIZE)

for line in sys.stdin:
	#remove leading and trailing whotespace
	line = line.strip()
	
	#parse the input
	A_B, lineno, row_value = line.split(' ',2)
	if A_B == 'L':
		ib = (int)(lineno)/BLOCKSIZE
		for jb in range(NB):
			#the key is the BLOCK Number
			intermediate_key = '%05d'%(ib*NB+jb)
			#the value is the {L/R} : {LineNo}: {values of the current line}
			intermediate_value = "L:%s:%s"%(lineno, row_value)
			#key and value are seperated by a tab
			#print "%s\t%s"%(intermediate_key,intermediate_value)
			print(intermediate_key+'\t'+intermediate_value)
		if A_B =='R':
			jb = (int)(lineno)/BLOCKSIZE;
			for ib in range(NB):
				intermediate_key = "%0.5d"%(ib*NB+jb)
				intermediate_value = "R:%s:%s"%(lineno, row_value)
				#print "%s\t%s"%(intermediate_key,intermediate_value)
				print(intermediate_key+'\t'+intermediate_value)
			
			
			
			
			
			