def bit_map_sort(target_seq,min_negative_int,max_positive_int):
	# target_seq: a list of integers (duplicates are not allowed in the list)
	# min_negative_int: an estimated minimum negative integer in the list
	# max_positive_int: an estimated maximum positive integer in the list
	# return a sorted result of target_seq
	seq = {}
	sorted_seq = []
	for i in range(min_negative_int,max_positive_int+1):
		seq[i] = 0
	for k in seq.keys():
		for j in target_seq:
			if k == j:
				seq[k] = 1
	for k in seq.items():
		if k[1]==1:
			sorted_seq.append(k[0])
	return sorted_seq
def bit_map_sort_univ(target_seq,min_negative_int,max_positive_int):
	# target_seq: a list of integers (duplicates are allowed in the list)
	seq = {}
	seq2 = {}
	sorted_seq = []
	occur = 0
	for i in range(min_negative_int,max_positive_int+1):
		seq[i] = 0
	for k in seq.keys():
		for j in target_seq:
			if k == j:
				seq2.setdefault(k,{1:0})
				seq2[k][1] += 1
	for k in seq2.items():
		if k[1][1]==1:
			sorted_seq.append(k[0])
		else:
			occur = k[1][1]/1
			for i in range(int(occur)):
				sorted_seq.append(k[0])
	return sorted_seq
