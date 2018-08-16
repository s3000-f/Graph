import networkx as nx


def count_w(graph, node_count):
    adj = nx.to_numpy_matrix(graph).tolist()
    adj = [[int(j) for j in i] for i in adj]
    ygreg = 0
    for headLeft in range(0, node_count):
        for headRight in range(0, node_count):
            for midUp in range(0, node_count):
                for midmid in range(0, node_count):
                    for midLow in range(0, node_count):
                        if headLeft == headRight or headLeft == midUp or headLeft == midmid or headLeft == midLow or headRight == midUp or headRight == midmid or headRight == midLow:
                            continue
                        if midUp == midmid or midUp == midLow or midLow == midmid:
                            continue
                        if adj[headRight][midUp] and adj[headLeft][midUp] and adj[midUp][midmid] and adj[midmid][
                            midLow]:
                            ygreg += 1
    return ygreg / 2
