import networkx as nx
import numpy as np
import read as rd
# import cycle as cy
import Path as pt


raw = rd.read_samples()
graphs =[]
matrices = []
for r in raw:
    m = np.matrix(r)
    matrices.append(m)
    g = nx.from_numpy_matrix(m)
    graphs.append(g)
# cnt = 1
# for r in raw:
#     f = open("OUT/"+str(cnt)+"_C4.txt","w")
#     f.write(str(cy.count_cycles(r, 4, len(r))))
#     f.close()
#     cnt += 1
f = open("OUT/P3&P4/"+str(8)+".txt","w")
f.write(str(pt.path_count(graphs[7], 4)))
f.close()
# cnt = 1
# for g in graphs:
#     if cnt<=8:
#         cnt+=1
#         continue
#     f = open("OUT/P3&P4/"+str(cnt)+".txt","w")
#     f.write(str(pt.path_count(g, 4)))
#     f.close()
#     cnt += 1
#cnt = 1
#for r in raw:
#    f = open("OUT/C6/"+str(cnt)+".txt","w")
#    f.write(str(cy.count_cycles(r, 6, len(r))))
#    f.close()
#    cnt += 1

