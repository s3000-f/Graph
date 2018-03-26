import networkx as nx
import numpy as np
from Subgraphs import read as rd
import energy as eg

# import Path as pt

raw = rd.read_samples()
graphs =[]
matrices = []
for r in raw:
    m = np.matrix(r)
    matrices.append(m)
    g = nx.from_numpy_matrix(m)
    graphs.append(g)
    print(eg.graph_energy(m))

# print(len(list(graphs[7].neighbors(list(graphs[7].nodes())[31]))))
# nx.draw_networkx(graphs[7], with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()

# cnt = 1
# for r in raw:
#     if cnt < 9:
#         cnt += 1
#         continue
#     f = open("OUT/C6/"+str(cnt)+".txt","w")
#     f.write(str(cy.count_cycles(r, 6, len(r))))
#     f.close()
#     cnt += 1
