
def dfs(graph, marked, n, vert, start, count, V):
    # mark the vertex vert as visited
    marked[vert] = True

    # if the path of length (n-1) is found
    if n == 0:

        # mark vert as un-visited to make
        # it usable again.
        marked[vert] = False

        # Check if vertex vert can end with
        # vertex start
        if graph[vert][start] == 1:
            count = count + 1
            return count
        else:
            return count

    # For searching every possible path of
    # length (n-1)
    for i in range(V):
        if marked[i] is False and graph[vert][i] == 1:
            # DFS for searching path by decreasing
            # length by 1

            count = dfs(graph, marked, n - 1, i, start, count, V)

    # marking vert as unvisited to make it
    # usable again.
    marked[vert] = False
    return count


# Counts cycles of length
# N in an undirected
# and connected graph.
# graph: Adjacency Matrix of graph
# n: size of cycle
# V: size of graph
def count_cycles(graph, n, v):
    # all vertex are marked un-visited intially.
    marked = [False] * v
    # Searching for cycle by using v-n+1 vertices
    count = 0
    for i in range(v - (n - 1)):
        count = dfs(graph, marked, n - 1, i, i, count, v)
        # ith vertex is marked as visited and
        # will not be visited again.
        marked[i] = True
    del marked
    return int(count / 2)
