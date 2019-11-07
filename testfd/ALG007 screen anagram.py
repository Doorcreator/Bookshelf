from functools import reduce
def readfl2dic():
	dic = {}
	uniqwdset = set()
	i=0
	with open (r'C:\Users\Neo\Desktop\Pythonx\oxfordwdlst.txt','r') as f:
		while True:
			line = f.readline()
			uniqwdset.add(line.strip().lower())
			if not line:
				break
		for w in uniqwdset:
			dic[i] = w
			i+=1
	return dic
def str2numseq(ori_str):
	convted_str = [x for x in map(ord,ori_str)]
	convted_str.sort()
	return reduce(lambda m,n:str(m)+str(n),convted_str,'')
def aggre_words(wdic):
	str_int_pair={}
	count_key = {}
	for k in wdic.values():
		v = str2numseq(k)
		str_int_pair[k] = v
		count_key.setdefault(v,0)
		count_key[v]+=1
	with open (r'C:\Users\Neo\Desktop\Pythonx\oxford_anagram.txt','w+') as w:
		for k,v in count_key.items():
			if v>1:
				wds=set()
				fr = filter(lambda x:k==x[1],str_int_pair.items())
				wds = [k for k,v in fr]
				w.write(','.join(wds))
				w.write('\n')




