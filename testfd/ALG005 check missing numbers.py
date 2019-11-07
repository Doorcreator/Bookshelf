from memory_profiler import profile
import random
# @profile
def rand(m,n1,n2):
	t=0
	s1=[]
	s3={}
	if m>(n2-n1)+1:
		print('Warning: The first argument [%d] should be smaller than [%d]!'%(m,(n2-n1)+1))
	else:
		for i in range(n1,n2+1):
			s3[i]=i
		s2 = [v for v in s3.values()]
		while t<m:
			r = random.choice(s2)
			s1.append(r)
			s2.remove(r)
			t+=1
	return s1
@profile
def check_missing_numbers(m,n1,n2):
	box = set()
	glst = rand(m,n1,n2)
	for i in range(n1,n2+1):
		if i not in glst:
			box.add(i)
	print(box)
check_missing_numbers(400,1000,9999)




