# binary search tree (BST)
# ref:
# https://www.geeksforgeeks.org/binary-search-tree-data-structure/
# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
from ALG024_queue import Queue
class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
class BST():
    def __init__(self):
        self.root = None
        self.que = Queue([])
        self.visit_order = []
    # queue-based insertion and search
    # ********************************
    def insert01(self,leaf):
        node = Node(leaf)
        que = self.que
        if self.root == None:
            self.root = node
        else:
            que.enqueue(self.root)
            while not que.is_empty():
                cur_node = que.dequeue()
                if leaf < cur_node.value:
                    if cur_node.left == None:
                        cur_node.left = node
                        return
                    else:
                        que.enqueue(cur_node.left)
                elif leaf >= cur_node.value:
                    if cur_node.right == None:
                        cur_node.right = node
                        return
                    else:
                        que.enqueue(cur_node.right)
    def search01(self,leaf):
        que = Queue([])
        if leaf == self.root.value:
            return True
        else:
            que.enqueue(self.root)
            while not que.is_empty():
                cur_node = que.dequeue()
                try:
                    if leaf < cur_node.value:
                        if leaf == cur_node.left.value:
                            return True
                        else:
                            que.enqueue(cur_node.left)
                    elif leaf > cur_node.value:
                        if leaf == cur_node.right.value:
                            return True
                        else:
                            que.enqueue(cur_node.right)
                except AttributeError:
                    return False
    # recursion-based insertion and search
    # ********************************
    def insert02(self,leaf):
        node = Node(leaf)
        if self.root == None:
            self.root = node
        else:
            if leaf < self.root.value:
                if self.root.left == None:
                    self.root.left = node
                else:
                    parent = self.root
                    self.root = self.root.left
                    self.insert02(leaf)
                    self.root = parent
            else:
                if self.root.right == None:
                    self.root.right = node
                else:
                    parent = self.root
                    self.root = self.root.right
                    self.insert02(leaf)
                    self.root = parent
    def search02(self,leaf):
        if self.root == None:
            return False
        elif leaf == self.root.value:
            return True
        else:
            try:
                if leaf < self.root.value:
                    parent = self.root
                    self.root = self.root.left
                    result = self.search02(leaf)
                    self.root = parent
                elif leaf > self.root.value:
                    parent = self.root
                    self.root = self.root.right
                    result = self.search02(leaf)
                    self.root = parent
            except AttributeError:
                self.root = parent
                return False
        return result
    def insert03(self,root,leaf):
        node = Node(leaf)
        if self.root == None:
            self.root = node
        elif leaf < root.value:
            if root.left == None:
                root.left = node
            else:
                self.insert03(root.left,leaf)
        elif leaf > root.value:
            if root.right == None:
                root.right = node
            else:
                self.insert03(root.right,leaf)
    def search03(self,root,leaf):
        while root:
            if self.root == None:
                return False
            elif root.value == leaf:
                return True
            elif leaf < root.value:
                return self.search03(root.left,leaf)
            elif leaf > root.value:
                return self.search03(root.right,leaf)
        return False
    # four tree traversal methods
    # **************************************
    def pre_order_traverse(self,node):
        if node != None:
            self.visit_order.append(node.value)
            self.pre_order_traverse(node.left)
            self.pre_order_traverse(node.right)
        return self.visit_order
    def post_order_traverse(self,node):
        if node != None:
            self.post_order_traverse(node.left)
            self.post_order_traverse(node.right)
            self.visit_order.append(node.value)
        return self.visit_order
    def in_order_traverse(self,node):
        if node != None:
            self.in_order_traverse(node.left)
            self.visit_order.append(node.value)
            self.in_order_traverse(node.right)
        return self.visit_order
    def level_order_traverse(self,node):
        que = Queue([])
        if node != None:
            que.enqueue(self.root)
            while not que.is_empty():
                cur_node = que.dequeue()
                self.visit_order.append(cur_node.value)
                if cur_node.left:
                    que.enqueue(cur_node.left)
                if cur_node.right:
                    que.enqueue(cur_node.right)
        return self.visit_order
    # To construct a level-order BST from given pre-order traversal of the BST.
    def pre2level_order(self,array):
        for a in array:
            self.insert01(a)
        v0 = self.root
        self.visit_order.clear()
        self.level_order_traverse(v0) # Other traversals may also be generated by traversing the tree from the root v0.
        return self.visit_order
    # To construct a level-order BST from given post-order traversal of the BST.
    def post2level_order(self,array):
        for a in array[::-1]:
            self.insert01(a)
        v0 = self.root
        self.visit_order.clear()
        self.level_order_traverse(v0) # Other traversals may also be generated by traversing the tree from the root v0.
        return self.visit_order
    # To delete a node from the BST.
    # Case 1: zero-child node
    # Move the pointer of the node's parent to None.
    # Case 2: one-child node
    # Move the pointer of the node's parent to the node's direct child, and make the node's direct child submit to the node's parent.
    # Case 3: two-children node
    # Replace the value of the node with a node with minimum value in the right subtree (relative to the node to be deleted) or a node with maximum value in the left subtree (relative to the node to be deleted), and recur down the right or left subtree (based on the node selected for replacement) to delete the node for replacement.
    # Conventional node structure (i.e., node with value, left, and right properties only) is widely used in BST deletion as in Delete Method 01 herein, but it is somewhat tricky to understand for adoption of multiple layers of recursion and assignment. A concise solution to this problem is to employ a new node structure ((i.e., node with parent property in addition to value, left, and right properties)) as in Delete Method 02 herein.
    # *************************************
    def find_subtree_max(self,root):
        if root.right != None:
            return self.find_subtree_max(root.right)
        else:
            if root.left != None:
                return root.left
            else:
                return root
    def find_subtree_min(self,root):
        if root.left != None:
            return self.find_subtree_min(root.left)
        else:
            return root
    # Delete Method 01:
    # *************************************
    def delete(self,root,leaf):
        if leaf < root.value:
            root.left = self.delete(root.left,leaf)
        elif leaf > root.value:
            root.right = self.delete(root.right,leaf)
        else:
            if root.left == None:
                temp = root.right
                return temp
            elif root.right == None:
                temp = root.left
                return temp
            # 1. Uncomment the following to replace the deleted node with the node with maximum value in the left subtree.
            # lstmax = self.find_subtree_max(root.left)
            # root.value = lstmax.value
            # root.left = self.delete(root.left,lstmax.value)
            # 2. Comment the following to replace the deleted node with the node with maximum value in the left subtree.
            rstmin = self.find_subtree_min(root.right)
            root.value = rstmin.value
            root.right = self.delete(root.right,rstmin.value)
        return root
    def delete01(self,root,leaf):
        if root == self.root and root.left == None and root.right == None:
            self.root = None
        elif root.left == None:
            rstmin = self.find_subtree_min(root.right)
            root.value = rstmin.value
            root.right = self.delete(root.right,rstmin.value)
        elif root.right == None:
            rstmin = self.find_subtree_min(root.left)
            root.value = rstmin.value
            root.left = self.delete(root.left,rstmin.value)
        else:
            self.delete(root,leaf)
    # Delete Method 02:
    # *************************************
    def insert04(self,root,leaf):
        node = Node(leaf)
        if self.root == None:
            self.root = node
        elif leaf < root.value:
            if root.left == None:
                root.left = node
                root.left.parent = root
            else:
                self.insert04(root.left,leaf)
        elif leaf > root.value:
            if root.right == None:
                root.right = node
                root.right.parent = root
            else:
                self.insert04(root.right,leaf)
    def delete02(self,root,leaf):
        if leaf < root.value:
            self.delete02(root.left,leaf)
        elif leaf > root.value:
            self.delete02(root.right,leaf)
        else:
            if root.left == None and root.right == None:
                if root.parent == None:
                    self.root = None
                elif root.parent.left == root:
                    root.parent.left = None
                elif root.parent.right == root:
                    root.parent.right = None
            elif root.left == None and root.right != None:
                if root.parent == None:
                    self.root = root.right
                    self.root.parent = None
                elif root.parent.left == root:
                    root.parent.left = root.right
                    root.right.parent = root.parent
                elif root.parent.right == root:
                    root.parent.right = root.right
                    root.right.parent = root.parent
            elif root.left != None and root.right == None:
                if root.parent == None:
                    self.root = root.left
                    self.root.parent = None
                elif root.parent.left == root:
                    root.parent.left = root.left
                    root.left.parent = root.parent
                elif root.parent.right == root:
                    root.parent.right = root.left
                    root.left.parent = root.parent
            else:
                rstmin = self.find_subtree_min(root.right)
                root.value = rstmin.value
                self.delete02(root.right,rstmin.value)

# arr = [25,15,50,10,22,35,70,4,12,18,24,31,44,66,90]
# arr = [25,15,10,4,12,22,18,24,50,35,31,44,70,66,90] # pre-order
# arr = [4,12,10,18,24,22,15,31,44,35,66,90,70,50,25] # post-order
# arr = [4,10,12,15,18,22,24,25,31,35,44,50,66,70,90] # in-order
# arr = [25,15,50,10,22,35,70,4,12,18,24,31,44,66,90] # level-order
# T = BST()
# for a in arr:
    # T.insert01(a)
    # T.insert02(a)
    # T.insert03(T.root,a)
    # T.insert04(T.root,a)
# for a in arr:
    # print(T.search01(a))
    # print(T.search01(45))
    # print(T.search02(a))
    # print(T.search02(45))
    # print(T.search03(T.root,a))
    # print(T.search03(T.root,42))
# for a in arr:
    # T.delete01(T.root,a)
    # T.delete02(T.root,a)
    # T.level_order_traverse(T.root)
    # print(T.visit_order)
    # T.visit_order = []
# T.pre_order_traverse(T.root)
# print(T.visit_order)
# traversal = [T.pre_order_traverse,T.post_order_traverse,T.in_order_traverse,T.level_order_traverse]
# v0 = T.root
# for t in traversal:
    # t(v0)
    # print(repr(t)+':%s'%T.visit_order)
    # T.visit_order = []
# print(T.pre2level_order(arr))
# print(T.post2level_order(arr))
# print(T.find_subtree_min(T.root.right).value)
# print(T.find_subtree_max(T.root.right).value)
