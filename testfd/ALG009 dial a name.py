key_index = {2:'abc',3:'def',4:'ghi',
			 5:'jkl',6:'mno',7:'pqr',
			 8:'stu',9:'vwx',0:'yz '}
def dial(name_array,dial_num,dial_order):
	temp = set()
	key_list = [e for e in key_index[dial_num]]
	for name in name_array:
		for key in key_list:
			try:
				if name[dial_order].lower() == key:
					temp.add(name)
			except:
				break
	return temp
def dial_all(name_array,dial_nums):
	i=0
	num = str(dial_nums)
	while True:
		r = dial(name_array,int(num[i]),i)
		name_array = r
		i+=1
		if i >= len(num):
			break
	return name_array
def readfl2dic():
	uniqwdset = set()
	with open (r'C:\Users\Neo\Desktop\Pythonx\world_names.txt','r') as f:
		while True:
			try:
				line = f.readline()
				uniqwdset.add(line.strip().lower())
			except Exception as e:
				print(e)
			if not line:
				break
	return uniqwdset
print(dial_all(readfl2dic(),5225089355))
# 385155



