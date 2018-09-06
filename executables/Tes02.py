import networkx as nx
import numpy as np
import time

V = 5
tm = time.time()

def DFS(graph, marked, n, vert, start, count):
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
        if marked[i] == False and graph[vert][i] == 1:
            # DFS for searching path by decreasing
            # length by 1

            count = DFS(graph, marked, n - 1, i, start, count)

    # marking vert as unvisited to make it
    # usable again.
    marked[vert] = False
    return count


# Counts cycles of length
# N in an undirected
# and connected graph.
def countCycles(graph, n):
    # all vertex are marked un-visited intially.
    marked = [False] * V

    # Searching for cycle by using v-n+1 vertices
    count = 0
    for i in range(V - (n - 1)):
        count = DFS(graph, marked, n - 1, i, i, count)

        # ith vertex is marked as visited and
        # will not be visited again.
        marked[i] = True

    return int(count / 2)


# main :
graph = [[0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0]]
h = nx.gnm_random_graph(200, 19000)
gmat = np.matrix(0)
gmat = nx.to_numpy_matrix(h).tolist()
V = len(h.node())
n = 6
asd = [12,34,32,1,3,4,23]
asd.pop(0)
# print(asd)
print("Total cycles of length ", n, " are ", countCycles(gmat, n))
tm = time.time() - tm
# tm /= 1000
tm /= 60
print(tm)