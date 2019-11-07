# minimum spanning tree (MST)
# ref: https://algs4.cs.princeton.edu/43mst/
# V01: union-find-set-based Kruskal's algorithm
class Graph():
    def __init__(self):
        self.vertices = set()
        self.parent = {}
        self.edges = []
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
        vroot = self.find(v)
        uroot = self.find(u)
        if vroot == uroot:
            return 0
        else:
            parent[uroot] = vroot
            return 1
    def Kruskal_MST(self,edges):
        edges = self.edges
        sedges = sorted(edges,key = lambda item:item[2])
        count = 0
        MST = []
        for e in sedges:
            if self.union(e[0],e[1]):
                count += 1
                MST.append((e[0],e[1],e[2]))
            if count == len(self.vertices) - 1:
                break
        return MST
graph = [[2,4,11],[3,5,13],[4,6,3],[5,6,4],[2,3,6],[4,5,7],[1,2,1],[3,4,9],[1,3,2]]
G = Graph()
for g in graph:
    G.add_edge(g[0],g[1],g[2])
print(G.Kruskal_MST(G.edges))

# V02: priority-queue-based Prim's algorithm
# graph represented by adjacency list
from ALG019_priority_queue_nb import PriorityQueue
class Graph():
    def __init__(self):
        self.vertices = set()
        self.edges = {}
    def add_edge(self,v,u,w):
        edges = self.edges
        self.vertices.update({v,u})
        edges.setdefault(v,{})
        edges[v].update({u:w})
        edges.setdefault(u,{})
        edges[u].update({v:w})
    def Prim_MST(self,edges):
        vertices = self.vertices
        edges = self.edges
        total_vertex = len(vertices)
        dist = {}
        MST = []
        unvisited = vertices
        v0 = vertices.pop()
        unvisited.discard(v0)
        count = 1
        heap = []
        pq = PriorityQueue()
        while count < total_vertex:
            count += 1
            for e in edges[v0].items():
                dist[(v0,e[0])] = e[1]
                pq.sift_up_min(heap,(e[1],(v0,e[0])))
            next_edge = pq.extract_min(heap)[0].key
            while not next_edge[1] in unvisited:
                next_edge = pq.extract_min(heap)[0].key
            v0 = next_edge[1]
            unvisited.discard(next_edge[1])
            MST.append((next_edge,dist[(next_edge)]))
        return MST
G = Graph()
graph = [[2,4,11],[3,5,13],[4,6,3],[5,6,4],[2,3,6],[4,5,7],[1,2,1],[3,4,9],[1,3,2]]
for g in graph:
    G.add_edge(g[0],g[1],g[2])
print(G.Prim_MST(G.edges))

# Performance
#data size  V01     V02
#250:       0.05    0.12
#1000:      0.33    0.84
#10000:     2.9     7.1