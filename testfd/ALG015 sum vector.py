# Vectors are represented by a sequence of real numbers (including positive and negative numbers).
# V1 O(n^2), massive recursion shall lead to program collapse.
maxsf = {0:0}
def sum_vector01(array):
    sum = 0
    imax = array[0]
    if len(array)>1:
        for i in array:
            sum += i
            if sum>imax:
                imax = sum
        if imax>maxsf[0]:
            maxsf[0] = imax
        array.pop(0)
        return sum_vector01(array)
    elif len(array)==1:
        if array[0]>maxsf[0]:
            maxsf[0] = array[0]
    return maxsf[0]
# V2 O(n^2)
def sum_vector02(array):
    max_arr = []
    for i in range(len(array)):
        sum = 0
        imax = array[i]
        for j in range(i,len(array)):
            sum +=array[j]
            if sum>imax:
                imax=sum
        max_arr.append(imax)
    global_max = max_arr[0]
    for i in range(1,len(max_arr)):
        if max_arr[i]>global_max:
            global_max = max_arr[i]
    return global_max
# V3 O(n^2)
def sum_vector03(array):
    imax = array[0]
    for i in range(len(array)):
        sum = 0
        for j in range(i,len(array)):
            sum +=array[j]
            if sum>imax:
                imax=sum
    return imax
# V4 O(n^2)
def sum_vector04(array):
    imax = array[0]
    sum = {}
    sum[-1] = 0
    for i in range(len(array)):
        sum[i] = sum[i-1] + array[i]
        if sum[i]>imax:
            imax=sum[i]
    for i in range(1,len(array)):
        for j in range(i,len(array)):
            sum[j] = sum[j] - array[i-1]
            if sum[j]>imax:
                imax=sum[j]
    return imax
# V5 O(n*log n), divide and conquer
def sum_vector05(L,U,array):
    # One possible initialized L=0 and U=len(array).
    if L>=U:
        return -1
    elif L<U:
        m = (L+U)//2
        lmax=array[m]
        sum=0
        for i in range(m,L-1,-1):
            sum += array[i]
            if sum>lmax:
                lmax=sum
        rmax=array[m+1]
        sum=0
        for i in range(m+1,U+1):
            sum += array[i]
            if sum>rmax:
                rmax=sum
        mmax = lmax+rmax
    rlmax = sum_vector05(L,m,array)
    rrmax = sum_vector05(m+1,U,array)
    return max(mmax,lmax,rmax)
# V6 O(n), scanning 
def sum_vector06(array):
    imax = array[0]
    sum = 0
    for i in range(len(array)):
        sum +=array[i]
        sum = max(0,sum)
        imax = max(imax,sum)
    return imax
