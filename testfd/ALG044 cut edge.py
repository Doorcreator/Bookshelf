# Find cut edges in a graph
# V01: union find set
# To be debugged due to failure to handle cycled graphs.
class Graph():
    def __init__(self):
        self.parent = {}
        self.flag = {}
    def add_edge(self,v,u):
        self.parent.update({v:v,u:u})
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
            while parent[v] != v:
                v = self.find(v)
            parent[v] = uroot
        for c,p in self.parent.items():
            self.parent[c] = self.find(p)
    def traverse(self,graph):
        results = []
        uniroot = set()
        for i in range(len(graph)):
            k = 0
            for e in graph:
                if i != k:
                    self.add_edge(e[0],e[1])
                else:
                    self.add_edge(e[0],e[0])
                    self.add_edge(e[1],e[1])
                k += 1
            k = 0
            for e in graph:
                if i != k:
                    self.union(e[0],e[1])
                k += 1
            for root in self.parent.values():
                uniroot.add(root)
            if len(uniroot) > 1:
                results.append(graph[i])
            uniroot = set()
            self.parent = {}
            self.flag = {}
        return results

graph = [[1,4],[1,3],[4,2],[3,2],[2,5],[5,6]]   # (2,5),(5,6)
G = Graph()
print(G.traverse(graph))

# V02: Tarjan's algorith
class Graph():
    def __init__(self):
        self.vertices = set()
        self.edges = {}
        self.nearest_grandpa = {}
        self.DFS_depth = {}
        self.parent = {}
        self.visited = {}
        self.cut_vertex = set()
    def add_edge(self,v,u):
        edges = self.edges
        self.vertices.update({v,u})
        edges.setdefault(v,[])
        edges[v].append(u)
        edges.setdefault(u,[])
        edges[u].append(v)
    def traverse(self,v,i):
        edges = self.edges
        DFS_depth = self.DFS_depth
        parent = self.parent
        visited = self.visited
        cut_vertex = self.cut_vertex
        nearest_grandpa = self.nearest_grandpa
        children = 0
        DFS_depth.setdefault(v,i)
        nearest_grandpa.setdefault(v,i)
        visited[v] = True
        for j in range(len(edges[v])):
            u = edges[v][j]
            if not visited[u]:
                children += 1
                parent[u] = v
                i += 1
                self.traverse(u,i)
                nearest_grandpa[v] = min(nearest_grandpa[u],nearest_grandpa[v])
                if parent[v] == None and children > 1:
                    cut_vertex.ad((v,u))
                elif parent[v] != None and nearest_grandpa[u] > DFS_depth[v]:
                    cut_vertex.add((v,u))
            elif u != parent[v]:
                nearest_grandpa[v] = min(nearest_grandpa[v],DFS_depth[u])
    def Tarjan(self,graph):
        for e in graph:
            self.add_edge(e[0],e[1])
        for v in self.edges:
            self.parent[v] = None
            self.visited[v] = False
        for v in self.edges:
            if self.visited[v] == False:
                self.traverse(v,0)
        return self.cut_vertex

G = Graph()
print(G.Tarjan(graph))

