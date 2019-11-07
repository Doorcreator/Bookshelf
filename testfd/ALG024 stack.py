# stack: a data structure characterized by a pop order of LIFO.
# from ALG024_stack import Stack
class Stack():
    def __init__(self,stack):
        self.stack = stack
        self.head = 0
        self.tail = len(self.stack)
    def push(self,element):
        self.stack.append('')
        self.stack[self.tail] = element
        self.tail += 1
    def pop(self):
        self.tail -= 1
        pop_item = self.stack[self.tail]
        self.stack = self.stack[self.head:self.tail]
        return pop_item
    def peek(self):
        return self.stack[self.tail-1]
    def is_empty(self):
        return self.head >= self.tail
    def size(self):
        return len(self.stack[self.head:self.tail])
    def clear(self):
        self.head = self.tail
        self.stack = self.stack[self.head:self.tail]
def palindrome01(string):
    mid = len(string)//2
    i = 0
    j = len(string)-1
    t = 0
    while i< mid:
        if string[i]==string[j]:
            t += 1
            i += 1
            j -= 1
        else:
            break
    if t == mid:
        return True
    else:
        return False
def palindrome02(string):
    s1 = Stack([])
    s2 = Stack(string)
    mid = len(string)//2
    i = 0
    while i< mid:
        s1.push(string[i])
        i += 1
    if ''.join(s1.stack) == string[:mid]:
        return True
    else:
        return False
# a = [10,1,3,9,12,5]
# s = Stack([])
# for i in a:
    # s.push(i)
    # print('stack:%s'%s.stack)
    # print('empty:%s'%s.is_empty())
    # print('size:%s'%s.size())
    # print('peek:%s'%s.peek())
# print('*****************')
# for i in a:
    # s.pop()
    # print('stack:%s'%s.stack)
    # print('empty:%s'%s.is_empty())
    # print('size:%s'%s.size())
    # if not s.is_empty():
        # print('peek:%s'%s.peek())
# print('*****************')
# s.push(a)
# print('stack:%s'%s.stack)
# print('empty:%s'%s.is_empty())
# print('size:%s'%s.size())
# s.clear()
# print('stack:%s'%s.stack)
# print('empty:%s'%s.is_empty())
# print('size:%s'%s.size())
