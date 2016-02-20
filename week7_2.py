fname=raw_input('enter file name')
fhand= open(fname)
sum=0
count=0
for line in fhand:
	line=line.rstrip()
	if not line.startswith("X-DSPAM-Confidence:") :
		continue
	str= line[20:]
	str1=float(str)
	sum=sum+str1
	count=count+1
print "Average spam confidence:", sum/count
