# Traversal of a tree represented by adjacency list.
# ref: https://www.tutorialspoint.com/data_structures_algorithms/tree_traversal.htm
from ALG024_queue import Queue
class Tree():
    def __init__(self):
        self.edges = {}
        self.nodes = set()
        self.visit_order = []
        self.visited = {}
    def add_edge(self,v,u):
        self.edges.setdefault(v,[])
        self.edges[v].append(u)
        self.nodes.update({v,u})
    # DFS
    #*****************************************
    def pre_order_traverse(self,v):
    # traversal order: root->left->right
        self.visit_order.append(v)
        edges = self.edges
        for i in range(len(edges)):
            try:
                u = edges[v][i]
                if self.visited[u] == False:
                    self.visited[u] = True
                    self.pre_order_traverse(u)
                    self.visited[u] = False
            except (KeyError,IndexError):
                return
    def post_order_traverse(self,v):
    # traversal order: left->right->root
        edges = self.edges
        for i in range(len(edges)):
            try:
                u = edges[v][i]
                if self.visited[u] == False:
                    self.visited[u] = True
                    self.post_order_traverse(u)
                    self.visited[u] = False
            except (KeyError,IndexError):
                self.visit_order.append(v)
                return
    def in_order_traverse(self,v):
    # traversal order: left->root->right
        edges = self.edges
        for i in range(len(edges)):
            try:
                u = edges[v][i]
                if self.visited[u] == False:
                    self.visited[u] = True
                    self.in_order_traverse(u)
                    self.visited[u] = False
                    if v not in self.visit_order:
                        self.visit_order.append(v)
            except (KeyError,IndexError):
                if v not in self.visit_order:
                    self.visit_order.append(v)
                return
    # BFS
    #*****************************************
    def level_order_traverse(self,v):
    # traversal order: level by level
        que = Queue([v])
        self.visit_order.append(v)
        while not que.is_empty():
            v = que.dequeue()
            for i in range(len(self.edges)):
                try:
                    u = self.edges[v][i]
                    self.visit_order.append(u)
                    que.enqueue(u)
                except (KeyError,IndexError):
                    break

# tree = [['A','B'],['A','C'],['B','D'],['B','E'],['C','F'],['C','G']]
# tree = [['50','30'],['50','70'],['30','20'],['70','60'],['70','80'],['30','40']]
tree = [[25,15],[25,50],[15,10],[15,22],[50,35],[50,70],[10,4],
[10,12],[22,18],[22,24],[35,31],[35,44],[70,66],[70,90]]
T = Tree()
for e in tree:
    T.add_edge(e[0],e[1])
    T.visited[e[0]]=False
    T.visited[e[1]]=False
v0 = list(T.edges)[0]
traversal = [T.pre_order_traverse,T.post_order_traverse,T.in_order_traverse,T.level_order_traverse]
for t in traversal:
    t(v0)
    print(repr(t)+':%s'%T.visit_order)
    T.visit_order = []