import networkx as nx


def dfs(graph, marked, viewed, vertices, n, vert, start, V):
    marked[vert] = True
    viewed.append(vert)
    if n == 0:
        marked[vert] = False
        if graph[vert][start] == 1:
            viewed.sort()
            print(viewed)
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
def count_f(g, v):
    graph = nx.to_numpy_matrix(g).tolist()
    marked = [False] * v
    viewed = []
    vertices = []
    count = 0
    for i in range(v - 6):
        dfs(graph, marked, viewed, vertices, 6, i, i, v)
        marked[i] = True

    vertices = list(set(vertices))
    print(vertices)
    for i in range(0, len(vertices)):
        dat = list(vertices[i])
        for node in dat:
            n = list(g.neighbors(node))
            if len(n) > 2:
                count += len(n) - 2

    del vertices
    del marked
    return int(count)


g = nx.Graph()
g.add_cycle([0, 1, 2, 3, 4, 5])
# g.add_nodes_from(range(0,5))
g.add_edge(0, 6)
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
print(count_f(g, 7))
#

