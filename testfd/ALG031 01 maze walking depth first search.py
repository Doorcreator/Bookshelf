# maze-walking game
# Depth first search
import time
from ALG024_stack import Stack
# To define a maze.
maze = [
'..#.',
'....',
'..#.',
'.#T.',
'...#',
]
maze2 = [
'......#...........#.....',
'....#....#..............',
'..#..#.....#.....#......',
'....#..#.#........#.....',
'......#.#...............',
'...#...#.....#..........',
'......#.................',
'.......######.#....#....',
'.......#...T....#.......',
'.......#.......#........',
'..................#.....'
]
# A depth first search function to probe the maze until a walkable path is found.
def walk(x,y):
    # plan: store the number of walkable paths.
    global plan
    # inc: store the increment (or direction) per step.
    inc = [(0,1),(1,0),(-1,0),(0,-1)]
    # flag: store the availability status ('0': available, has not been probed; '1': unavailable, has already been probed;) of current (x,y) or next (nx,ny) step.
    flag.setdefault((x,y),1)
    for i in range(4):
        # (nx,ny): coordinate of next step.
        nx = x+inc[i][0]
        ny = y+inc[i][1]
        flag.setdefault((nx,ny),0)
        # To identify the walkable status of next step. If the next step has been out of the maze borders or blocked by a barrier ('#') or probed (flag == 1), then it is skipped.
        if nx < 0 or nx > row-1 or ny <0 or ny > clmn-1 or maze[nx][ny] == '#' or flag[(nx,ny)] == 1:
            continue
        else:
            # If next step is our target, this round of probing shall be ended and recorded.
            if maze[nx][ny] == 'T':
                stc.push((nx,ny))
                path.setdefault(plan,stc.stack)
                stc.pop()
                plan += 1
                return
            # If next step is walkable, the probing shall be repeated by taking the next step as current step.
            # Before probing, the next step should be marked as 'walked' (flag == 1) and pushed into the stack. After probing, the next step should be marked as 'walkable' (flag == 0) and popped out of the stack. This is critical for proper running of the recursion.
            if maze[nx][ny] == '.':
                flag[(nx,ny)] = 1
                stc.push((nx,ny))
                walk(nx,ny)
                stc.pop()
                flag[(nx,ny)] = 0
    # return all the possible strategies to walk to the target.
    return path
t0 = time.time()
if __name__=='__main__':
    # To define initial status of the maze and relevant variables.
    row = len(maze)
    clmn = len(maze[0])
    flag = {}
    path = {}
    # (x0,y0): the start point
    x0,y0 = (0,0)
    stc = Stack([])
    stc.push((x0,y0))
    plan = 0
    paths = walk(x0,y0)
    # sort the paths according the steps needed, and output them.
    sorted_paths = sorted(paths.items(),key = lambda item:len(item[1]))
    for p in sorted_paths:
        print(p)
    optimal_path = sorted_paths[0][1]
    print('There are %s paths to the target. The shortest path include %s steps %s'%(len(paths),len(optimal_path)-1,optimal_path))
t1 = time.time()
print('dfs:%s'%(t1-t0))

