# Merge sort is implemented in the light of "divide and conquer" idea: first, divide a sequence into single elements, sort them in pairs (usually, in half), and then merge the sorted pieces into bigger pieces until the whole original sequence is sorted in place.
# V01: recursive version
def merge_sort01(L,U,array):
    if len(array)==1:
        return array
    L = 0
    U = len(array)
    mid = (L+U)//2
    left_arr = array[L:mid]
    right_arr = array[mid:U]
    left_ele = merge_sort01(L,mid,left_arr)
    right_ele = merge_sort01(mid,U,right_arr)
    return merge_array(left_ele,right_ele)
def merge_array(array01,array02):
    merged_arr = []
    i = 0
    j = 0
    while i<len(array01) and j<len(array02):
        if array01[i]<array02[j]:
            merged_arr.append(array01[i])
            i += 1
        else:
            merged_arr.append(array02[j])
            j += 1
    last_index,last_arr = (j,array02) if i==len(array01) else (i,array01)
    merged_arr.extend(last_arr[last_index:])
    return merged_arr
# V02: iterative version
def merge_sort02(array):
    merged_arr = {}
    p = 0
    k = 0
    while k <= len(array)/2:
        merged_arr[k] = merge_array(array[p:p+1],array[p+1:p+2])
        p += 2
        k += 1
    temp_len = len(merged_arr)
    while temp_len > 1:
        y = 0
        for x in range(0,temp_len,2):
            if x+1 < temp_len:
                merged_arr[y] = merge_array(merged_arr[x],merged_arr[x+1])
            else:
                merged_arr[y] = merged_arr[x]
            y += 1
        temp_len = y
    return merged_arr[0]
      # qsort  vs  merge_sort01  merge_sort02
# 10^3: 0.11       0.04          0.030
# 10^4: 1.41       0.55          0.40
# 10^5:            5.2           4.8
# a =[5,8,3,1,12,14,7,-12,22,16,11,0,6,4,45,58,32,9,10,11,80,81,92,800,765,44,2,145,90,46,63,21] # 16
# b =[5,8,3,1,12,9,14,7,-12,22,16,7,11,10,4] # 15
# c =[5,8,3,1,12,9,14,7,-12,22,16,11,7,0] # 14
# d =[5,8,3,1,12,9,14,7,-12,22,16,7,11]
# e = [12,8,34,1,5,-2,15,19,14]
# f = [30,84,2]
# print(merge_sort02(b))
# print(merge_sort01(0,len(b),b))
# import random
# r = random.sample(range(100000),100000)
# from line_profiler import LineProfiler
# lp = LineProfiler()
# lp.enable_by_count()
# lp_wrapper = lp(merge_sort01)
# merge_sort02(r)
# merge_sort01(0,len(r),r)
# lp.print_stats()