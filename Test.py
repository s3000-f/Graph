import networkx as nx
import matplotlib.pyplot as plt
import itertools
import numpy as np


# equivalent of static variable
def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


# arguments are as follows
# gr: simple graph
# cnt: cycle length
# curr: Current node
# first: first(starting) node of cycle
# tmps: temp array for visited nodes

@static_vars(counter=0)
def cCount(gr: nx.Graph, cnt, curr, first, tmps, nOe, eID):
    # print("called with:", cnt, curr, first, tmps, nOe, eID)
    if cnt == 0:
        if first == curr and sum(tmps) >= gr.number_of_edges() and 0 not in tmps:
            for i in range(0, nOe):
                tmps[i] = 0
            cCount.counter += 1
        # print("---------------------: ", cCount.counter)
        return
    tmps[eID] += 1
    for n in gr.neighbors(curr):
        w = gr[curr][n]['w']
        shit = tmps[w]
        if cnt > 0:
            cCount(gr, cnt - 1, n, first, tmps, nOe, w)
        if tmps[w] > shit:
            tmps[w] -= 1


#

g = nx.Graph()
g.add_cycle([0, 1, 2])
g.add_edge(0, 5)
g.add_edge(2, 3)
# g.add_edge(2, 3)
# g.add_edge(4, 3)
# g.add_edge(5, 3)
# g.add_edge(6, 5)
cnt = 0
for (u, v) in g.edges:
    g.add_edge(u, v, w=cnt)
    cnt += 1

    # cCount(h, 4, nod, nod, tmp)
# print(cCount.counter)
cCount(g, 8, 0, 0, [0] * 6, 6, 0)
print(cCount.counter)
# The Following 3 Lines are for Printing of Graph
# nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()

# g = nx.Graph()
# g.add_node("a")
# g.add_nodes_from(range(1, 20))
#
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3, 7)
# g.add_edge(7, 8)
# g.add_edge(8, 1)
#
# g.add_edge(4, 5)
# g.add_edge(5, 6)
# g.add_edge(6, 4)
#
#
# # g.add_edge(5, 6)
# # g.add_path([4, 7, 8, 9])
# # g.add_nodes_from(range(30, 50))
# #
# # g.add_weighted_edges_from([(30, 31, 15), (32, 33, 23)])
#
# # g.add_cycle(range(34, 48))
# nx.draw_networkx(g, whith_labels=True, node_size=1)
# print(list(nx.find_cycle(g, orientation='ignore')))
# print(list(nx.find_cycle(g, orientation='ignore')))
#
# plt.draw()
# plt.show()
# ----------------------------------------------------------------
# for n in h:
#     print(n)
# print("hello")
# c = list(nx.simple_cycles(h.to_directed()))
# print(c.__len__())
# d = []
# for a in c:
#     d.append(list(a).sort())
# d.sort()
# d = list(d for d,_ in itertools.groupby(d))
# # print(c)
# mat = [tuple(t) for t in c]
# st = set(mat)
# for s in d:
#     if len(s) == 3:
#         print(s)
#
# # eq(c)
# print(d.__len__())
# print("hi")
# # for i in range(1, 10):
# #     for a in c:
# #         if list(a).__len__() == i:
# #             print(a)
#
# # for v in nx.nodes(h):
# #     print("%s %d %f"%(v,nx.degree(h,v),nx.clustering(h,v)))
#
#
