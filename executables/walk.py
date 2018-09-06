import networkx as nx


def dfs(graph: nx.Graph, marked, n, vert, ew, start, count, V):
    # mark the vertex vert as visited
    marked[ew] += 1

    # if the path of length (n-1) is found
    if n == 0:

        # mark vert as un-visited to make
        # it usable again.
        marked[ew] -= 1

        # Check if vertex vert can end with
        # vertex start
        if start in graph[vert] == 1:
            count = count + 1
            return count
        else:
            return count

    # For searching every possible path of
    # length (n-1)
    for i in range(V):
        if i in graph[vert]:
            # DFS for searching path by decreasing
            # length by 1

            count = dfs(graph, marked, n - 1, i, graph[vert][i]['w'], start, count, V)

    # marking vert as unvisited to make it
    # usable again.
    marked[vert] -= 1
    return count


# Counts cycles of length
# N in an undirected
# and connected graph.
# graph: Adjacency Matrix of graph
# n: size of cycle
# V: size of graph
def count_cycles(graph: nx.Graph, n, v):
    # all vertex are marked un-visited intially.
    marked = [0] * v
    # Searching for cycle by using v-n+1 vertices
    count = 0
    for i in range(v):
        count = dfs(graph, marked, n - 1, i, 0, i, count, v)
        # ith vertex is marked as visited and
        # will not be visited again.
        marked[i] += 1
    del marked
    return int(count / 2)


g = nx.Graph()
g.add_edge(0, 1, w=0)
c = count_cycles(g, 8, 2)
print(c)
