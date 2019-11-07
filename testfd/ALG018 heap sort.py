#V01---------------------------------------------------------------
def sift_up01(array):
# move out-of-order elements from bottom to top of a tree (array in this case), and get possibly not a heap.
    n=len(array)
    for j in range(n,1,-1):
        p = j//2
        try:
            if array[j-1]<array[p-1]:
                t = array[j-1]
                array[j-1] = array[p-1]
                array[p-1] = t
        except IndexError:
            continue
    return array
def sift_up02(array):
# move out-of-order elements from bottom to top of a tree (array in this case), and get surely a heap.
    n=len(array)
    change_count = 0
    for j in range(n,1,-1):
        p = j//2
        try:
            if array[j-1]<array[p-1]:
                t = array[j-1]
                array[j-1] = array[p-1]
                array[p-1] = t
                change_count+=1
        except IndexError:
            continue
    if change_count==0:
        return array
    else:
        return sift_up02(array)
def sift_down01(array):
# move out-of-order elements from top to bottom of a tree (array in this case), and get possibly not a heap.
    n=len(array)
    for j in range(1,n//2+1):
        c = 2*j
        try:
            if array[c-1]<array[j-1]:
                t = array[c-1]
                array[c-1] = array[j-1]
                array[j-1] = t
            if array[c]<array[j-1]:
                t = array[c]
                array[c] = array[j-1]
                array[j-1] = t
        except IndexError:
            continue
    return array
def sift_down02(array):
# move out-of-order elements from top to bottom of a tree (array in this case),and get surely a heap.
    n=len(array)
    change_count = 0
    for j in range(1,n//2+1):
        c = 2*j
        try:
            if array[c-1]<array[j-1]:
                t = array[c-1]
                array[c-1] = array[j-1]
                array[j-1] = t
                change_count+=1
            if array[c]<array[j-1]:
                t = array[c]
                array[c] = array[j-1]
                array[j-1] = t
                change_count+=1
        except IndexError:
            continue
    if change_count==0:
        return array
    else:
        return sift_down02(array)
def extract_min01(heap):
# extract the minimum value [top 1 element in this case] in a heap and restore the heap.
    h_min = heap.pop(0)
    new_heap = sift_down01(heap)
    return h_min,new_heap
def heap_sort01(array):
    heap = sift_down01(sift_up01(array))
    sorted_heap = []
    for i in range(len(heap)):
        current_min = extract_min01(heap)[0]
        sorted_heap.append(current_min)
    return sorted_heap
# V02----------------------------------------------------------
def sift_up03(heap,new_elmt):
# move an out-of-order element [new_elmt] from bottom to top of a heap
    heap.append(new_elmt)
    n = len(heap)
    parent_pos = n//2 - 1
    while parent_pos >= 0:
        current_pos = 2*parent_pos + 1 if n%2==0 else 2*parent_pos + 2
        if heap[current_pos] < heap[parent_pos]:
            t = heap[current_pos]
            heap[current_pos] = heap[parent_pos]
            heap[parent_pos] = t
            n = parent_pos + 1
            parent_pos = n//2 - 1
        else:
            break
    return heap
def sift_down03(heap,new_elmt):
# move an out-of-order element [new_elmt] from top to bottom of a heap
    heap.append(new_elmt)
    t = heap[-1]
    heap[-1] = heap[0]
    heap[0] = t
    last_elmt = heap.pop()
    n = len(heap)
    parent_pos = 0
    while parent_pos <= n//2 - 1:
        left_child_pos = 2*parent_pos + 1
        right_child_pos = 2*parent_pos + 2
        try:
            current_pos = left_child_pos if heap[left_child_pos]<heap[right_child_pos] else right_child_pos
        except IndexError:
            current_pos = left_child_pos
        if heap[current_pos] < heap[parent_pos]:
            t = heap[current_pos]
            heap[current_pos] = heap[parent_pos]
            heap[parent_pos] = t
            parent_pos = current_pos
        else:
            break
    sift_up03(heap,last_elmt)
    return heap
def extract_min02(heap):
# extract the minimum value [top 1 element in this case] in a heap and restore the heap.
    heap_min = heap[0]
    t = heap[-1]
    heap[-1] = heap[0]
    heap[0] = t
    heap.pop(-1)
    n = len(heap)
    parent_pos = 0
    while parent_pos <= n//2 - 1:
        left_child_pos = 2*parent_pos + 1
        right_child_pos = 2*parent_pos + 2
        try:
            current_pos = left_child_pos if heap[left_child_pos]<heap[right_child_pos] else right_child_pos
        except IndexError:
            current_pos = left_child_pos
        if heap[current_pos] < heap[parent_pos]:
            t = heap[current_pos]
            heap[current_pos] = heap[parent_pos]
            heap[parent_pos] = t
            parent_pos = current_pos
        else:
            break
    return heap_min,heap
def heapify(array):
# convert an array [typically, a list] into a heap
    heap = []
    for elmt in array:
        sift_up03(heap,elmt)
    return heap
def heap_sort02(array):
# sort an out-of-order array using heap method
    sorted_arr = []
    heap = heapify(array)
    while len(heap)>0:
        r = extract_min02(heap)
        heap_min = r[0]
        heap = r[1]
        sorted_arr.append(heap_min)
    return sorted_arr

# efficiency: V02>V01
# sort performance comparison between heap_sort02 and qsort04
#       heap_sort02   qsort04
# 10^2: 0.0039      0.0050
# 10^3: 0.056       0.071
# 10^4: 0.73        1.0
# 10^5: 9.3         13.0
# 10^6: 113         166
# import random
# r = random.sample(range(10000),1000)
# print(heap_sort01(r))
# print(heap_sort02(r))
