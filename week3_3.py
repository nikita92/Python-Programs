try:
	istr=raw_input("enter a number between 0 and 1")
	score=float(istr)
	if score<=1:
		if score>=0.9:
			print 'A'
		if score>=0.8:
			print 'B'
		if score>=0.7:
			print 'C'
		if score>=0.6:
			print 'D'
		if score<0.6:
			print 'F'
	else:
		print 'Error'
except:
	print 'Please enter a valid number'
