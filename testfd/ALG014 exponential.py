def exp(x,n):
	i=0
	r=1
	while i<n:
		r*=x
		i+=1
	return r
def expn(x,n):
	if n==0:
		return 1
	elif n%2==0:
		return expn(x,n/2)*expn(x,n/2)
	elif n%2!=0:
		return x*expn(x,n-1)