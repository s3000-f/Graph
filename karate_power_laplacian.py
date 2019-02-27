import networkx as nx
import scipy as sc
import matplotlib.pyplot as plt
from Subgraphs import f as f, star as s, Path as p, h as h, cycle as c



g = nx.karate_club_graph()
print(len(g.edges))
print(len(g.nodes))
# f = open('karate.txt', 'w')
# f.write(str(nx.to_numpy_matrix(g).tolist()).replace(".0", "").replace("],", "\n")
#         .replace("[", "").replace("]]", "").replace(" ", ""))
# f.close()
#
# f = open('karate_laplacian.txt', 'w')
# f.write(str(nx.laplacian_matrix(g).todense().tolist()).replace(".0", "").replace("],", "\n")
#         .replace("[", "").replace("]]", "").replace(" ", ""))
# f.close()


g = nx.Graph()
g.add_cycle(range(0, 18))
g.add_edge(2, 4)
g.add_edge(5, 7)
g.add_edge(9, 11)
g.add_edge(13, 15)
g.add_edge(16, 0)
g.add_edge(16, 4)
g.add_edge(15, 19)
g.add_edge(19, 5)
g.add_edge(10, 19)
g.add_edge(17, 20)
g.add_edge(3, 21)
print(len(g.edges))
print(len(g.nodes))
# f = open('power.txt', 'w')
# f.write(str(nx.to_numpy_matrix(g).tolist()).replace(".0", "").replace("],", "\n")
#         .replace("[", "").replace("]]", "").replace(" ", ""))
# f.close()

# f = open('power_laplatian.txt', 'w')
# f.write(str(nx.laplacian_matrix(g).todense().tolist()).replace(".0", "").replace("],", "\n")
#         .replace("[", "").replace("]]", "").replace(" ", ""))
# f.close()