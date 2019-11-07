from line_profiler import LineProfiler
import math
def pretest(n):
	lst = (2,3,5,7)
	for i in lst:
		if n%i==0 and n not in lst:
			break
		else:
			return 1
def prime(n):
	k=0
	m = int(math.sqrt(n))
	for i in range(2,m+1):
		if n%i==0:
			break
		else:
			k+=1
	if k == m-1:
		return 1
def main(n):
	k=0
	for i in range(2,n+1):
		try:
			if prime(i) == 1:
				k+=1
		except:
			break
	print('There are %s prime numbers!'%k)
# from line_profiler import LineProfiler
# lp = LineProfiler()
# lp.enable_by_count()
# lp_wrapper = lp(main)
# main(100000)
# lp.print_stats()
#total,		primes,	time
#1000,		168,	0.012s
#100000,	9592,	3.78s



