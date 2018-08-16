import networkx as nx
import numpy as np
from Subgraphs import f as f, d as d, star as s, Path as p, h as h, read as r, cycle as c, w as w

name = [80]
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
ws = [];

for i in name:
    read = r.read_graph("fullerene/"+str(i)+".txt")
    g = nx.from_numpy_matrix(np.matrix(read))
    # g.add_nodes_from(range(0, i))
    gl = read
    # nx.to_numpy_matrix(g).tolist()
    c3.append(c.count_cycles(gl, 3, i))
    c4.append(c.count_cycles(gl, 4, i))
    c6.append(c.count_cycles(gl, 6, i))
    print(c.count_cycles(gl, 5, i))
    c8.append(c.count_cycles(gl, 8, i))
    pss = p.path_count(g, 4)
    ps.append(pss)
    # p3.append(pss[3])
    # p4.append(pss[4])
    fs.append(f.count_f(g, len(gl)))
    hs.append(h.count_h(gl, len(gl)))
    s13.append(s.count_star(g))
    d4.append(d.count_d(gl, len(gl)))
    # print(w.count_w(gl, len(gl)))


print(c3)
print(c4)
print(c6)
print(c8)
print(ps)
# print(p3)
# print(p4)
print(fs)
print(hs)
print(s13)
print(d4)
# print(ws)








    # nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
    # plt.draw()
    # plt.show()
    # print(ps)
    # break;