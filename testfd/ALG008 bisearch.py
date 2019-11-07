from line_profiler import LineProfiler
def div_interv(lst):
	dlst = {}
	for e in enumerate(lst):
		dlst[e[0]] = e[1]
	mid = round(len(lst)/2)
	for i in range(mid,0,-1):
		midpoint = dlst[i]
		lower_interv = lst[:i]
		upper_interv = lst[i:]
		break
	return midpoint,lower_interv,upper_interv
def bisearch(t,lst):
	try:
		r = div_interv(lst)
		if t < r[0]:
			return bisearch(t,r[1])
		elif t > r[0]:
			return bisearch(t,r[2])
		elif t == r[0]:
			print('%s is found at position %s.'%(t,[x[0] for x in enumerate(lst) if x[1]==t]))
			# print('%s'%(t))
	except:
		print('%s not found!'%(t))
def ord_search(n,lst):
	dlst = {}
	for e in lst:
		if n == e:
			print(e)
			break
		else:
			print('No')
a = [1,12,20,37,44.3,64,73,78.2,78.2,89,98,99.001,145,183,299,300,899,900.9,1000,1002]
bisearch(37,a)
# ord_search(145,a)
# lp = LineProfiler()
# lp.enable_by_count()
# lp_wrapper = lp(bisearch)
# bisearch(44.3,a) # 0.0003 s
# lp_wrapper = lp(ord_search)
# ord_search(1002,a) # 0.0016
# lp.print_stats()





