# generate m unique random numbers within the range of n1 to n2.
import random
# V01: applicable to the case where m <<< n2-n1.
def rand01(m,n1,n2):
	t=0
	array=[]
	if m>n2-n1+1:
		print('Warning: The first argument [%d] should be smaller than [%d]!'%(m,n2-n1+1))
	else:
		while t<m:
			r = random.randint(n1,n2)
			if r not in array:
				array.append(r)
				t+=1
	return array
# V02: applicable to general purposes, but not so efficient as V03.
def rand02(m,n1,n2):
	t=0
	array=[]
	seed={}
	if m>n2-n1+1:
		print('Warning: The first argument [%d] should be smaller than [%d]!'%(m,n2-n1+1))
	else:
		for i in range(n1,n2+1):
			seed[i]=i
		temp_arr = [v for v in seed.values()]
		while t<m:
			r = random.choice(temp_arr)
			array.append(r)
			temp_arr.remove(r)
			t+=1
	return array
# V03: 
def rand03(m,n1,n2):
    t=0
    seed = {}
    array = []
    for i in range(n1,n2+1):
        seed[i] = i
    if m>n2-n1+1:
        print('Warning: The first argument [%d] should be smaller than [%d]!'%(m,n2-n1+1))
    else:
        while t<m:
            label = random.randint(n1,n2)
            array.append(seed[label])
            if label != n1:
                seed[label]=seed[n1]
                n1+=1
            else:
                n1+=1
            t+=1
    return array
# V04: very efficient when m is rather small and n2 is rather large (more than 2^32).
def rand04(m,n1,n2):
    t=0
    seed = {}
    array = []
    if m>n2-n1+1:
        print('Warning: The first argument [%d] should be smaller than [%d]!'%(m,n2-n1+1))
    else:
        while t<m:
            label = random.randint(n1,n2)
            array.append(seed.get(label,label))
            if label != n1:
                seed[label]=seed.get(n1,n1)
                n1+=1
            else:
                n1+=1
            t+=1
    return array
# V05
def rand05(m,n1,n2):
    r = random.sample(range(n1,n2+1),m)
    return r

from line_profiler import LineProfiler
lp = LineProfiler()
lp.enable_by_count()
lp_wrapper = lp(rand04)
rand04(5*10**6,0,10**9)
lp.print_stats()
# Ver:          V01     V02      V03     V04        V05
# DoM(10^2):    0.0064  0.0017  0.0020   0.0019     0.00087  
# DoM(10^3):    0.20    0.023   0.020    0.019      0.0076
# DoM(10^4):    12      0.82    0.20     0.19       0.076
# DoM(10^5):            65      2.1      1.9        0.78
