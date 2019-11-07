import random
def rand_even(m,n1,n2):
	t=0
	s1=[]
	s3={}
	if m>(n2-n1)/2:
		print('Warning: The first argument [%d] should be smaller than [%d]!'%(m,(n2-n1)/2))
	else:
		for i in range(n1,n2+1):
			s3[i]=i
		s2 = [v for v in s3.values()]
		while t<m:
			r = random.choice(s2)
			if r%2==0:
				s1.append(r)
				s2.remove(r)
				t+=1
	return s1
def rand_odds(m,n1,n2):
	t=0
	s1=[]
	s3={}
	if m>(n2-n1)/2:
		print('Warning: The first argument [%d] should be smaller than [%d]!'%(m,(n2-n1)/2))
	else:
		for i in range(n1,n2+1):
			s3[i]=i
		s2 = [v for v in s3.values()]
		while t<m:
			r = random.choice(s2)
			if r%2!=0:
				s1.append(r)
				s2.remove(r)
				t+=1
	return s1
def gene_can(even,odds,L,U):
	dic = {}
	e_lst = rand_even(even,L,U)
	o_lst = rand_odds(odds,L,U)
	e_lst.extend(o_lst)
	random.shuffle(e_lst)
	for e in e_lst:
		if e%2==0:
			dic[e]='w'
		else:
			dic[e]='b'
	return dic
def pick_bean(can): # can format: dict[1:'w',2:'b',...,n:'w']
	bean = random.sample(set(can),2)
	if can[bean[0]]==can[bean[1]]:
		del can[bean[0]]
		del can[bean[1]]
		rb = random.randint(1,10000)
		can.update({rb:'b'})
	elif can[bean[0]]=='w' and can[bean[1]]=='b':
		del can[bean[1]]
	elif can[bean[0]]=='b' and can[bean[1]]=='w':
		del can[bean[0]]
	print(can)
	if len(can) != 1:
		return pick_bean(can)

# gene_can(i,j,k,m) w: even -> left b; w: odds-> left w
# pick_bean(gene_can(4,3,10,100))


