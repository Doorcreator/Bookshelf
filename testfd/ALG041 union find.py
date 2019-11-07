# union find set
class Graph():
    def __init__(self):
        self.vertices = set()
        self.parent = {}
        self.edges = []
        self.flag = {}
    def add_edge(self,v,u,w):
        self.vertices.update({v,u})
        self.parent.update({v:v,u:u})
        self.edges.append([v,u,w])
    def find(self,child):
        parent = self.parent
        if parent[child] == child:
            return child
        else:
            parent[child] = self.find(parent[child])
            return parent[child]
    def union(self,v,u):
        parent = self.parent
        flag = self.flag
        flag.setdefault(u,0)
        vroot = self.find(v)
        uroot = self.find(u)
        if flag[u] == 0:
            parent[u] = v
            flag[u] = 1
        else:
            parent[v] = uroot
        for c,p in self.parent.items():
            self.parent[c] = self.find(p)

graph = [[1,2],[3,4],[5,2],[4,6],[2,6],[8,7],[9,7],[1,6],[2,4],[10,10]]
G = Graph()
for g in graph:
    G.add_edge(g[0],g[1],0)
for g in graph:
    G.union(g[0],g[1])
print(G.parent)

