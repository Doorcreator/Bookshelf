# V01
def search(t,array,recur):
    # t: an element (integer,float, or string) to search
    # array: a sorted list to search from
    # recur: return the number of recurrences
    recur+=1
    L = 0
    U = len(array)
    mid = len(array)//2
    if t < array[L] or t > array[U-1]:
        return -1,recur
    else:
        if t == array[mid]:
            return t,recur
        elif t < array[mid]:
            U = mid
            return search(t,array[L:U],recur)
        elif t > array[mid]:
            L = mid
            return search(t,array[L:U],recur)
def bi_search01(t,array):
    # t: element to search
    # array: a sorted list to search from
    # return -1 (target element not found) or a tuple((position of target element, target element),recurrences), return the first position for multiple occurrences of one element.
    dic = {}
    for e in enumerate(array):
        dic.setdefault(e[0])
        dic[e[0]]=e[1]
    r = search(t,[x[1] for x in dic.items()],0)
    if r[0] == t:
        for x in filter(lambda x:x[1]==t,dic.items()):
            return x,r[1]
            break
    else:
        return -1
# V02
def bi_search02(t,array):
    re_arr = {}
    for i in enumerate(array):
        re_arr[i[0]] = i[1]
    L = 0
    U = len(re_arr)-1
    if t < re_arr[L] or t > re_arr[U]:
            return -1
    else:
        while U-L != 1:
            mid = (L+U)//2
            if t < re_arr[mid]:
                U = mid
            elif t > re_arr[mid]:
                L = mid
            else:
                while mid >1 and t == re_arr[mid-1]:
                    mid -= 1
                return mid
        if t == re_arr[L]:
            mid = L
        elif t == re_arr[U]:
            mid = U
        else:
            return -1
        return mid
# V03
# code tuning only applicable to an array with 2^n elements.
def bi_search03(t,array):
    re_arr = {}
    for i in enumerate(array):
        re_arr[i[0]] = i[1]
    L = 0
    U = len(re_arr)
    step = U/2
    if t < re_arr[L] or t > re_arr[U-1]:
            return -1
    else:
        pos = step
        while step >= 1:
            if t < re_arr[pos]:
                step = step/2
                pos -= step
            elif t > re_arr[pos]:
                step = step/2
                pos += step
            elif t == re_arr[pos]:
                return pos,re_arr[pos]
        if step < 1:
            if t == re_arr[0]:
                pos = 0
                return pos,re_arr[pos]
        else:
            return -1

import random
# from line_profiler import LineProfiler
# lp = LineProfiler()
# lp.enable_by_count()
# lp_wrapper = lp(bi_search02)
# lp.print_stats()
# a = [-11,-8,-6,-5,3,8,9,13,13,13,15,17]
# b = [',','.','as','ask','can','country','do','for','not','you','you','your']
# r = random.sample(range(200),180)
# r.sort()
# print(bi_search02(13,a))
# print(bi_search02('.',b))
# from ALG008_bisearch_v2.0 import bi_search02





