import networkx as nx


# graph: NetworkX Graph
# max_len: maximum length of path
def path_count(graph, max_len):
    cnt = [0] * 10
    asd = []
    for src in graph.node():
        for dst in graph.node():
            for p in nx.all_simple_paths(graph, src, dst, max_len):
                shit = []
                for i in p:
                    if i not in shit:
                        shit.append(i)
                asd.append(shit)
                del shit
    # print(asd)
    # asd = list(set(asd))
    asd2 = []
    for p in asd:
            if p not in asd2:
                asd2.append(p)
    del asd
    for p in asd2:
        length = len(p)
        cnt[length] += 1
    for i in range(0, len(cnt)):
        cnt[i] = int(cnt[i] / 2)
    del asd2
    return cnt


# g = nx.Graph()
# g.add_path(range(0,m4))
# # asd = list(nx.all_simple_paths(g, 0, 3, 3))
# # print(asd)
#
#
# p = path_count(g, 3)
# print(p)