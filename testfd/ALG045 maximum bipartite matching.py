# Find maximum bipartite matching (MBM) for an undirected bipartite graph (BPG)
# ref: https://www.geeksforgeeks.org/maximum-bipartite-matching/
class Graph():
    def __init__(self):
        self.edges = {}
        self.paired = {}
        self.visited = {}
    def add_edge(self,v,u):
        edges = self.edges
        edges.setdefault(v,[])
        edges[v].append(u)
        edges.setdefault(u,[])
        edges[u].append(v)
    def traverse(self,v):
        edges = self.edges
        paired = self.paired
        visited = self.visited
        for j in range(len(edges[v])):
            u = edges[v][j]
            if visited[u] == False:
                visited[u] = True
                if paired[u] == None or self.traverse(paired[u]):
                    paired[u] = v
                    paired[v] = u
                    return True
        return False
    def MBM(self,edges):
        edges = self.edges
        paired = self.paired
        visited = self.visited
        flag = set()
        total_pair = []
        for v in edges:
            paired[v] = None
            visited[v] = False
        for v in edges:
            if paired[v] == None:
                self.traverse(v)
        for v in edges:
            if paired[v] and v not in flag:
                flag.add(paired[v])
                total_pair.append((v,paired[v]))
        return total_pair

graph = [[1,2],[1,3],[2,1],[2,4],[4,3],[6,6],[3,3],[4,4]]
G = Graph()
for e in graph:
    G.add_edge(e[0],e[1])
print(G.MBM(G.edges))
