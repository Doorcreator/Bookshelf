from ALG024_stack import Stack
map = [
[5,3,5,3],
[1,5,3,0],
[2,3,5,1],
[6,1,1,5],
[1,5,5,4]
]

class Pipe():
    def __init__(self,tp,inlet):
    # To define a pipe class representing the 6 types of pipes, each of which has its own orientations of inlet and outlet. 
        # tp: type of pipes
        self.tp = tp
        self.inlet = inlet
        dic = {(1,'U'):'R',(1,'R'):'U',(2,'R'):'D',(2,'D'):'R',(3,'L'):'D',(3,'D'):'L',
        (4,'L'):'U',(4,'U'):'L',(5,'L'):'R',(5,'R'):'L',(6,'U'):'D',(6,'D'):'U'}
        # The outlet of a pipe is determined by its tp and inlet properties. Once the latter two are given, the former one shall be definite by referring to the dict above.
        self.outlet = dic[(self.tp,self.inlet)]
def lay_pipe(x,y):
    # To connect the pipes using DFS.
    inc = ['L','R','U','D']
    drct = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
    out2inlet = {'L':'R','R':'L','U':'D','D':'U'}
    in2outlet = {'L':('U','D'),'R':('U','D'),'U':('L','R'),'D':('L','R')}
    inout2tp = {('U','R'):1,('R','U'):1,('R','D'):2,('D','R'):2,('L','D'):3,('D','L'):3,
    ('L','U'):4,('U','L'):4,('L','R'):5,('R','L'):5,('U','D'):6,('D','U'):6}
    for i in range(4):
        if p[(x,y)].outlet == inc[i]:
            # This is the most subtle part of the algorithm. The next pipe to be connected shall be determined not only by its predecessor's coordinate but also by its predecessor's outlet. That's where the arguments [inc] and [drct] come in and play. 
            nx,ny = x+drct[inc[i]][0],y+drct[inc[i]][1]
            flag.setdefault((nx,ny),0)
            if nx < 0 or nx > row-1 or ny < 0 or ny > clmn-1 \
            or map[nx][ny] == 0 or flag[(nx,ny)] == 1:
                continue
            else:
                # The inlet of next pipe is determined by its predecessor's outlet.
                inlet = out2inlet[p[(x,y)].outlet]
                tp = map[nx][ny]
                if tp <= 4:
                    for j in range(2):
                        # The outlet of next pipe is determined by its type (smaller than or equal to 4) and inlet.
                        outlet = in2outlet[inlet][j]
                        # The possible types of next pipe are determined by its type, inlet, and outlet.
                        ntp = inout2tp[(inlet,outlet)]
                        # Now all are ready, let's lay the pipe.
                        p[(nx,ny)] = Pipe(ntp,inlet)
                        flag[(nx,ny)] = 1
                        stc.push({(nx,ny):ntp})
                        lay_pipe(nx,ny)
                        stc.pop()
                        flag[(nx,ny)] = 0
                else:
                # process cases when tp > 4.
                    outlet = p[(x,y)].outlet
                    ntp = inout2tp[(inlet,outlet)]
                    p[(nx,ny)] = Pipe(ntp,inlet)
                    flag[(nx,ny)] = 1
                    stc.push({(nx,ny):ntp})
                    lay_pipe(nx,ny)
                    stc.pop()
                    flag[(nx,ny)] = 0
                # To check whether the final pipe can be properly laid.
                if (nx,ny) == (xe,ye) and p[(nx,ny)].outlet == 'R':
                    stc.push({(nx,ny):ntp})
                    path.append(stc.stack)
    return path
if __name__=='__main__':
    # start point
    x0,y0 = 0,0
    # end point
    xe,ye = 4,3
    row = len(map)
    clmn = len(map[0])
    flag = {}
    flag.setdefault((x0,y0),1)
    p = {}
    p[(x0,y0)] = Pipe(5,'L')
    stc = Stack([])
    stc.push({(x0,y0):5})
    path = []
    pipeline = lay_pipe(x0,y0)  
    print(pipeline)