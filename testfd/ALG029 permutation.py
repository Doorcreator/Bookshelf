# V01
def permutate01(n1,n2):
    # To find any permutations formed by numbers between n1 and n2 (the interval should not span a number ending with zero) by increasing digits from a minimum to a maximum (both are chosen from the possible permutations).
    results = set()
    m1_str = [repr(i) for i in range(n1,n2+1)]
    m2_str = m1_str.copy()
    norm_m1 = int(''.join(sorted(''.join(m1_str))))
    m1_int = int(''.join(m1_str))
    m2_str.reverse()
    m2_int = int(''.join(m2_str))
    for j in range(m1_int,m2_int+1):
        num = int(''.join(sorted(repr(j))))
        if num == norm_m1 and test_digit(j,m1_str) == True:
            results.add(j)
    return results,len(results)
def test_digit(n,array):
    n_str = repr(n)
    i = 1
    while i <= len(n_str):
        lower_bndry = n_str[:i]
        if lower_bndry in array:
            try:
                n = int(n_str[i:])
            except ValueError:
                if n_str in array:
                    return True
                else:
                    return False
            return test_digit(n,array)
        i += 1
    return False
# V02: recursive implementation
results = set()
def permutate02(bin,start,end):
    if start==end:
        results.add(''.join(bin))
    else:
        for m in range(start,end):
            bin[start],bin[m] = bin[m],bin[start]
            permutate02(bin,start+1,end)
            bin[start],bin[m] = bin[m],bin[start]
    return results,len(results)
# V03: recursive implementation
results = set()
flag = {}
box = {}
def permutate03(cards_in_hand,cur_pos):
    # cur_pos must start from 1 when the function is initially called.
    if cur_pos == len(cards_in_hand)+1:
        for i in range(1,len(box)+1):
            results.add(''.join([v for v in box.values()]))
    else:
        for i in range(0,len(cards_in_hand)):
            if flag.setdefault(i,0) == 0:
                box[cur_pos] = cards_in_hand[i]
                flag[i] = 1
                print(box)
                permutate03(cards_in_hand,cur_pos+1)
                flag[i] = 0
    return results,len(results)
arr = ['1','2','3']
import time
t0 = time.time()
# print(test_digit(9711216100,['161','97','112','100']))
# print(permutate01(11,14))
# t1 = time.time()
# print(permutate02(arr,0,len(arr)))
# t2 = time.time()
print(permutate03(arr,1))
# t3 = time.time()
# print(t1-t0,t2-t1)


