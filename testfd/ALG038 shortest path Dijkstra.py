# Dijkstra: To find the shortest paths from one vertex to all the other vertices in a graph.
# Dijkstra algorithm is based on the fact that the shortest path between two vertices (Vi,Vj) in a graph (G) must be either the direct distance between the two vertices (D[ij]) or the sum of two distances of a two-portion segment intermediated by a third vertex in the graph (Vk). Once a vertex with shortest distance to the source vertex Vi is determined, another vertex with sub-shortest distance to Vi can be determined accordingly. If this procedure goes on until the last vertex (also the vertex with the longest distance to Vi) in the graph is reached, the shortest path from the source vertex to all other vertices shall be generated.
# Representing the graph with adjacency list instead of adjacency matrix shall improves time complexity from V^2 to (V+E)logV.
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
from ALG019_priority_queue_nb import PriorityQueue
def traverse(v0):
    dist = {}
    count = 0
    heap = []
    pq = PriorityQueue()
    dist.setdefault((v0,v0),0)
    # Set initial distances from all the vertices to the source vertex to infinity and source vertex to itself as zero. Then, heapify the vertices and distances to make a priority queue.
    for vi in adj_list:
        dist.setdefault((v0,vi),inf)
        pq.sift_up_min(heap,(dist[(v0,vi)],vi))
    # Since there must be one vertex whose shortest distance from the source vertex can be determined in each iteration, and the final (also the furthest (with respect to weight)) vertex needs no further iteration, the number of necessary iterations is one less than the total number of vertices.
    while count < vertex_num:
        count += 1
        vu = pq.extract_min(heap)[0].key
        try:
            sentinel = 0
            for it in adj_list[vu].items():
                vk = it[0]
                wt = it[1]
                if dist[(v0,vk)] > dist[(v0,vu)] + wt:
                    dist[(v0,vk)] = dist[(v0,vu)] + wt
                    pq.sift_up_min(heap,(dist[(v0,vk)],vk))
                    sentinel = 1
            # Guarantee an early exit from the iteration if appropriate.
            if sentinel == 0:
                return dist
            # When the number of iterations is equal to or larger than the number of vertices, it indicates the presence of negatively weighted loops in the graph.
            elif count > vertex_num-1:
                return 'There is a negatively weighted loop in the graph!'
        except UnboundLocalError:
            return 'No shortest path from vertex %s to other vertices in the graph!'%v0
if __name__=='__main__':
    for al in [adj_list01,adj_list02,adj_list03,adj_list04]:
        adj_list = al
        v0 = tuple(list(adj_list)[0])[0]
        # vertex_num: number of vertices in the graph
        vertex_num = len(adj_list)
        print('*******************matrix************************')
        print(traverse(v0))