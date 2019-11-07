# breadth first search
from ALG024_queue import Queue
from ALG032_dict_key_permutation import *
maze = [
'..#.',
'....',
'..#.',
'.#T.',
'...#',
]
def walk(x0,y0):
    row = len(maze)
    clmn = len(maze[0])
    flag = {}
    path = []
    # came_from: keep track of the coordinate of previous point.
    came_from = {}
    # que: keep track of all the points visited.
    que = Queue([])
    que.enqueue((x0,y0))
    inc = [(0,1),(1,0),(0,-1),(-1,0)]
    flag.setdefault((x0,y0),1)
    # step: keep track of the distance of next point from the start point.
    step = {}
    step.setdefault((x0,y0),0)
    while not que.is_empty():
        # If there are neighbour points not visited for the visited points in the queue, pop the most-recently visited point and check its neighbours as before.
        x,y = que.get()
        for i in range(4):
            nx = x+inc[i][0]
            ny = y+inc[i][1]
            flag.setdefault((nx,ny),0)
            if nx < 0 or nx > row-1 or ny <0 or ny > clmn-1 or maze[nx][ny] == '#' or flag[(nx,ny)] == 1:
                continue
            else:
                # Once the end point 'T' is reached, the probing shall be ended.
                if maze[nx][ny] == 'T':
                    que.enqueue((nx,ny))
                    step[(nx,ny)] = step[(x,y)] + 1
                    came_from[(nx,ny)] = (x,y)
                    path.append((nx,ny))
                    # Uncomment the following to return only one shortest path. Otherwise all possible shortest paths shall be returned if there were multiple ones.
                    # while (nx,ny) != (x0,y0):
                        # x,y = came_from[(nx,ny)]
                        # path.append((x,y))
                        # nx,ny = x,y
                    # path.reverse()
                    return step
                # End point not reached, keep on advancing.
                if maze[nx][ny] == '.':
                    flag[(nx,ny)] = 1
                    step[(nx,ny)] = step[(x,y)] + 1
                    came_from[(nx,ny)] = (x,y)
                    que.enqueue((nx,ny))
        # Once all the neighbours of a point have been visited, the point shall be popped out of the queue. 
        que.dequeue()
if __name__=='__main__':
    # (x0,y0): the start point
    (x0,y0) = (0,0)
    paths = is_path(walk(x0,y0))
    sorted_paths = sorted(paths.items(),key = lambda item:len(item[1]))
    for p in sorted_paths:
        print(p)
    optimal_path = sorted_paths[0][1]
    print('There are %s paths to the target. The shortest path include %s steps %s'%(len(paths),len(optimal_path)-1,optimal_path))

