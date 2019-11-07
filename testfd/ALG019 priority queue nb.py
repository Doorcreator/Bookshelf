# PriorityQueue implementation based on heap containing self-defined class Node as its elements.
# from ALG019_priority_queue_nb import PriorityQueue
class Node():
    def __init__(self,value=None,key=None):
        self.value = value
        self.key = key
class PriorityQueue():
    def __init__(self):
        pass
    def sift_up_min(self,heap,node):
    # Move an out-of-order element [node] from bottom to top of a heap. Min on the top of the heap.
    # Equivalent to push function.
        if type(node) == Node:
            new_elmt = node
        elif type(node) == int:
            new_elmt = Node(node)
        elif type(node) == tuple and len(node)==2:
            new_elmt = Node(node[0],node[1])
        else:
            return 'Error: incorrect argument type!'
        heap.append(new_elmt)
        n = len(heap)
        parent_pos = n//2 - 1
        while parent_pos >= 0:
            current_pos = 2*parent_pos + 1 if n%2==0 else 2*parent_pos + 2
            if heap[current_pos].value < heap[parent_pos].value:
                heap[current_pos],heap[parent_pos] = \
                heap[parent_pos],heap[current_pos]
                n = parent_pos + 1
                parent_pos = n//2 - 1
            else:
                break
        return heap
    def sift_down_min(self,heap,node):
    # Move an out-of-order element [new_elmt] from top to bottom of a heap. Min on the top of the heap.
    # Equivalent to push function.
        if type(node) == Node:
            new_elmt = node
        elif type(node) == int:
            new_elmt = Node(node)
        elif type(node) == tuple and len(node)==2:
            new_elmt = Node(node[0],node[1])
        else:
            return 'Error: incorrect argument type!'
        heap.append(new_elmt)
        heap[-1],heap[0] = heap[0],heap[-1]
        last_elmt = heap.pop()
        n = len(heap)
        parent_pos = 0
        while parent_pos <= n//2 - 1:
            left_child_pos = 2*parent_pos + 1
            right_child_pos = 2*parent_pos + 2
            try:
                current_pos = left_child_pos \
                if heap[left_child_pos].value < heap[right_child_pos].value \
                else right_child_pos
            except IndexError:
                current_pos = left_child_pos
            if heap[current_pos].value < heap[parent_pos].value:
                heap[current_pos],heap[parent_pos] = \
                heap[parent_pos],heap[current_pos]
                parent_pos = current_pos
            else:
                break
        self.sift_up_min(heap,last_elmt)
        return heap
    def extract_min(self,heap):
    # Extract the minimum value in a heap and restore the heap. Min on the top of the heap.
    # Equivalent to pop function.
        heap_min = heap[0]
        heap[-1],heap[0] = heap[0],heap[-1]
        heap.pop(-1)
        n = len(heap)
        parent_pos = 0
        while parent_pos <= n//2 - 1:
            left_child_pos = 2*parent_pos + 1
            right_child_pos = 2*parent_pos + 2
            try:
                current_pos = left_child_pos \
                if heap[left_child_pos].value < heap[right_child_pos].value \
                else right_child_pos
            except IndexError:
                current_pos = left_child_pos
            if heap[current_pos].value < heap[parent_pos].value:
                heap[current_pos],heap[parent_pos] = \
                heap[parent_pos],heap[current_pos]
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
    def get_key_index(self,heap,key):
    # Return the index of a node in the heap based on its key.
        i = 0
        while heap[i].key != key:
            i += 1
        if i > len(heap)-1:
            return None
        else:
            return i
    def get_value_index(self,heap,value):
    # Return the index of a node in the heap based on its value.
        i = 0
        while heap[i].value != value:
            i += 1
        if i > len(heap)-1:
            return None
        else:
            return i
    def remove(self,heap,index):
    # Remove a node in the heap based on its index in the heap.
        heap[-1],heap[index] = heap[index],heap[-1]
        heap.pop(-1)
        n = len(heap)
        parent_pos = index
        while parent_pos <= n//2 - 1:
            left_child_pos = 2*parent_pos + 1
            right_child_pos = 2*parent_pos + 2
            try:
                current_pos = left_child_pos \
                if heap[left_child_pos].value < heap[right_child_pos].value \
                else right_child_pos
            except IndexError:
                current_pos = left_child_pos
            if heap[current_pos].value < heap[parent_pos].value:
                heap[current_pos],heap[parent_pos] = \
                heap[parent_pos],heap[current_pos]
                parent_pos = current_pos
            else:
                break
        return heap
    def sift_up_max(self,heap,node):
    # Move an out-of-order element [node] from bottom to top of a heap. Max on the top of the heap.
    # Equivalent to push function.
        if type(node) == Node:
            new_elmt = node
        elif type(node) == int:
            new_elmt = Node(node)
        elif type(node) == tuple and len(node)==2:
            new_elmt = Node(node[0],node[1])
        else:
            return 'Error: incorrect argument type!'
        heap.append(new_elmt)
        n = len(heap)
        parent_pos = n//2 - 1
        while parent_pos >= 0:
            current_pos = 2*parent_pos + 1 if n%2==0 else 2*parent_pos + 2
            if heap[current_pos].value > heap[parent_pos].value:
                heap[current_pos],heap[parent_pos] = \
                heap[parent_pos],heap[current_pos]
                n = parent_pos + 1
                parent_pos = n//2 - 1
            else:
                break
        return heap
    def sift_down_max(self,heap,node):
    # Move an out-of-order element [new_elmt] from top to bottom of a heap. Max on the top of the heap.
    # Equivalent to push function.
        if type(node) == Node:
            new_elmt = node
        elif type(node) == int:
            new_elmt = Node(node)
        elif type(node) == tuple and len(node)==2:
            new_elmt = Node(node[0],node[1])
        else:
            return 'Error: incorrect argument type!'
        heap.append(new_elmt)
        heap[-1],heap[0] = heap[0],heap[-1]
        last_elmt = heap.pop()
        n = len(heap)
        parent_pos = 0
        while parent_pos <= n//2 - 1:
            left_child_pos = 2*parent_pos + 1
            right_child_pos = 2*parent_pos + 2
            try:
                current_pos = left_child_pos \
                if heap[left_child_pos].value > heap[right_child_pos].value \
                else right_child_pos
            except IndexError:
                current_pos = left_child_pos
            if heap[current_pos].value > heap[parent_pos].value:
                heap[current_pos],heap[parent_pos] = \
                heap[parent_pos],heap[current_pos]
                parent_pos = current_pos
            else:
                break
        self.sift_up_max(heap,last_elmt)
        return heap
    def extract_max(self,heap):
    # Extract the maximum value in a heap and restore the heap. Max on the top of the heap.
    # Equivalent to pop function
        heap_max = heap[0]
        heap[-1],heap[0] = heap[0],heap[-1]
        heap.pop(-1)
        n = len(heap)
        parent_pos = 0
        while parent_pos <= n//2 - 1:
            left_child_pos = 2*parent_pos + 1
            right_child_pos = 2*parent_pos + 2
            try:
                current_pos = left_child_pos \
                if heap[left_child_pos].value > heap[right_child_pos].value \
                else right_child_pos
            except IndexError:
                current_pos = left_child_pos
            if heap[current_pos].value > heap[parent_pos].value:
                heap[current_pos],heap[parent_pos] = \
                heap[parent_pos],heap[current_pos]
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

# arr = [(1,'a'),5,12,9,3,(6,'f'),(7,'g')]
# heap = []
# pq = PriorityQueue()
# print('*********min**********')
# print('*********sift_up_min**********')
# for a in arr:
    # h1 = pq.sift_up_min(heap,a)
# for n in h1:
    # vi = pq.get_value_index(h1,n.value)
    # h1 = pq.remove(h1,vi)
# heap = []
# print('*********sift_down_min**********')
# for a in arr:
    # h2 = pq.sift_down_min(heap,a)
# for n in h2:
    # print((n.key,n.value))
# print('*********heapify_min**********')
# hpf = pq.heapify_min(arr)
# for n in hpf:
    # print((n.key,n.value))
# print('*********heap_sort_ascend**********')
# hs = pq.heap_sort_ascend(arr)
# for n in hs:
    # print((n.key,n.value))
# print('*********extract_min**********')
# hm = pq.extract_min(heap)
# print(hm[0].value)
# heap = []
# print('*********max**********')
# print('*********sift_up_max**********')
# for a in arr:
    # h1 = pq.sift_up_max(heap,a)
# for n in h1:
    # print((n.key,n.value))
# heap = []
# print('*********sift_down_max**********')
# for a in arr:
    # h2 = pq.sift_down_max(heap,a)
# for n in h2:
    # print((n.key,n.value))
# print('*********heapify_max**********')
# hpf = pq.heapify_max(arr)
# for n in hpf:
    # print((n.key,n.value))
# print('*********heap_sort_descend**********')
# hs = pq.heap_sort_descend(arr)
# for n in hs:
    # print((n.key,n.value))
# print('*********extract_max**********')
# hm = pq.extract_max(heap)
# print(hm[0].value)