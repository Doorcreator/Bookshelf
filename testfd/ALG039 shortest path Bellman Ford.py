# Bellman-Ford: To find the shortest paths from one vertex to all the other vertices in a graph.
# Bellman-Ford algorithm distinguishes itself from Dijkstra algorithm by its capacity of handling negatively-weighted edges and detecting negatively-weighted loops in the graph. This is realized by iterating over every vertices impartially instead of iterating from a vertex with the shortest distance from the source vertex in each round. The cost is time complexity increasing from O(ElogV) to O(VE), where V is the number of vertices and E is the number of edges.

inf = float('inf')
# graph without loops or multiple ingoing/outgoing edges
adj_list01 = {
'A':{'B':-3},
'B':{'C':2},
'C':{'D':3},
'D':{'E':2},
'E':{'E':0}
}
# graph without loops
adj_list02 = {
'A':{'B':-3,'E':5},
'B':{'C':2,'E':5},
'C':{'D':3},
'D':{'E':2},
'E':{'E':0}
}
# graph without negatively-weighted loops
adj_list03 = {
'A':{'B':-3,'E':5},
'B':{'C':2,'D':4,'E':5},
'C':{'D':3},
'D':{'E':2},
'E':{'C':1}
}
# graph with negatively-weighted loops
adj_list04 = {
'A':{'B':-3,'E':5},
'B':{'C':2,'D':-4,'E':5},
'C':{'D':3},
'D':{'E':2},
'E':{'C':-10}
}
# V01
def traverse01(v0):
    dist = {}
    visited = set()
    dist.setdefault((v0,v0),0)
    for vi in adj_list:
        dist.setdefault((v0,vi),inf)
    for vu in adj_list:
        sentinel = 0
        if vu not in visited:
            for it in adj_list[vu].items():
                vk = it[0]
                wt = it[1]
                if dist[(v0,vk)] > dist[(v0,vu)] + wt:
                    dist[(v0,vk)] = dist[(v0,vu)] + wt
                    sentinel = 1
            visited.add(vu)
            # To guarantee an early exit from the iteration.
            if sentinel == 0:
                break
    # To detect negatively-weighted loops.
    for vu in adj_list:
        for it in adj_list[vu].items():
            vk = it[0]
            wt = it[1]
            if dist[(v0,vk)] > dist[(v0,vu)] + wt:
                return 'There is a negatively weighted loop in the graph!'
    return dist
# V02: optimized with queue
from ALG024_queue import Queue
def traverse02(v0):
    dist = {}
    que = Queue([])
    que.enqueue(v0)
    dist.setdefault((v0,v0),0)
    for vi in adj_list:
        dist.setdefault((v0,vi),inf)
    count = 0
    while not que.is_empty():
        count += 1
        vu = que.get()
        sentinel = 0
        for it in adj_list[vu].items():
            vk = it[0]
            wt = it[1]
            if dist[(v0,vk)] > dist[(v0,vu)] + wt:
                dist[(v0,vk)] = dist[(v0,vu)] + wt
                sentinel = 1
                que.enqueue(vk)
        que.dequeue()
        if count > vertex_num-1 and sentinel == 1:
            return 'There is a negatively weighted loop in the graph!'
    return dist
if __name__=='__main__':
    for al in [adj_list01,adj_list02,adj_list03,adj_list04]:
        adj_list = al
        v0 = tuple(list(adj_list)[0])[0]
        # vertex_num: number of vertices in the graph
        vertex_num = len(adj_list)
        print(traverse01(v0))
        print(traverse02(v0))