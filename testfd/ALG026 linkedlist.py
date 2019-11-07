# from ALG026_linkedlist import LinkedList
class Node():
    def __init__(self,item = None,cursor = None):
    # To define a node class for LinkedList class.
        self.item = item
        self.cursor = cursor
class LinkedList():
    # To define a singly linked list.
    def __init__(self):
        self.head = Node()
    def length(self):
    # To get the total number of nodes in the LinkedList.
        count = 0
        cur_node = self.head
        while cur_node.cursor != None:
            cur_node = cur_node.cursor
            count += 1
        return count
    def get_index(self,item):
    # To get the index of an item in the LinkedList.
        index = 0
        cur_node = self.head
        while cur_node.cursor != None:
            if cur_node.item == item:
                return index
            else:
                cur_node = cur_node.cursor
                index += 1
        if cur_node.item == item:
            return index
        else:
            return '%s is not in the list!'%item
    def insert(self,index,item):
    # To insert an item at the specified position.
        node = Node(item)
        cur_node = self.head
        if index <= 0:
            if self.length() == 0:
                cur_node.cursor = node
                return
            else:
                tmp_node = cur_node.cursor
                cur_node.cursor = node
                node.cursor = tmp_node
                return
        elif index >= self.length():
            while cur_node.cursor != None:
                cur_node = cur_node.cursor
            cur_node.cursor = node
            return
        else:
            while cur_node.cursor != None:
                if self.get_index(cur_node.item) == index:
                    tmp_node = cur_node.cursor
                    cur_node.cursor = node
                    node.cursor = tmp_node
                    return
                else:
                    cur_node = cur_node.cursor
    def append(self,item):
    # To append an item at the tail of the LinkedList.
        node = Node(item)
        cur_node = self.head
        while cur_node.cursor != None:
            cur_node = cur_node.cursor
        cur_node.cursor = node
    def append_simp(self,item):
    # Another version of append() function using insert() function.
        self.insert(self.length(),item)
    def remove(self,item):
    # To remove an item at its first occurrence.
        cur_node = self.head
        if self.length() == 0:
            return 'Cannot delete an element from an empty list!'
        if self.length() == 1:
            if cur_node.cursor.item == item:
                cur_node.cursor = None
                return
            else:
                return 'Cannot remove an element not contained in the list!'
        else:
            while cur_node.cursor != None:
                if cur_node.item == item:
                    cur_node.item = cur_node.cursor.item
                    cur_node.cursor = cur_node.cursor.cursor
                    return
                elif cur_node.cursor.item == item and cur_node.cursor.cursor == None:
                    cur_node.cursor = None
                    return
                else:
                    cur_node = cur_node.cursor
            else:
                return 'Cannot remove an element not contained in the list!'
    def pop(self,index):
    # To remove an item according to its index.
        cur_node = self.head
        if self.length() == 0:
            return 'Cannot pop an element from an empty list!'
        if self.length() == 1:
            if index == 1:
                cur_node.cursor = None
                return
            else:
                return 'Index out of range!'
        else:
            while cur_node.cursor != None:
                if self.get_index(cur_node.item) == index:
                    cur_node.item = cur_node.cursor.item
                    cur_node.cursor = cur_node.cursor.cursor
                    return
                elif self.get_index(cur_node.cursor.item) == index and cur_node.cursor.cursor == None:
                    cur_node.cursor = None
                    return
                else:
                    cur_node = cur_node.cursor
            else:
                return 'Index out of range!'
    def search(self,item):
    # To search an item and return True if it exists in the LinkedList or False otherwise.
        cur_node = self.head
        if self.length() == 1:
            if cur_node.cursor.item == item:
                return True
            else:
                return False
        else:
            while cur_node.cursor != None:
                if cur_node.item == item:
                    return True
                else:
                    cur_node = cur_node.cursor
            return False
    def iterator(self):
    # To return an self-defined iterator.
        return LinkedListIterator(self)
class LinkedListIterator():
    # To define an iterator for the LinkedList.
    def __init__(self,linked_list):
        self.linked_list = linked_list
        self.cur_node = self.linked_list.head
    def __next__(self):
        try:
            self.cur_node = self.cur_node.cursor
            return self.cur_node.item
        except AttributeError:
            raise StopIteration()
    def __iter__(self):
        return self
# LL = LinkedList()
# LL.append(10)
# LL.append(13)
# LL.append(14)
# LLit = LL.iterator() # equivalent to: LLit = LinkedListIterator(LL)
# for i in range(5):
    # print(next(LLit))