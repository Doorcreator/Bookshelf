# V01：随机数分界法
# from ALG004_qsort import qsort04
import random
def divide_seq(lst):
    L=[]
    R=[]
    rc = random.choice(lst)
    for x in lst:
        if x < rc:
            L.append(x)
        else:
            R.append(x)
    return L,R
def qsort01(lst):
    f = []
    m =[]
    while True:
        r1 = divide_seq(lst)
        if len(r1[1]) == 1:
            if len(r1[0]) == 1:
                f.append(r1[0][0])
                f.append(r1[1][0])
                f.extend(m)
                m =[]
                break
            elif len(r1[0]) > 1:
                m.insert(0,r1[1][0])
                lst = r1[0]
        else:
            if len(r1[0]) == 0:
                if len(set(r1[1]))==1:
                    f.extend(r1[1])
                    f.extend(m)
                    m =[]
                    break
                else:
                    lst = r1[1]
            elif len(r1[0]) == 1:
                f.append(r1[0][0])
                lst = r1[1]
            elif len(r1[0]) > 1:
                if len(set(r1[0]))==1:
                    f.extend(r1[0])
                    lst = r1[1]
    return f
# V02：分而治之法
sorted_arr = []
def qsort02(array):
    L = []
    R = []
    if len(array) == 1:
        sorted_arr.append(array[0])
        return None
    if  len(set(array)) == 1:
        for x in range(len(array)):
            sorted_arr.append(array[0])
        return None
    if len(array) == 0:
        return None
    for i in range(1,len(array)):
        m = array[0]
        if array[i] <= m:
            L.append(array[i])
        else:
            R.append(array[i])
    L.append(m)
    qsort02(L)
    qsort02(R)
    return sorted_arr
# initial state: L:0, U:len(array), array:a list of integers.
# V03_01：从前向后扫描
def qsort03_01(L,U,array):
    if L>=U:
        return None
    m = L
    i = L+1
    j = U
    while j-1>m:
        if array[i]<array[m]:
            t = array[i]
            array[i] = array[m]
            array[m] = t
            m=i
            i+=1
        else:
            t = array[i]
            array[i] = array[j-1]
            array[j-1] = t
            j-=1
    qsort03_01(L,m,array)
    qsort03_01(m+1,U,array)
    return array
# V03_02：从后向前扫描
def qsort03_02(L,U,array):
    if L>=U:
        return None
    m = U-1
    i = L
    j = U-1
    while i<m:
        if array[j-1]>=array[m]:
            t = array[j-1]
            array[j-1] = array[m]
            array[m] = t
            m=j-1
            j-=1
        else:
            t = array[j-1]
            array[j-1] = array[i]
            array[i] = t
            i+=1
    qsort03_02(L,m,array)
    qsort03_02(m+1,U,array)
    return array
# V04：从两头向中间扫描
def qsort04(L,U,array):
    if L>=U:
        return None
    m = L
    i = L+1
    j = U
    while m<j-1:
        if array[i]<array[m]:
            t = array[i]
            array[i] = array[m]
            array[m] = t
            m=i
            i+=1
            if array[j-1]>=array[m]:
                j-=1
            else:
                t = array[j-1]
                array[j-1] = array[m+1]
                array[m+1] = t
                t = array[m]
                array[m] = array[m+1]
                array[m+1] = t
                m=m+1
                i+=1
        else:
            t = array[i]
            array[i] = array[j-1]
            array[j-1] = t
            j-=1
            if i>=j:
                break
            if array[i]<array[m]:
                t = array[i]
                array[i] = array[m]
                array[m] = t
                m=i
                i+=1
            else:
                t = array[i]
                array[i] = array[j-1]
                array[j-1] = t
                j-=1
    qsort04(L,m,array)
    qsort04(m+1,U,array)
    return array

# Efficiency (V04 - V03)> 3%
# a = [1,12,12,20,37,44,64,31,775,33,775,90,145,2,90,5,37,8,20,9,20,33,20]
# b = ['this','is','a','great','night',' ','right','?','good','noon','righter','god','rare']
# print(qsort04(0,len(b),b))
# import random
# r = random.sample(range(10000),10000)
# from line_profiler import LineProfiler
# lp = LineProfiler()
# lp.enable_by_count()
# lp_wrapper = lp(qsort04)
# qsort04(0,len(r),r)
# lp.print_stats()
# 10^3:0.11 s
# 10^4:1.41 s
