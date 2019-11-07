# directed graph (有向图)
'''
1->2:2
1->5:10
2->3:3
2->5:7
3->1:4
3->4:4
4->5:5
5->3:3
'''
# directed graph represented by adjacency matrix (邻接矩阵)
# The first column (keys) in the matrix indicates vertices, and the symbols (0, w [1,2,3...n], 'inf') indicate the relationships between the vertices (0: the vertex itself, w: weight between two connected vertices, 'inf': not connected).
# *****************************************************
matrix = {
'1':[0,2,'inf','inf',10],
'2':['inf',0,3,'inf',7],
'3':[4,'inf',0,4,'inf'],
'4':['inf','inf','inf',0,5],
'5':['inf','inf',3,'inf',0]
}
# map the column numbers of the matrix to the vertices
clmn2v = {0:'1',1:'2',2:'3',3:'4',4:'5'}
v2clmn = {'1':0,'2':1,'3':2,'4':3,'5':4}
# *****************************************************
# V01: DFS
from ALG024_stack import Stack
def traverse01(v):
    
    global min_dist
    for j in range(clmn):
        nv = v
        # nu: vertex pointed to by vertex nv
        nu = clmn2v[j]
        flag.setdefault(nu,0)
        if flag[nu] == 1 or matrix[nv][j] == 0 or matrix[nv][j] == 'inf':
            continue
        else:
            if nu == ve:
                flag[nu] = 1
                stc.push(nu)
                dist = 0
                m = 0
                while m < stc.size()-1:
                    v1 = stc.stack[m]
                    v2 = stc.stack[m+1]
                    dist += matrix[v1][v2clmn[v2]]
                    m += 1
                if dist < min_dist:
                    min_dist = dist
                    path[tuple(stc.stack)] = min_dist
                    
                stc.pop()
                flag[nu] = 0
                return list(path.items())[-1]
            else:
                flag[nu] = 1
                stc.push(nu)
                traverse01(nu)
                stc.pop()
                flag[nu] = 0
# V02: BFS: <To be completed>
from ALG024_queue import Queue
def traverse02(v):
    flag = {}
    dist = 0
    global min_dist
    while not que.is_empty():
        v = que.get()
        for j in range(clmn):
            nv = v
            nu = clmn2v[j]
            flag.setdefault((nv,nu),0)
            if flag[(nv,nu)] == 1 or matrix[nv][j] == 0 or matrix[nv][j] == 'inf':
                continue
            else:
                dist += matrix[nv][j]
                flag[(nv,nu)] = 1
                que.enqueue(nu)
        dq = que.dequeue()
if __name__=='__main__':
    # v0: initial vertex
    v0 = '1'
    # ve: final vertex
    ve = '5'
    row = len(matrix)
    clmn = len(matrix[v0])
    min_dist = float('inf')
    path = {}
    stc = Stack([])
    stc.push(v0)
    flag = {}
    flag.setdefault(v0,1)
    results01 = traverse01(v0)
    print(results01)
    path = []
    que = Queue([])
    que.enqueue(v0)
    # results02 = traverse02(v0)
    # print(results02)
#================================================================================================
# directed graph represented by adjacency adj_list (邻接表)
# The keys in the adj_list dict indicates vertices, the values of the dict indicate the vertices a vertex points to and the corresponding weight, and the relationships between the vertices are represented by presence or absence of values for relevant keys (i.e., A points to B when there is a value (vertex B) for a key (vertex A).
# *****************************************************
adj_list = {
'1':{'2':2,'5':10},
'2':{'3':3,'5':7},
'3':{'1':4,'4':4},
'4':{'5':5},
'5':{'3':3}
}
# *****************************************************
# V01: DFS
from ALG024_stack import Stack
def traverse01(v):
    global min_dist
    for j in adj_list[v]:
        nv = v 
        # nu: vertex pointed to by vertex nv
        nu = j
        flag.setdefault(nu,0)
        if flag[nu] == 1:
            continue
        else:
            if nu == ve:
                flag[nu] = 1
                stc.push(nu)
                dist = 0
                m = 0
                while m < stc.size()-1:
                    v1 = stc.stack[m]
                    v2 = stc.stack[m+1]
                    dist += adj_list[v1][v2]
                    m += 1
                if dist < min_dist:
                    min_dist = dist
                    path[tuple(stc.stack)] = min_dist
                stc.pop()
                flag[nu] = 0
                return list(path.items())[-1]
            else:
                flag[nu] = 1
                stc.push(nu)
                traverse01(nu)
                stc.pop()
                flag[nu] = 0
# V02: BFS <To be completed>
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
    # v0: initial vertex
    v0 = '1'
    # ve: final vertex
    ve = '5'
    min_dist = float('inf')
    path = {}
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
    # results02 = traverse02(v0)
    # print(results02)
#*******************************************
# V03: DFS (early exit)
def traverse03(v):
    global min_dist,dist
    for j in adj_list[v]:
        nv = v 
        nu = j
        flag.setdefault(nu,0)
        if flag[nu] == 1:
            continue
        else:
            if nu == ve:
                return min_dist
            else:
                flag[nu] = 1
                dist += adj_list[nv][nu]
                traverse03(nu)
                if dist > min_dist:
                    return
                else:
                    min_dist = dist
                flag[nu] = 0
if __name__=='__main__':
    v0 = '1'
    ve = '5'
    min_dist = float('inf')
    dist = 0
    flag = {}
    flag.setdefault(v0,1)
    results03 = traverse03(v0)
    print(results03)