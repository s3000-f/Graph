import networkx as nx
import matplotlib.pyplot as plt


def dfs(graph, marked, viewed, vertices, n, vert, start, V):
    marked[vert] = True
    viewed.append(vert)
    if n == 0:
        marked[vert] = False
        if graph[vert][start] == 1:
            viewed.sort()
            vertices.append(tuple(viewed))
            viewed.remove(vert)
            return
        else:
            viewed.remove(vert)
            return

    for i in range(V):
        if marked[i] is False and graph[vert][i] == 1:
            dfs(graph, marked, viewed, vertices, n - 1, i, start, V)
    marked[vert] = False
    viewed.remove(vert)
    return


# graph: Adjacency Matrix of graph
# n: size of cycle
# V: size of graph
def count_d(graph, v):
    marked = [False] * v
    viewed = []
    vertices = []
    count = 0
    for i in range(v - 2):
        dfs(graph, marked, viewed, vertices, 2, i, i, v)
        marked[i] = True

    vertices = list(set(vertices))
    for i in range(0, len(vertices)):
        for j in range(0, len(vertices)):
            if len(set(vertices[i]) & set(vertices[j])) == 2:
                count += 1
    del vertices
    del marked
    return int(count / 2)


# g = nx.Graph()
# g.add_nodes_from(range(1,5))
# g.add_edge(1,2)
# g.add_edge(2,3)
# g.add_edge(3,1)
# g.add_edge(1,4)
# g.add_edge(4,3)
# g.add_edge(4,5)
# g.add_edge(3,5)
# print( count_d(nx.to_numpy_matrix(g).tolist(), 5))
#
# nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()
