def selection_sort(array,flag):
    # To sort an array in ascending order when flag = 1 or in descending order when flag = -1.
    # Compare current element with the succeeding element, and exchange their positions if the condition is met (i.e., the succeeder < the current (as in the case of flag = 1) or the succeeder > the current (as in the case of flag = -1)).
    if flag == 1:
        for i in range(len(array)-1):
            for j in range(i+1,len(array)):
                if array[i]>array[j]:
                    array[i],array[j] = array[j],array[i]
    elif flag == -1:
        for i in range(len(array)-1):
            for j in range(i+1,len(array)):
                if array[i]<array[j]:
                    array[i],array[j] = array[j],array[i]
    return array

# a =[5,8,-3,1,2,9,4,7,-12,66,8,22,90,-42,22,409,11,11,-12]
# print(selection_sort(a,-1))