import mathchem as mc
import networkx as nx
import matplotlib.pyplot as plt

h = nx.gnm_random_graph(200, 19000)
gmat = nx.to_numpy_matrix(h).tolist()
ch = mc.Mol()
ch.read_matrix(gmat)
print(ch.energy())
# The Following 3 Lines are for Printing of Graph
# nx.draw_networkx(h, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()