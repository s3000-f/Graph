import networkx as nx
from sympy.physics.quantum.circuitplot import np

def formatFixer(matfile):
    file_object = open("Test 4.txt","w")
    data=file_object.read()
    flag =0;
    for a in data:
        if(flag==0)
         if(a=="]")
             flag=1;
        if(flag==1)

def adjencyOf(graph):
    mat = np.matrix(0)
    mat = nx.to_numpy_matrix(graph).tolist()
    print(mat)
graph=nx.erdos_renyi_graph(150,0.5)
adjencyOf(graph)