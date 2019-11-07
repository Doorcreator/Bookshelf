# V1
def rotate_str(n,i,j):
	i+=1
	if i>=j:
		n = n[1:]+n[0]
		return n
	else:
		n = n[1:]+n[0]
		return rotate_str(n,i,j)
# V2
def reverstr(s):
# reverse a list and concatenate all the elements in the list to one string
	rs = list(s)
	return ''.join([rs.pop() for e in range(len(rs))])
def part_rev(s,n):
	former_n = reverstr(s[:n])
	latter_n = reverstr(s[n:])
	return reverstr(former_n+latter_n)