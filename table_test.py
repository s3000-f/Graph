import networkx as nx
from Subgraphs import f as f, star as s, Path as p, h as h, cycle as c

c3 = []
c4 = []
c6 = []
c8 = []
p3 = []
p4 = []
fs = []
hs = []
s13 = []
d4 = []

for i in range(3,11):
    g = nx.Graph()
    # g.add_nodes_from(range(0, i))
    g.add_cycle(range(0, i))
    gl = nx.to_numpy_matrix(g).tolist()
    c3.append(c.count_cycles(gl, 3, i))
    c4.append(c.count_cycles(gl, 4, i))
    c6.append(c.count_cycles(gl, 6, i))
    c8.append(c.count_cycles(gl, 8, i))
    ps = p.path_count(g, 3)
    p3.append(ps[3])
    p4.append(ps[4])
    fs.append(f.count_f(g, len(gl)))
    hs.append(h.count_h(gl, len(gl)))
    s13.append(s.count_star(g))
    d4.append(h.count_h(gl, len(gl)))


print(c3)
print(c4)
print(c6)
print(c8)
print(p3)
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