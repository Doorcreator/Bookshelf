# V1: 区间折半法
def half_intval(n1,n2):
	h = (n2-n1)/2
	return [n1,n1+h,n2]
def get_root(n):
	n1=0;n2=n
	lst=[]
	while True:
		new_intval = half_intval(n1,n2)
		s01=new_intval[0]*new_intval[0]
		s02=new_intval[1]*new_intval[1]
		s03=new_intval[2]*new_intval[2]
		if n>=s01 and n<=s02:
			half_intval(new_intval[0],new_intval[1])
			n1=new_intval[0]
			n2=new_intval[1]
		else:
			half_intval(new_intval[1],new_intval[2])
			n1=new_intval[1]
			n2=new_intval[2]
		lst.append((n1,n2))
		if lst[-1][1]*lst[-1][1] == n or (len(lst)>1 and lst[-1] == lst[-2]):
			break
	return lst[-1][1]
def pre_test(n):
	if n<1:
		digit = len(str(n).split('.')[-1])
		numerator = n*(10**digit)
		denominator = 10**digit
		result = get_root(numerator)/get_root(denominator)
	else:
		result = get_root(n)
	return result

# V2: 牛顿迭代法（Newton Iteration）
def get_root(n):
	# When n is greater than 3, setting the initial x1 to the following will refine the performance.
	# digit=len(str(n).split('.')[0])
	# x1=10**(digit/2)
	x1=1
	lst=[]
	while True:
		x2=x1/2+n/(2*x1)
		x1=x2
		lst.append(x2)
		if len(lst) >= 2 and lst[-1]==lst[-2]:
			break
	return lst[-1]