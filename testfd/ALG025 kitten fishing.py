class Queue():
    def __init__(self,queue):
        self.queue = queue
    def enqueue(self,element):
        self.queue.append(element)
    def dequeue(self):
        ele = self.queue.pop(0)
        return ele
    def is_empty(self):
        if self.size > 0:
            return False
        else:
            return True
    def size(self):
        return len(self.queue)
    def clear(self):
        self.queue.clear()
class Stack():
    def __init__(self,stack):
        self.stack = stack
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        ele = self.stack.pop(-1)
        return ele
    def is_empty(self):
        if self.size > 0:
            return False
        else:
            return True
    def size(self):
        return len(self.stack)
    def clear(self):
        self.stack.clear()
def kitten_fishing(q1,q2,cards_on_desk):
    while q1.size()>0 and q2.size()>0:
        card_played = q1.dequeue()
        if card_played not in cards_on_desk.stack:
            cards_on_desk.push(card_played)
        else:
            cards_on_desk.push(card_played)
            t=0
            while t>=0 and t<2:
                card_winned = cards_on_desk.pop()
                q1.enqueue(card_winned)
                if card_winned == card_played:
                    t += 1
            q1,q2 = q2,q1
            return kitten_fishing(q1,q2,cards_on_desk)
        q1,q2 = q2,q1
        return kitten_fishing(q1,q2,cards_on_desk)
    return q1.queue,cards_on_desk.stack
q1 = Queue([2,4,1,2,5,6,5])
q2 = Queue([3,1,3,5,6,4,9])
s = Stack([])
print(kitten_fishing(q1,q2,s))






