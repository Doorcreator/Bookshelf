# bucket sort
# V01: create empty buckets, put the array elements into appropriate buckets, sort the elements in each bucket using insertion sort method, and then concatenate the sorted buckets.
def bktsort(array):
    max = array[0]
    min = array[0]
    bin = {}
    global total_bucket
    # find the maximum and minimum value in the array
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
        if array[i] > max:
            max = array[i]
    if max == min:
        bin[0] = array
        total_bucket = 1
        return bin
    # allocate an appropriate number of buckets and a within-bucket interval
    
    if len(array) < 100:
        total_bucket = len(array)//2 + 1
    else:
        total_bucket = len(array)//10+1
    interval = (max-min)/total_bucket
    # put each element in the array into appropriate buckets
    for i in range(len(array)):
        k = (array[i]-min)//interval
        bin.setdefault(k,[])
        bin[k].append(array[i])
    return bin
def insertion_sort(array):
    for i in range(1,len(array)):
        for j in range(i):
            if array[i]<array[j]:
                array[i],array[j]=array[j],array[i]
    return array
def bucket_sort01(array):
    bin = bktsort(array)
    sorted_arr = []
    # sort the elements in each bucket containing more than one element
    for b in bin.items():
        if len(b[1]) > 1:
            bin[b[0]] = insertion_sort(b[1])
    # outputting the elements in the buckets by order shall yield a sorted array
    for i in range(total_bucket+1):
        try:
            sorted_arr.extend(bin[i])
        except:
            pass
    return sorted_arr
# V02: replace the insertion sort in V01 with binary search based insertion sort for within-bucket sorting, but it is not as efficient as V01.
def bi_search(t,array):
    re_arr = {}
    for i in enumerate(array):
        re_arr[i[0]] = i[1]
    L = 0
    U = len(re_arr)-1
    while U-L != 1:
        mid = (L+U)//2
        if t < re_arr[mid]:
            U = mid
        elif t > re_arr[mid]:
            L = mid
        else:
            return mid
    if t > re_arr[L]:
        return U
    else:
        return L
def bucket_sort02(array):
    max = array[0]
    min = array[0]
    bin = {}
    sorted_arr = []
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
        if array[i] > max:
            max = array[i]
    if max == min:
        return array
    if len(array) < 100:
        total_bucket = len(array)//2 + 1
    else:
        total_bucket = len(array)//10+1
    interval = (max-min)/total_bucket
    for i in range(len(array)):
        k = (array[i]-min)//interval
        bin.setdefault(k,[])
        if len(bin[k]) == 0 or array[i] >= bin[k][-1]:
            bin[k].append(array[i])
        elif array[i] <= bin[k][0]:
            bin[k].insert(0,array[i])
        else:
            pos = bi_search(array[i],bin[k])
            bin[k].insert(pos,array[i])
    for b in range(total_bucket+1):
        try:
            sorted_arr.extend(bin[b])
        except:
            pass
    return sorted_arr

array = [63, 157, 189, 51, 101, 47, 141, 28, 121, 0.34, 157, -156, 194, 117, 98, 0.34, 139, 67, 133, 181, 13, 28, 109, 28]
print(bucket_sort01(array))
print(bucket_sort02(array))
         # V01      V02
# 10     0.00015    0.00018
# 10^2   0.0012     0.002
# 10^3   0.012      0.022
# 10^4   0.12       0.22
# 10^5   1.24       2.23