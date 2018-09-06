import networkx as nx
import matplotlib.pyplot as plt


g = nx.LCF_graph(20, [50], 400)

nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
plt.draw()
plt.show()