# To color the land in map (which is represented by dots '.') with asterisks '*' using BFS.
from ALG024_queue import Queue
map = [
'...#####..',
'.#.#...#..',
'.#.#....#.',
'..###...##',
'######...#',
'#...#....#',
'#........#',
'##......##',
'###....#..',
'########.#',
]
def probe(x0,y0):
    color.setdefault((x0,y0),'*')
    flag = {}
    flag.setdefault((x0,y0),1)
    que = Queue([])
    que.enqueue((x0,y0))
    area = 1
    inc = [(0,1),(1,0),(0,-1),(-1,0)]
    while not que.is_empty():
        x,y = que.get()
        for i in range(4):
            nx,ny = x+inc[i][0],y+inc[i][1]
            flag.setdefault((nx,ny),0)
            if nx < 0 or nx > row-1 or ny < 0 or ny > clmn-1 \
            or map[nx][ny] == '#' or flag[(nx,ny)] == 1:
                continue
            else:
                flag[(nx,ny)] = 1
                area += 1
                color[(nx,ny)] = '*'
                que.enqueue((nx,ny))
        que.dequeue()
    return area,que.queue,color
if __name__=='__main__':
    row = len(map)
    clmn = len(map[0])
    new_map = []
    color = {}
    for i in range(row):
        for j in range(clmn):
            if map[i][j] != '#' and color.get((i,j),'#') != '*':
                clr = probe(i,j)[2]
    for i in range(row):
        for j in range(clmn):
            if (i,j) in clr:
                new_map.append('*')
            else: 
                new_map.append('#')
        new_map.append('\n')
    print(''.join(new_map))
