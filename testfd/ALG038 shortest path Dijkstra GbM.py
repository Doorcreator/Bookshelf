# Dijkstra algorithm with the graph represented by adjacency matrix
# To define the graph
# **********************************************************************
inf = float('inf')
# graph without loops or multiple ingoing/outgoing edges
matrix01 = {
'A':[0,-3,inf,inf,inf],
'B':[inf,0,2,inf,inf],
'C':[inf,inf,0,3,inf],
'D':[inf,inf,inf,0,2],
'E':[inf,inf,inf,inf,0]
}
# graph without loops
matrix02 = {
'A':[0,-3,inf,inf,5],
'B':[inf,0,2,inf,5],
'C':[inf,inf,0,3,inf],
'D':[inf,inf,inf,0,2],
'E':[inf,inf,inf,inf,0]
}
# graph without negatively-weighted loops
matrix03 = {
'A':[0,-3,inf,inf,5],
'B':[inf,0,2,4,5],
'C':[inf,inf,0,3,inf],
'D':[inf,inf,inf,0,2],
'E':[inf,inf,1,inf,0]
}
# graph with negatively-weighted loops
matrix04 = {
'A':[0,-3,inf,inf,5],
'B':[inf,0,2,-4,5],
'C':[inf,inf,0,3,inf],
'D':[inf,inf,inf,0,2],
'E':[inf,inf,-10,inf,0]
}
# **********************************************************************
# V01: mark the visited vertices with dict [flag].
# Time complexity: O(V^2)
def traverse01(v0):
    dist = {}
    flag = {}
    flag.setdefault(v0,1)
    for j in range(vertex_num):
        vj = clmn2v[j]
        flag.setdefault(vj,0)
        dist.setdefault((v0,vj),matrix[v0][j])
        if flag[vj] != 1:
            vu = vj
            flag[vu] = 1
            for k in range(vertex_num):
                vk = clmn2v[k]
                dist.setdefault((v0,vk),matrix[v0][k])
                if dist[(v0,vk)] > dist[(v0,vu)] + matrix[vu][k]:
                    dist[(v0,vk)] = dist[(v0,vu)] + matrix[vu][k]
    return dist
# V02: mark the visited vertices with set [Q].
# Time complexity: O(VE)
def traverse02(v0):
    dist = {}
    # set of unvisited vertices
    Q = set()
    dist.setdefault((v0,v0),0)
    for x in range(vertex_num):
        vx = clmn2v[x]
        dist.setdefault((v0,vx),matrix[v0][x])
        # add all unvisited vertices into set Q
        if vx != v0:
            Q.add(vx)
    for vi in list(Q):
        min_dist = inf
        for vj in Q:
            j = v2clmn[vj]
            if dist[(v0,vj)] < min_dist:
                min_dist = dist[(v0,vj)]
                vu = vj
        Q.discard(vu)
        for vk in Q:
            k = v2clmn[vk]
            if dist[(v0,vk)] > dist[(v0,vu)] + matrix[vu][k]:
                dist[(v0,vk)] = dist[(v0,vu)] + matrix[vu][k]
    return dist
# V03: mark the visited vertices with queue [que].
from ALG024_queue import Queue
def traverse03(v0):
    dist = {}
    que = Queue([])
    que.enqueue(v0)
    count = 0
    while not que.is_empty():
        v = que.get()
        count += 1
        sentinel = 0
        min_dist = inf
        for i in range(vertex_num):
            vi = clmn2v[i]
            dist.setdefault((v0,vi),matrix[v0][i])
            if matrix[v][i] != inf and matrix[v][i] != 0 and matrix[v][i] < min_dist:
                min_dist = matrix[v][i]
                vu = vi
        try:
            for k in range(vertex_num):
                vk = clmn2v[k]
                if dist[(v0,vk)] > dist[(v0,vu)] + matrix[vu][k]:
                    dist[(v0,vk)] = dist[(v0,vu)] + matrix[vu][k]
                    sentinel = 1
                    que.enqueue(vu)
        except UnboundLocalError:
            return 'No shortest path from vertex %s to other vertices in the graph!'%v0
        if count > vertex_num-1 and sentinel == 1:
            return 'There is a negatively-weighted loop in the graph!'
        que.dequeue()
    return dist
# V04: implementation with priority queue.
from ALG019_priority_queue_nb import PriorityQueue
def traverse04(v0):
    dist = {}
    heap = []
    pq = PriorityQueue()
    for i in range(vertex_num):
        vi = clmn2v[i]
        dist.setdefault((v0,vi),matrix[v0][i])
        if vi != v0:
            # heapify unvisited vertices
            pq.sift_up_min(heap,(dist[(v0,vi)],vi))
    while len(heap) >0:
        # pop the vertex with the shortest distance (i.e., vu) to the source vertex out of the pq
        vu = pq.extract_min(heap)[0].key
        try:
            # update the distance from the source vertex to the unvisited vertices (i.e., the vertices in the heap) using the above vertex vu as an intermediate vertex.
            for v in heap:
                vk = v.key
                k = v2clmn[vk]
                if dist[(v0,vk)] > dist[(v0,vu)] + matrix[vu][k]:
                    dist[(v0,vk)] = dist[(v0,vu)] + matrix[vu][k]
                    index = pq.get_key_index(heap,vk)
                    if index != None:
                        pq.remove(heap,index)
                        pq.sift_up_min(heap,(dist[(v0,vk)],vk))
                    else:
                        pq.sift_up_min(heap,(dist[(v0,vk)],vk))
        except UnboundLocalError:
            return 'No shortest path from vertex %s to other vertices in the graph!'%v0
    return dist
# ****************************************************************
# V05: optimized V02
def traverse05(v0):
    dist = {}
    # set of unvisited vertices
    Q = set()
    dist.setdefault((v0,v0),0)
    for x in range(vertex_num):
        vx = clmn2v[x]
        dist.setdefault((v0,vx),matrix[v0][x])
        # add all unvisited vertices into set Q
        if vx != v0:
            Q.add(vx)
    for vi in list(Q):
        min_dist = inf
        for vj in Q:
            j = v2clmn[vj]
            if dist[(v0,vj)] < min_dist:
                min_dist = dist[(v0,vj)]
                vu = vj
        for k in range(vertex_num):
            vk = clmn2v[k]
            if dist[(v0,vk)] > dist[(v0,vu)] + matrix[vu][k]:
                dist[(v0,vk)] = dist[(v0,vu)] + matrix[vu][k]
        Q.discard(vu)
    return dist
# V06: optimized V04
from ALG019_priority_queue_nb import PriorityQueue
def traverse06(v0):
    dist = {}
    count = 0
    heap = []
    pq = PriorityQueue()
    for i in range(vertex_num):
        vi = clmn2v[i]
        dist.setdefault((v0,vi),matrix[v0][i])
        if vi != v0:
            # heapify unvisited vertices
            pq.sift_up_min(heap,(dist[(v0,vi)],vi))
    while count < vertex_num:
        count += 1
        # pop the vertex with the shortest distance (i.e., vu) to the source vertex out of the pq
        vu = pq.extract_min(heap)[0].key
        try:
            # update the distance from the source vertex to the unvisited vertices (i.e., the vertices in the heap) using the above vertex vu as an intermediate vertex.
            sentinel = 0
            for k in range(vertex_num):
                vk = clmn2v[k]
                if dist[(v0,vk)] > dist[(v0,vu)] + matrix[vu][k]:
                    dist[(v0,vk)] = dist[(v0,vu)] + matrix[vu][k]
                    pq.sift_up_min(heap,(dist[(v0,vk)],vk))
                    sentinel = 1
            if count > vertex_num-1 and sentinel == 1:
                return 'There is a negatively-weighted loop in the graph!'
        except UnboundLocalError:
            return 'No shortest path from vertex %s to other vertices in the graph!'%v0
    return dist
if __name__=='__main__':
    for m in [matrix01,matrix02,matrix03,matrix04]:
        matrix = m
        V = len(matrix)
        v2clmn = {}
        clmn2v = {}
        v2c = list(map(lambda k,v:(k,v),list(map(lambda j:j,list(matrix))),list(map(lambda i:i,range(V)))))
        c2v = list(map(lambda k,v:(k,v),list(map(lambda i:i,range(V))),list(map(lambda j:j,list(matrix)))))
        for d in v2c:
            v2clmn[d[0]] = d[1] 
        for d in c2v:
            clmn2v[d[0]] = d[1]
        v0 = list(matrix)[0][0]
        # vertex_num: number of vertices in the graph
        vertex_num = len(matrix)
        print('*******************matrix************************')
        for f in [traverse01,traverse02,traverse03,traverse04,traverse05,traverse06]:
            print('%s:%s'%(f,f(v0)))