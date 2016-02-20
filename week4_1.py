hrs = raw_input("Enter Hours:")
h = float(hrs)
rate=raw_input("enter rate:")
r=float(rate)
def computepay(h,r):
	pay= 40*r + (((h-40)*1.5*r))
	return pay
if h<=40:
	pay=h*r
	print pay
if h>40:
	final=computepay(h,r)
	print final
