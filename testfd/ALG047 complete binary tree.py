# complete binary tree (CBT)
# A node-based CBT and its insertion and search methods.
from ALG024_queue import Queue
class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class CBT():
    def __init__(self):
        self.root = None
        self.que = Queue([])
    def insert(self,leaf):
        node = Node(leaf)
        que = self.que
        if self.root == None:
            self.root = node
            que.enqueue(self.root)
        else:
            while not que.is_empty():
                cur_node = que.dequeue()
                if cur_node.left == None:
                    cur_node.left = node
                    que.enqueue(cur_node)
                    return
                elif cur_node.right == None:
                    cur_node.right = node
                    que.enqueue(cur_node.left)
                    return
                else:
                    que.enqueue(cur_node.right)
    def search(self,leaf):
        que = Queue([])
        cur_node = self.root
        if cur_node.value == leaf:
            return True
        else:
            que.enqueue(cur_node)
            while not que.is_empty():
                cur_node = que.dequeue()
                try:
                    if cur_node.left.value == leaf:
                        return True
                    elif cur_node.right.value == leaf:
                        return True
                    else:
                        que.enqueue(cur_node.left)
                        que.enqueue(cur_node.right)
                except AttributeError:
                    if cur_node.left == leaf:
                        return True
                    elif cur_node.left == leaf:
                        return True
        return False

arr = [2,4,13,22,3,89,96,28,32,50,45]
T = CBT()
for a in arr:
    T.insert(a)
for a in arr:
    print(T.search(a))