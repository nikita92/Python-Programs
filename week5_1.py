count=0
sum=0
while True:
	try:
		line=raw_input('enter something')
		if line=='done':
			break
		num=float(line)
		sum=sum+num
		count=count+1
	except:
		print 'Please enter a valid number'
		
print sum, sum/count