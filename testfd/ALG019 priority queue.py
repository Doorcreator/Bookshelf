# from ALG019_priority_queue import PriorityQueue
# PriorityQueue implementation based on heap containing integers as its elements.
class PriorityQueue():
    def __init__(self):
        pass
    def sift_up_min(self,heap,new_elmt):
    # Move an out-of-order element [new_elmt] from bottom to top of a heap. Min on the top of the heap.
    # Equivalent to push function.
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
    def sift_down_min(self,heap,new_elmt):
    # Move an out-of-order element [new_elmt] from top to bottom of a heap. Min on the top of the heap.
    # Equivalent to push function.
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
        self.sift_up_min(heap,last_elmt)
        return heap
    def extract_min(self,heap):
    # Extract the minimum value in a heap and restore the heap. Min on the top of the heap.
    # Equivalent to pop function.
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
    def heapify_min(self,array):
    # Convert an array [typically, a list] into a heap. Min on the top of the heap.
        heap = []
        for elmt in array:
            self.sift_up_min(heap,elmt)
        return heap
    def heap_sort_ascend(self,array):
    # Sort an out-of-order array using heap method. Return a sorted array with min in the first place.
    # Equivalent to sort function.
        sorted_arr = []
        heap = self.heapify_min(array)
        while len(heap)>0:
            r = self.extract_min(heap)
            heap_min = r[0]
            heap = r[1]
            sorted_arr.append(heap_min)
        return sorted_arr
    def sift_up_max(self,heap,new_elmt):
    # Move an out-of-order element [new_elmt] from bottom to top of a heap. Max on the top of the heap.
    # Equivalent to push function.
        heap.append(new_elmt)
        n = len(heap)
        parent_pos = n//2 - 1
        while parent_pos >= 0:
            current_pos = 2*parent_pos + 1 if n%2==0 else 2*parent_pos + 2
            if heap[current_pos] > heap[parent_pos]:
                t = heap[current_pos]
                heap[current_pos] = heap[parent_pos]
                heap[parent_pos] = t
                n = parent_pos + 1
                parent_pos = n//2 - 1
            else:
                break
        return heap
    def sift_down_max(self,heap,new_elmt):
    # Move an out-of-order element [new_elmt] from top to bottom of a heap. Max on the top of the heap.
    # Equivalent to push function.
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
                current_pos = left_child_pos if heap[left_child_pos]>heap[right_child_pos] else right_child_pos
            except IndexError:
                current_pos = left_child_pos
            if heap[current_pos] > heap[parent_pos]:
                t = heap[current_pos]
                heap[current_pos] = heap[parent_pos]
                heap[parent_pos] = t
                parent_pos = current_pos
            else:
                break
        self.sift_up_max(heap,last_elmt)
        return heap
    def extract_max(self,heap):
    # Extract the maximum value in a heap and restore the heap. Max on the top of the heap.
    # Equivalent to pop function
        heap_max = heap[0]
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
                current_pos = left_child_pos if heap[left_child_pos]>heap[right_child_pos] else right_child_pos
            except IndexError:
                current_pos = left_child_pos
            if heap[current_pos] > heap[parent_pos]:
                t = heap[current_pos]
                heap[current_pos] = heap[parent_pos]
                heap[parent_pos] = t
                parent_pos = current_pos
            else:
                break
        return heap_max,heap
    def heapify_max(self,array):
    # Convert an array [typically, a list] into a heap. Max on the top of the heap.
        heap = []
        for elmt in array:
            self.sift_up_max(heap,elmt)
        return heap
    def heap_sort_descend(self,array):
    # Sort an out-of-order array using heap method. Return a sorted array with max in the first place.
    # Equivalent to reverse sort function.
        sorted_arr = []
        heap = self.heapify_max(array)
        while len(heap)>0:
            r = self.extract_max(heap)
            heap_max = r[0]
            heap = r[1]
            sorted_arr.append(heap_max)
        return sorted_arr
# Merge sorted arrays
import random
def gen_sorted_seq(num_of_seqs, seq_size):
# Generate a list containing n [num_of_seqs] sublists, each of which has m [seq_size] sorted elements.
    dic = {}
    start = 0
    stop = 2*seq_size
    seq = []
    for i in range(num_of_seqs):
        dic[i] = random.sample(range(start,stop),seq_size)
        dic[i].sort()
        start += seq_size
        stop += 2*seq_size
        seq.append(dic[i])
    return seq
sorted_arr = []
h = PriorityQueue()
# V01: function reaches its bottleneck quickly due to a maximum recursive depth limit of about 1000.
def multi_seqc_sort01(array):
    try:
        heap = []
        for sub_arr in array:
            if len(sub_arr) ==0:
                array.remove(sub_arr)
            h.sift_up_min(heap,sub_arr[0])
        heap_min = heap[0]
        sorted_arr.append(heap_min)
        for sub_arr in array:
            if sub_arr[0] == heap_min:
                sub_arr.pop(0)
                break
    except IndexError:
        if len(array)==0:
            return sorted_arr
        else:
            pass
    return multi_seqc_sort01(array)
# V02: function performs better than a full_heap_sort when array size is very large (e.g., 10^5), but has not reached its best performance since it rebuilds a heap from scratch in each loop instead of reusing the heap already generated.
def multi_seqc_sort02(array):
    while True:
        try:
            heap = []
            for sub_arr in array:
                if len(sub_arr) ==0:
                    array.remove(sub_arr)
                h.sift_up_min(heap,sub_arr[0])
            heap_min = heap[0]
            sorted_arr.append(heap_min)
            for sub_arr in array:
                if sub_arr[0] == heap_min:
                    sub_arr.pop(0)
                    break
        except IndexError:
            if len(array)==0:
                return sorted_arr
# V03: Thanks to the priority queue (push the next element in a subarray into a priority queue successively, and pop the minimum from the current queue), function performs perfectly when heap height is small (i.e., a limited number (e.g., 50) of subarrays each with a large number of elements), but its performance decreases substantially and even behaves more poorly than a full_heap_sort when heap height increases.
def multi_seqc_sort03(array):
    heap = []
    for sub_arr in array:
        h.sift_up_min(heap,sub_arr[0])
    heap_min = h.extract_min(heap)[0]
    sorted_arr.append(heap_min)
    while True:
        try:
            for sub_arr in array:
                if sub_arr[0] == heap_min:
                    sub_arr.pop(0)
                    if len(sub_arr) == 0:
                        array.remove(sub_arr)
                    heap = h.sift_up_min(heap,sub_arr[0])
                    heap_min = h.extract_min(heap)[0]
                    sorted_arr.append(heap_min)
        except IndexError as e:
            if len(array)==0:
                return sorted_arr
            else:
                heap_min = h.extract_min(heap)[0]
                sorted_arr.append(heap_min)
# V04: push all the elements into a single huge heap utterly, and then heap_sort the heap. It behaves fairly at the cost of consuming too much memory.
def full_heap_sort(array):
    pooled_arr = []
    for sub_arr in array:
        pooled_arr.extend(sub_arr)
    hp = h.heapify_min(pooled_arr)
    heap = h.heap_sort_ascend(hp)
    return heap

# g_arr = gen_sorted_seq(50,1000)
# print(multi_seqc_sort03(g_arr))

# Performance comparison
#       multi_seqc_sort01   multi_seqc_sort02    multi_seqc_sort03            full_heap_sort
# 10^2: 0.0023              0.0083               0.0056                       0.0038
# 10^3: 0.13                0.083                0.064                        0.054
# 10^4: ME                  0.83                 0.65                         0.73
# 10^5:                     8.2                  6.7                          9.2
# 10^6:                     95                   71                           108

# arr = [1,5,12,9,3,6,7]
# heap = []
# pq = PriorityQueue()
# print('*********min**********')
# print('*********sift_up_min**********')
# for a in arr:
    # h1 = pq.sift_up_min(heap,a)
# for n in h1:
    # print(n)
# heap = []
# print('*********sift_down_min**********')
# for a in arr:
    # h2 = pq.sift_down_min(heap,a)
# for n in h2:
    # print(n)
# print('*********heapify_min**********')
# hpf = pq.heapify_min(arr)
# for n in hpf:
    # print(n)
# print('*********heap_sort_ascend**********')
# hs = pq.heap_sort_ascend(arr)
# for n in hs:
    # print(n)
# print('*********extract_min**********')
# hm = pq.extract_min(heap)
# print(hm[0])
# heap = []
# print('*********max**********')
# print('*********sift_up_max**********')
# for a in arr:
    # h1 = pq.sift_up_max(heap,a)
# for n in h1:
    # print(n)
# heap = []
# print('*********sift_down_max**********')
# for a in arr:
    # h2 = pq.sift_down_max(heap,a)
# for n in h2:
    # print(n)
# print('*********heapify_max**********')
# hpf = pq.heapify_max(arr)
# for n in hpf:
    # print(n)
# print('*********heap_sort_descend**********')
# hs = pq.heap_sort_descend(arr)
# for n in hs:
    # print(n)
# print('*********extract_max**********')
# hm = pq.extract_max(heap)
# print(hm[0])