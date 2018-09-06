import networkx as nx
import numpy as np
import f as f, d as d, star as s, Path as p, h as h, read as r, cycle as c
import dangle as dan
import matplotlib.pyplot as plt

name = [20, 24, 26, 28, 30, 32, 36, 50, 60, 76, 80]
c3 = []
c4 = []
c6 = []
c8 = []
ps = []
p3 = []
p4 = []
fs = []
hs = []
s13 = []
d4 = []

# for i in name:
# read = r.read_graph("fullerene/" + str(i) + ".txt")
# g = nx.from_numpy_matrix(np.matrix(read))
g = nx.Graph()
g.add_cycle([0, 1, 2])
g.add_edge(0, 3)
g.add_edge(1, 4)
i = 5
# nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()

# g.add_nodes_from(range(0, i))
gl = nx.to_numpy_matrix(g).tolist()
# nx.to_numpy_matrix(g).tolist()
# c3.append(dan.count_f(g, i))
# c4.append(c.count_cycles(gl, 6, i))
c3.append(c.count_cycles(gl, 3, i))
c4.append(c.count_cycles(gl, 4, i))
c6.append(c.count_cycles(gl, 6, i))
c8.append(c.count_cycles(gl, 8, i))
pss = p.path_count(g, 4)
ps.append(pss)
p3.append(pss[3])
p4.append(pss[4])
fs.append(f.count_f(g, len(gl)))
hs.append(h.count_h(gl, len(gl)))
s13.append(s.count_star(g))
d4.append(d.count_d(gl, len(gl)))

print(c3)
print(c4)
print(c6)
print(c8)
print(ps)
print(p4)
print(fs)
print(hs)
print(s13)
print(d4)

# nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()
# print(ps)
# break;
