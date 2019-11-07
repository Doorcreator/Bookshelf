# from ALG024_queue import Queue
# queue: a data structure characterized by a pop order of FIFO.
class Queue(object):
    def __init__(self,queue):
        self.queue = queue
        self.head = 0
        self.tail = len(self.queue)
    def enqueue(self,element):
        self.queue.append('')
        self.queue[self.tail] = element
        self.tail += 1
    def dequeue(self):
        dequeue_item = self.queue[self.head]
        self.head += 1
        self.queue = self.queue[self.head:self.tail]
        self.head -= 1
        self.tail = len(self.queue)
        return dequeue_item
    def get(self):
        return self.queue[self.head]
    def is_empty(self):
        return self.head >= self.tail
    def size(self):
        return len(self.queue[self.head:self.tail])
    def clear(self):
        self.head = self.tail
        self.queue = self.queue[self.head:self.tail]
def q_test01(queue):
    q = []
    while len(queue)>0:
        ele2q = queue.pop(0)
        q.append(ele2q)
        if len(queue)>0:
            ele2a = queue.pop(0)
            queue.append(ele2a)
    return q
def q_test02(queue):
    q = []
    head = -1
    tail = len(queue)-1
    while head < tail:
        head += 2
        if head > tail:
            break
        queue.append(queue[head])
        tail += 1
    for i in range(0,len(queue),2):
        q.append(queue[i])
    return q
def q_test03(queue):
    q = []
    head = 0
    tail = len(queue)
    while head < tail:
        head += 1
        queue.append('')
        queue[tail] = queue[head]
        head += 1
        tail += 1
    for i in range(0,len(queue),2):
        q.append(queue[i])
    return q
# V04: implemented with the Queue class
def q_test04(queue):
    q1 = Queue(queue)
    q2 = Queue([])
    while not q1.is_empty():
        r2 = q2.enqueue(queue[0])
        r1 = q1.dequeue()
        if not q1.is_empty():
            q1.enqueue(r1[0])
            queue = q1.dequeue()
    return q2.queue
a = [6,3,1,7,5,8]
q = Queue([])
# for i in a:
    # q.enqueue(i)
    # print('queue:%s'%q.queue)
    # print('head:%s'%q.head)
    # print('tail:%s'%q.tail)
    # print('empty:%s'%q.is_empty())
    # print('size:%s'%q.size())
# print('*****************')
# for i in a:
    # dq = q.dequeue()
    # print('dq:%s'%dq)
    # print('queue:%s'%q.queue)
    # print('head:%s'%q.head)
    # print('tail:%s'%q.tail)
    # print('empty:%s'%q.is_empty())
    # print('size:%s'%q.size())
    # if not q.is_empty():
        # print('get:%s'%q.get())
# print('*****************')
# q.enqueue(a)
# print('queue:%s'%q.queue)
# print('empty:%s'%q.is_empty())
# print('size:%s'%q.size())
# q.clear()
# print('queue:%s'%q.queue)
# print('empty:%s'%q.is_empty())
# print('size:%s'%q.size())
