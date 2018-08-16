import networkx as nx
import matplotlib.pyplot as plt


def internal(graph, v):
    if sum(graph[v]) < 4:
        return 0
    cnt = 0
    for i, val in enumerate(graph[v]):
        if val == 1:
            for j, val2 in enumerate(graph[v]):
                if val2 == 1 and i != j:
                    for k, val3 in enumerate(graph[v]):
                        if val3 == 1 and k != i and k != j:
                            for n, val4 in enumerate(graph[v]):
                                if val4 == 1 and n != i and n != j and n != k:
                                    if graph[i][j] == 1 and graph[k][n] == 1:
                                        cnt += 1
    return cnt / 8


def count_h(graph, size):
    g = nx.to_numpy_matrix(graph).tolist()
    g = [[int(j) for j in i] for i in g]
    sums = 0
    for i in range(0, len(g)):
        sums += internal(g, i)
    return sums

# g = nx.Graph()
# g.add_edge(0,1)
# g.add_edge(1,3)
# g.add_edge(4,3)
# g.add_edge(3,0)
# g.add_edge(0,4)
# g.add_edge(0,5)
# g.add_edge(0,6)
# g.add_edge(4,6)
# g.add_edge(1,6)
# # g.add_edge(8,0)
#
#
# print(count_h(g, 8))
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
# print( count_h(g, 5))
#
# nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()
