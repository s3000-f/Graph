import networkx as nx


def dfs(g: nx.Graph, curr, parent, distance, lens, start, matris):
    ans = False
    if distance == lens:
        return False
    for node in g.neighbors(curr):
        matris[node][curr] += 1
        matris[curr][node] += 1
        ans2 = dfs(g, node, curr, distance + 1, lens, start, matris)
        if ans2:
            ans = ans2
        if distance == lens - 1 and node == start:
            s = 0
            for row in range(len(mat)):
                for col in range(len(mat[0])):
                    if matris[row][col] != 0:
                        s += 1
            if s / 2 >= len(g.edges):
                ans = True
        matris[node][curr] -= 1
        matris[curr][node] -= 1
    return ans


g = nx.Graph()







mlength = 8
g.add_edge(0, 1)







length = len(g.nodes)
mat = []
for i in range(0, length):
    mat.append([0] * length)
an = False
for n in g.nodes:
    an2 = dfs(g, n, -1, 0, mlength, n, mat)
    if an2:
        an = an2

print(an)
