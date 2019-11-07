from ALG019_priority_queue import PriorityQueue
import random
# To find the first k biggest numbers in an array.
def first_k_biggest(k,array):
    pq = PriorityQueue()
    base_elmts = random.sample(array,k)
    left_elmts = set(array).difference(set(base_elmts))
    hp = pq.heapify_min(base_elmts)
    for e in left_elmts:
        pq.sift_up_min(hp,e)
        pq.extract_min(hp)
    return hp
# To find the first k smallest numbers in an array.
def first_k_smallest(k,array):
    pq = PriorityQueue()
    base_elmts = random.sample(array,k)
    left_elmts = set(array).difference(set(base_elmts))
    hp = pq.heapify_max(base_elmts)
    for e in left_elmts:
        pq.sift_up_max(hp,e)
        pq.extract_max(hp)
    return hp

arr = [12,98,43,22,86,55,54,37,2,23,41]
print(first_k_biggest(3,arr))
print(first_k_smallest(3,arr))
