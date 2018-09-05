import networkx as nx
import matplotlib.pyplot as plt
import d as d, h as h, f as f, g18 as g18

g = nx.Graph()
g.add_cycle([0, 1, 2])
g.add_cycle([0, 3, 4])
g.add_edge(2, 4)
g.add_edge(1, 3)
# g.add_edge(5, 0)
# g.add_edge(2, 5)

print(h.count_h(g, 5))
print(d.count_d(g, 5))
print(f.count_f(g, 5))
print(g18.count_g18(g))

nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
plt.draw()
plt.show()