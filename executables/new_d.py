import networkx as nx
import matplotlib.pyplot as plt


def internal(graph, v):
    if sum(graph[v]) < 3:
        return 0
    cnt = 0
    for i, val in enumerate(graph[v]):
        if val == 1:
            for j, val2 in enumerate(graph[v]):
                if val2 == 1 and i != j:
                    for k, val3 in enumerate(graph[v]):
                        if val3 == 1 and k != i and k != j:
                            if graph[i][j] == 1 and graph[j][k] == 1:
                                cnt+=1
    return cnt / 2


def count_f(graph):
    sums = 0
    for i in range(0, len(graph)):
        sums += internal(graph, i)
    return sums / 2


g = nx.Graph()
g.add_cycle([0, 1, 2, 3])
g.add_edge(0, 4)
g.add_edge(1, 3)
g.add_edge(0, 2)
x = nx.to_numpy_matrix(g).tolist()
x = [[int(j) for j in i] for i in x]
print(count_f(x))
nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
plt.draw()
plt.show()