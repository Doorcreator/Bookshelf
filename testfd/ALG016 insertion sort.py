# Efficiency: V02>V01>V03
# V01
def insert_sort01(array):
    sort_arr = []
    sort_arr.append(array[0])
    for i in range(1,len(array)):
        if array[i]>sort_arr[len(sort_arr)-1]:
            sort_arr.append(array[i])
            continue
        for k in range(len(sort_arr)):
            if array[i]<sort_arr[k]:
                sort_arr.insert(k,array[i])
                break
            elif array[i]<sort_arr[k+1]:
                sort_arr.insert(k+1,array[i])
                break
    return sort_arr
# V02
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
def insert_sort02(array):
    sort_arr = []
    sort_arr.append(array[0])
    for i in range(1,len(array)):
        if array[i]>sort_arr[len(sort_arr)-1]:
            sort_arr.append(array[i])
            continue
        for k in range(len(sort_arr)):
            if array[i]<sort_arr[k]:
                sort_arr.insert(k,array[i])
                break
            else:
                pos = bi_search(array[i],sort_arr[:-1])
                sort_arr.insert(pos,array[i])
                break
    return sort_arr
# V03
def insert_sort03(array):
    for i in range(1,len(array)):
        for j in range(i):
            if array[i]<array[j]:
                array[i],array[j] = array[j],array[i]
    return array

# a =[5,8,-3,1,2,9,4,7,-12,66,8,90,-42,8,22,409,11,11,-12]
# import random
# print(insert_sort02(random.sample(range(10000),1000)))
