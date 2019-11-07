# bubble_sort, O(n^2)
# V01 & V02: Stack overflow for an array of more than 7000 elements.
# V03: Stack overflow for an array of more than 14000 elements.
import sys
sys.setrecursionlimit(1000000)
# V01: forward bubble sort
def bubble_sort01(L,U,array):
    # L: lower boundary of array indexes, typically 0.
    # U: (upper boundary of array indexes)+1, typically len(array).
    # array: a list of integers.
    m = L
    if L == U:
        return array
    for i in range(L+1,U):
        if array[i]<array[m]:
            t = array[i]
            array[i] = array[m]
            array[m] = t
            m = i
        else:
            m = i
    return bubble_sort01(L,U-1,array)
# V02: backward bubble sort
def bubble_sort02(L,U,array):
    m = U-1
    if U == L:
        return array
    for i in range(U-2,L-1,-1):
        if array[i]>array[m]:
            t = array[i]
            array[i] = array[m]
            array[m] = t
            m = i
        else:
            m = i
    return bubble_sort02(L+1,U,array)
# V03: bidirectional bubble sort
def bubble_sort03(L,U,array):
    if L==U//2:
        return array
    m = L
    m2 = U-1
    for i in range(L+1,len(array)):
        if array[i]<array[m]:
            t = array[i]
            array[i]=array[m]
            array[m]=t
            m=i
        else:
            m=i
        j = len(array)-i-1
        if array[j]>array[m2]:
            t = array[j]
            array[j]=array[m2]
            array[m2]=t
            m2=j
        else:
            m2=j
    return bubble_sort03(L+1,U,array)

# import random
# a = [18,2,9,4,16,24,10,42,22,12,7,-1,19,33]
# b = random.sample(range(10000),500)
# print(bubble_sort03(0,500,b))
