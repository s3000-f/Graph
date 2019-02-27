import networkx as nx
import matplotlib.pyplot as plt
from Subgraphs.Graphlets import *
import numpy as np
from executables import read
import run_me2 as rm

alldata = []
for i in range(0, 30):
    r = read.read_graph("graphlets/G" + str(i) + ".txt")
    g = nx.from_numpy_matrix(np.matrix(r))
    alldata.append(rm.remove_graphlets(g, 120))
    print(i)
print(alldata)

f = open('shit.txt', 'w')
f.write(str(alldata).replace(".0", "").replace("],", "\n")
        .replace("[", "").replace("]]", "").replace(" ", ""))
f.close()
# nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()
