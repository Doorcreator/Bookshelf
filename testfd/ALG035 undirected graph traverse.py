# undirected graph (无向图)
'''
1--2
1--3
1--5
2--4
3--5
'''
# undirected graph represented by adjacency matrix (邻接矩阵)
# The first column (keys) in the matrix indicates vertices, and the symbols (0, 1, 'inf') indicate the relationships between the vertices (0: the vertex itself, 1: connected, 'inf': not connected).
# *****************************************************
matrix = {
'1':[0,1,1,'inf',1],
'2':[1,0,'inf',1,'inf'],
'3':[1,'inf',0,'inf',1],
'4':['inf',1,'inf',0,'inf'],
'5':[1,'inf',1,'inf',0]
}
# map the column numbers of the matrix to the vertices
clmn2v = {0:'1',1:'2',2:'3',3:'4',4:'5'}
# *****************************************************
# V01: DFS
from ALG024_stack import Stack
def traverse01(v):
    path = ''
    for j in range(0,clmn):
        nv = v
        # nu: vertex pointed to by vertex nv
        nu = clmn2v[j]
        flag.setdefault(nu,0)
        if flag[nu] == 1 or matrix[nv][j] == 0 or matrix[nv][j] == 'inf':
            continue
        else:
            flag[nu] = 1
            stc.push(nu)
            path = stc.stack
            traverse01(nu)
    return path
# V02: BFS
from ALG024_queue import Queue
def traverse02(v):
    while not que.is_empty():
        v = que.get()
        for j in range(clmn):
            nv = v
            nu = clmn2v[j]
            flag.setdefault(nu,0)
            if flag[nu] == 1 or matrix[nv][j] == 0 or matrix[nv][j] == 'inf':
                continue
            else:
                flag[nu] = 1
                que.enqueue(nu)
        dq = que.dequeue()
        path.append(dq)
    return path
if __name__=='__main__':
    # v0: initial vertex
    v0 = '1'
    row = len(matrix)
    clmn = len(matrix[v0])
    path = []
    stc = Stack([])
    stc.push(v0)
    flag = {}
    flag.setdefault(v0,1)
    results01 = traverse01(v0)
    print(results01)
    que = Queue([])
    que.enqueue(v0)
    flag = {}
    flag.setdefault(v0,1)
    results02 = traverse02(v0)
    print(results02)
# ==============================================================================
# undirected graph represented by adjacency adj_list (邻接表)
# The keys in the adj_list dict indicates vertices, the values of the dict indicate the vertices a vertex points to, and the relationships between the vertices are represented by presence or absence of values for relevant keys (i.e., A and B are connected when there is a value (vertex B) for a key (vertex A). Accordingly, there should be a value (vertex A) for a key (vertex B)). 
# *****************************************************
adj_list = {
'1':['2','3','5'],
'2':['1','4'],
'3':['1','5'],
'4':['2'],
'5':['1','3']
}
# *****************************************************
# V01: DFS
from ALG024_stack import Stack
def traverse01(v):
    path = ''
    for j in range(len(adj_list[v])):
        # u: vertex pointed to by vertex v
        u = adj_list[v][j]
        flag.setdefault(u,0)
        if flag[u] == 1:
            continue
        else:
            flag[u] = 1
            stc.push(u)
            path = stc.stack
            traverse01(u)
    return path
# V02: BFS
from ALG024_queue import Queue
def traverse02(v):
    while not que.is_empty():
        v = que.get()
        for j in range(len(adj_list[v])):
            nv = v
            nu = adj_list[v][j]
            flag.setdefault(nu,0)
            if flag[nu] == 1:
                continue
            else:
                flag[nu] = 1
                que.enqueue(nu)
        dq = que.dequeue()
        path.append(dq)
    return path
if __name__=='__main__':
    v0 = '1'
    stc = Stack([])
    stc.push(v0)
    flag = {}
    flag.setdefault(v0,1)
    results01 = traverse01(v0)
    print(results01)
    path = []
    que = Queue([])
    que.enqueue(v0)
    flag = {}
    flag.setdefault(v0,1)
    results02 = traverse02(v0)
    print(results02)