import networkx as nx
import matplotlib.pyplot as plt


def internal(graph):
    siz = len(graph)
    cnt = 0
    for i in range(0, siz):
        for j in range(0, siz):
            for k in range(0, siz):
                for l in range(0, siz):
                    for m in range(0, siz):
                        if (i != j and i != k and i != l and i != m and j != k
                                and j != l and j != m and k != l and k != m and l != m):
                            if (graph[i][j] == 1 and graph[i][k] == 1 and graph[i][l] == 1 and
                                    graph[i][m] == 1 and graph[k][l] == 1 and graph[k][m] == 1
                                    and graph[l][m] == 1):
                                cnt += 1
    return cnt


def count_g23(graph):
    g = nx.to_numpy_matrix(graph).tolist()
    g = [[int(j) for j in i] for i in g]
    sums = internal(g)
    return sums / 6

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
