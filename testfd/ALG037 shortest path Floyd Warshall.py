# Floyd Warshall Algorithm
# To find all-pair shortest paths in a graph.
# To define the graph with matrix.
inf = float('inf')
matrix = {
'A':[0,1,12,inf,inf,inf],
'B':[inf,0,9,3,inf,inf],
'C':[inf,inf,0,inf,5,inf],
'D':[inf,inf,4,0,13,15],
'E':[inf,inf,inf,inf,0,4],
'F':[inf,inf,inf,inf,inf,0]
}
# V: number of vertices in the graph
V = len(matrix)
v2clmn = {}
clmn2v = {}
v2c = list(map(lambda k,v:(k,v),list(map(lambda j:j,list(matrix))),list(map(lambda i:i,range(V)))))
c2v = list(map(lambda k,v:(k,v),list(map(lambda i:i,range(V))),list(map(lambda j:j,list(matrix)))))
for d in v2c:
    v2clmn[d[0]] = d[1] 
for d in c2v:
    clmn2v[d[0]] = d[1] 
# *****************************************************
def traverse():
    for k in list(matrix):
        for i in range(row):
            for j in range(clmn):
                matrix[clmn2v[i]][j] = min(\
                matrix[clmn2v[i]][j],
                matrix[clmn2v[i]][v2clmn[k]] + matrix[k][j])
    return matrix
if __name__=='__main__':
    v0 = list(matrix)[0][0]
    row = len(matrix)
    clmn = len(matrix[v0])
    results = traverse()
    for r in results.items():
        print(r)