from functools import reduce
def gen_step_list(step_dict):
    path_dict = {}
    for i in range(len(set(step_dict.values()))):
        path_dict.setdefault(i,[])
        for item in step_dict.items():
            if item[1] == i:
                path_dict[i].append(item[0])
    path_list = [path for path in path_dict.values()]
    return path_list
def permut(step_seq):
    permut_path = reduce(lambda seq1,seq2: [str(x)+','+str(y) for x in seq1 for y in seq2],step_seq)
    return permut_path
dequot_arr = []
def dequote(arr):
    for ele in arr:
        if isinstance(ele,str):
            ele = list(eval(ele))
            dequote(ele)
        else:
            dequot_arr.append(ele)
    return dequot_arr
def is_path(step_dict):
    step_seq = gen_step_list(step_dict)
    permut_path = permut(step_seq)
    arr = dequote(permut_path)
    start = 0
    unit = len(step_seq)
    count = 0
    paths = {}
    n = 0
    while count <= len(permut_path):
        path = arr[start:start+unit]
        occur = 0
        for m in range(len(path)-1):
            if (path[m][0] == path[m+1][0] and path[m][1] == path[m+1][1]-1) \
            or (path[m][0] == path[m+1][0] and path[m][1] == path[m+1][1]+1) \
            or (path[m][1] == path[m+1][1] and path[m][0] == path[m+1][0]-1) \
            or (path[m][1] == path[m+1][1] and path[m][0] == path[m+1][0]+1) :
                occur += 1
        if occur == len(path)-1 and path not in [pv for pv in paths.values()] \
        and path[-1] == step_seq[-1][-1]:
            paths[n] = path
            n += 1
        start = start+unit
        count+=1
    return paths
# step_seq = [[(0,0)],[(0,1),(1,0)],[(1,1),(2,0)],[(2,1),(3,0)]]
# step_dict = {(0,0):0,(0,1):1,(1,0):1,(1,1):2,(2,0):2,(1,2):3,(2,1):3,(3,0):3,(1,3):4,(4,0):4,(2,3):5,(0,3):5,(4,1):5,(3,3):6,(4,2):6,(3,2):7}
# print(is_path(step_dict))
# print(gen_step_list(step_dict)[])




