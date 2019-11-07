# Counting sort is based on the idea of sorting data (exactly, integers) according to their position mapped in a sequence of integers in naturally occurring order (i.e., every number is in its proper place, and the sequence as a whole is in ascending or descending order). Duplicates are mapped in identical positions. Finally, output the sequence successively. 
# V01:
def counting_sort01(array):
    min_element = min(array)
    max_element = max(array)
    bucket = {}
    sorted_arr = []
    for i in range(min_element,max_element+1):
        bucket[i] = 0
    for ele in array:
        bucket[ele] += 1
    for b in bucket:
        if bucket[b] > 0:
            for x in range(bucket[b]):
                sorted_arr.append(b)        # sort in ascending order
                # sorted_arr.insert(0,b)    # sort in descending order
    return sorted_arr
# V02:
def counting_sort02(array):
    min_element = min(array)
    max_element = max(array)
    bucket = {}
    sorted_arr = []
    for ele in array:
        bucket.setdefault(ele,0)
        bucket[ele] += 1
    for b in range(min_element,max_element+1):
        try:
            if bucket[b] > 0:
                for x in range(bucket[b]):
                    sorted_arr.append(b)
        except KeyError:
            continue
    return sorted_arr
# V03: optimized V02
def counting_sort03(array):
    min_element = min(array)
    max_element = max(array)
    bucket = {}
    for ele in array:
        bucket.setdefault(ele,0)
        bucket[ele] += 1
    p = 0
    for b in range(min_element,max_element+1):
        if bucket.get(b,0) > 0:
            for x in range(bucket[b]):
                array[p] = b
                p += 1
    return array
# V04:
def counting_sort04(array):
    min_element = min(array)
    max_element = max(array)
    bucket = [0]*(max_element-min_element+1)
    for ele in array:
        bucket[ele-min_element] += 1
    p = 0
    for b in range(len(bucket)):
        while bucket[b] >= 1:
            array[p] = b+min_element
            p += 1
            bucket[b] -= 1
    return array
# V05:
def counting_sort05(array):
    min_element = min(array)
    max_element = max(array)
    sorted_arr = [None]*len(array)
    bucket = [0]*(max_element-min_element+1)
    for ele in array:
        bucket[ele-min_element] += 1
    for i in range(1,len(bucket)):
        bucket[i] += bucket[i-1]
    for a in array:
        sorted_arr[bucket[a-min_element]-1] = a
        bucket[a-min_element] -= 1
    return sorted_arr
# Performance: numbers are time (in seconds) consumed on homogeneous data (or heterogeneous data for those in brackets).
#       V01            V02             V03              V04
# 10^2: 0.00091(3.27)  0.00091(4.49)   0.00089(1.89)    0.00081(1.76)
# 10^3: 0.0089(3.37)   0.0091(4.55)    0.0087(1.93)     0.0075(1.80)
# 10^4: 0.088(3.47)    0.091(4.62)     0.086(2.0)       0.076(1.87)
# 10^5: 0.90(4.0)      0.92(5.11)      0.90(2.6)        0.77(2.54)
# r = [-8,5,200,6,2,10,4,-8,2,9,5,-8,1000,28900]
# r = [-8,5,20,6,2,10,4,-8,2,9,5,-8,10,28]
# import random
# r = random.sample(range(1000),100)
# from line_profiler import LineProfiler
# lp = LineProfiler()
# lp.enable_by_count()
# lp_wrapper = lp(counting_sort03)
# print(counting_sort05(r))
# lp.print_stats()

