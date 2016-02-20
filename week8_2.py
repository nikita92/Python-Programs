fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	line= line.rstrip()
	words=line.split()
	for i in words:
		if i in lst:        
			continue               
		else :                     
			lst.append(i)
lst.sort()
print lst