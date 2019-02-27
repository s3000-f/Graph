import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def internal(graph):
    siz = len(graph)
    cnt = 0
    deletions = set()
    for i in range(0, siz):
        for j in range(0, siz):
            for k in range(0, siz):
                for l in range(0, siz):
                    if (i != j and i != k and i != l and j != k
                            and j != l and k != l):
                        if graph[i][j] == 1 and graph[j][k] == 1 and graph[l][k] == 1:
                            cnt += 1
                            deletions.add((i, j))
                            deletions.add((j, i))
                            deletions.add((l, k))
                            deletions.add((k, l))
                            deletions.add((k, j))
                            deletions.add((j, k))
    return cnt, deletions


def count_g3(graph):
    in_g = nx.to_numpy_matrix(graph).tolist()
    in_g = [[int(j) for j in i] for i in in_g]
    sums, deletions = internal(in_g)
    for (i, j) in deletions:
        in_g[i][j] = 0
    in_g = np.matrix(in_g)
    in_g = nx.from_numpy_matrix(in_g)
    return sums / 2, in_g

# g = nx.Graph()
# g.add_nodes_from(range(0,5))
# g.add_edge(0,1)
# g.add_edge(1,2)
# g.add_edge(2,3)
# g.add_edge(3,0)
# g.add_edge(0,4)
# g.add_edge(0,5)
# g.add_edge(0,6)
# g.add_edge(7,6)
# g.add_edge(1,7)
# # g.add_edge(8,0)
#
#
# print(count_f(g, 8))
#
# nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()


# g = nx.Graph()
# g.add_nodes_from(range(1,5))
# g.add_edge(1,2)
# g.add_edge(2,3)
# g.add_edge(3,1)
# g.add_edge(1,4)
# g.add_edge(4,3)
# g.add_edge(4,5)
# g.add_edge(3,5)
# print( count_f(g, 5))
#
# nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()
