'''
1--2
1--3
2--3
2--4
3--4
3--5
4--5
'''
adj_list = {
'1':['2','3'],
'2':['1','3','4'],
'3':['1','2','4','5'],
'4':['2','3','5'],
'5':['3','4']
}
# BFS
from ALG024_queue import Queue
def traverse02(v):
    came_from = {}
    step = 0
    path = []
    while not que.is_empty():
        v = que.get()
        for j in range(len(adj_list[v])):
            nv = v
            nu = adj_list[v][j]
            flag.setdefault(nu,0)
            if flag[nu] == 1:
                continue
            else:
                came_from[nu] = nv
                flag[nu] = 1
                que.enqueue(nu)
                if nu == ve:
                    path.append(nu)
                    while nu != v0:
                        nv = came_from[nu]
                        path.append(nv)
                        nu = nv
                        step += 1
                    path.reverse()
                    return path,step
        que.dequeue()
if __name__=='__main__':
    v0 = '1'
    ve = '5'
    que = Queue([])
    que.enqueue(v0)
    flag = {}
    flag.setdefault(v0,1)
    results02 = traverse02(v0)
    print(results02)