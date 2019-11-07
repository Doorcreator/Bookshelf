map = [
'#############',
'#GG.GGG#GGG.#',
'###.#G#G#G#G#',
'#.......#..G#',
'#G#.###.#G#G#',
'#GG.GGG.#.GG#',
'#G#.#G#.#.#.#',
'##G...G.....#',
'#G#.#G###.#G#',
'#...G#GGG.GG#',
'#G#.#G#G#.#G#',
'#GG.GGG#G.GG#',
'#############',
]
# V01: Probe the entire map and count the enemies at each point, update max_enm if the number of enemies at a point is larger than max_enm. But whether the point of max_enm is reachable is not confirmed.
def count_enm(arr,x0,y0):
    enm = 0
    x,y = x0,y0
    while arr[x][y] != '#':
        x -= 1
        if arr[x][y] == 'G':
            enm += 1
    x,y = x0,y0
    while arr[x][y] != '#':
        x += 1
        if arr[x][y] == 'G':
            enm += 1
    x,y = x0,y0
    while arr[x][y] != '#':
        y -= 1
        if arr[x][y] == 'G':
            enm += 1
    x,y = x0,y0
    while arr[x][y] != '#':
        y += 1
        if arr[x][y] == 'G':
            enm += 1
    return enm
def wipe_enm(arr):
    max_enm = 0
    for i in range(13):
        for j in range(13):
            if arr[i][j]=='.':
                total_enm = count_enm(arr,i,j)
                if total_enm > max_enm:
                    max_enm = total_enm
                    max_x,max_y = i,j
    return max_x,max_y,max_enm
print(wipe_enm(map))
# V02: Probe the entire map and count the enemies at each point, update max_enm if the number of enemies at a point is larger than max_enm and the point is reachable (as confirmed by BFS).
from ALG024_queue import Queue
row = len(map)
clmn = len(map[0])
def get_path(x0,y0,xw,yw):
    # (x0,y0): start point
    # (xw,yw): end point
    que = Queue([])
    que.enqueue((x0,y0))
    flag = {}
    flag.setdefault((x0,y0),1)
    inc = [(0,1),(1,0),(0,-1),(-1,0)]
    while not que.is_empty():
        x,y = que.get()
        for i in range(4):
            nx = x+inc[i][0]
            ny = y+inc[i][1]
            flag.setdefault((nx,ny),0)
            if nx < 0 or nx > row-1 or ny <0 or ny > clmn-1 or map[nx][ny] == '#' or map[nx][ny] == 'G' or flag[(nx,ny)] == 1:
                continue
            else:
                if (nx,ny) == (xw,yw):
                    return True
                if map[nx][ny] == '.':
                    flag[(nx,ny)] = 1
                    que.enqueue((nx,ny))
        que.dequeue()
def count_enm(arr,x0,y0):
    enm = 0
    inc = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(4):
        x,y = x0,y0
        x,y = (x+inc[i][0],y+inc[i][1])
        while arr[x][y] != '#':
            if arr[x][y] == 'G':
                enm += 1
                x,y = (x+inc[i][0],y+inc[i][1])
            elif arr[x][y] == '.':
                x,y = (x+inc[i][0],y+inc[i][1])
            else:
                break
    return enm
def wipe_enm(arr):
    max_enm = 0
    for i in range(row):
        for j in range(clmn):
            if arr[i][j]=='.':
                total_enm = count_enm(arr,i,j)
                if total_enm > max_enm and get_path(3,3,i,j) != None:
                    max_enm = total_enm
                    max_x,max_y = i,j
    return (max_x,max_y),max_enm
print(wipe_enm(map))
# V03: Probe the map using BFS and count the enemies killed at each point probed, update the max_enm if the number of enemies killed is larger than current max_enm.
from ALG024_queue import Queue
def wipe_enm(x0,y0):
    # (x0,y0): start point
    row = len(map)
    clmn = len(map[0])
    que = Queue([])
    que.enqueue((x0,y0))
    flag = {}
    flag.setdefault((x0,y0),1)
    enm = {}
    max_enm = 0
    enm[(x0,y0)] = count_enm(map,x0,y0)
    if enm[(x0,y0)] > max_enm:
        max_enm = enm[(x0,y0)]
    inc = [(0,1),(1,0),(0,-1),(-1,0)]
    while not que.is_empty():
        x,y = que.get()
        for i in range(4):
            nx = x+inc[i][0]
            ny = y+inc[i][1]
            flag.setdefault((nx,ny),0)
            if nx < 0 or nx > row-1 or ny < 0 or ny > clmn-1 \
            or map[nx][ny] == '#' or map[nx][ny] == 'G' or flag[(nx,ny)] == 1:
                continue
            else:
                if (nx,ny) == (row,clmn):
                    return True
                if map[nx][ny] == '.':
                    flag[(nx,ny)] = 1
                    enm[(nx,ny)] = count_enm(map,nx,ny)
                    if enm[(nx,ny)] > max_enm:
                        max_enm = enm[(nx,ny)]
                        max_i,max_j = nx,ny
                    que.enqueue((nx,ny))
        que.dequeue()
    return (max_i,max_j),max_enm
def count_enm(arr,x0,y0):
    enm = 0
    inc = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(4):
        x,y = x0,y0
        x,y = (x+inc[i][0],y+inc[i][1])
        while arr[x][y] != '#':
            if arr[x][y] == 'G':
                enm += 1
                x,y = (x+inc[i][0],y+inc[i][1])
            elif arr[x][y] == '.':
                x,y = (x+inc[i][0],y+inc[i][1])
            else:
                break
    return enm
print(wipe_enm(3,3))
# V04: DFS implementation
def wipe_enm(x,y):
    inc = [(0,1),(1,0),(0,-1),(-1,0)]
    global max_enm,max_i,max_j
    for i in range(4):
        nx = x+inc[i][0]
        ny = y+inc[i][1]
        flag.setdefault((nx,ny),0)
        if nx < 0 or nx > row-1 or ny <0 or ny > clmn-1 or map[nx][ny] == '#' or map[nx][ny] == 'G' or flag[(nx,ny)] == 1:
            continue
        else:
            enm[(nx,ny)] = count_enm(map,nx,ny)
            if enm[(nx,ny)] > max_enm:
                    max_enm = enm[(nx,ny)]
                    max_i,max_j = nx,ny
            if nx == 1 or nx == row-2 or ny == 1 or ny == clmn-2:
                return
            elif map[nx][ny] == '.':
                flag[(nx,ny)] = 1
                wipe_enm(nx,ny)
                flag[(nx,ny)] = 0
    return (max_i,max_j),max_enm
def count_enm(arr,x0,y0):
    enm = 0
    inc = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(4):
        x,y = x0,y0
        x,y = (x+inc[i][0],y+inc[i][1])
        while arr[x][y] != '#':
            if arr[x][y] == 'G':
                enm += 1
                x,y = (x+inc[i][0],y+inc[i][1])
            elif arr[x][y] == '.':
                x,y = (x+inc[i][0],y+inc[i][1])
            else:
                break
    return enm
if __name__=='__main__':
    row = len(map)
    clmn = len(map[0])
    x0,y0 = 3,3
    flag = {}
    flag.setdefault((x0,y0),1)
    enm = {}
    max_enm = 0
    max_i,max_j = x0,y0
    enm[(x0,y0)] = count_enm(map,x0,y0)
    if enm[(x0,y0)] > max_enm:
        max_enm = enm[(x0,y0)]
    print(wipe_enm(x0,y0))
# V05: calculate the total number of enemies killed along a path starting from a point in the map.
# First, generate all the paths possible using DFS. Then, add up the enemies killed along each path.
from ALG024_stack import Stack
def wipe_enm(x,y):
    inc = [(0,1),(1,0),(0,-1),(-1,0)]
    global path
    atmp[(x,y)] = 0
    for i in range(4):
        nx = x+inc[i][0]
        ny = y+inc[i][1]
        flag.setdefault((nx,ny),0)
        if nx < 1 or nx > row-2 or ny <1 or ny > clmn-2 or map[nx][ny] == '#' or map[nx][ny] == 'G' or flag[(nx,ny)] == 1:
            atmp[(x,y)]+=1
            if atmp[(x,y)] == 4:
                total_enm[path] = stc.stack
                path += 1
            continue
        else:
            flag[(nx,ny)] = 1
            stc.push((nx,ny))
            wipe_enm(nx,ny)
            stc.pop()
            flag[(nx,ny)] = 0
    return total_enm
def count_enm(arr,x0,y0):
    enm = 0
    inc = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(4):
        x,y = x0,y0
        x,y = (x+inc[i][0],y+inc[i][1])
        while arr[x][y] != '#':
            if arr[x][y] == 'G':
                enm += 1
                x,y = (x+inc[i][0],y+inc[i][1])
            elif arr[x][y] == '.':
                x,y = (x+inc[i][0],y+inc[i][1])
            else:
                break
    return enm
if __name__=='__main__':
    row = len(map)
    clmn = len(map[0])
    x0,y0 = 3,3
    flag = {}
    flag.setdefault((x0,y0),1)
    stc = Stack([])
    stc.push((x0,y0))
    max_enm = {}
    atmp = {}
    total_enm = {}
    path = 0
    te = wipe_enm(x0,y0)
    for i in range(len(te)):
        max_enm[i] = 0
        for e in te[i]:
            max_enm[i] += count_enm(map,e[0],e[1])
    pe = [(max_enm[i],te[i]) for i in range(len(te))]
    for p in pe:
        print('%s enemies can be killed along the path: %s'%(p[0],p[1]))
