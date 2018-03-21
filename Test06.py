import networkx as nx
import numpy as np
import read as rd
import star as st


raw = rd.read_samples()
graphs = []
for r in raw:
    m = np.matrix(r)
    g = nx.from_numpy_matrix(m)
    graphs.append(g)

cnt = 1
for r in graphs:
    f = open("OUT/S1_3/"+str(cnt)+".txt","w")
    f.write(str(st.count_star(r)))
    f.close()
    cnt += 1
