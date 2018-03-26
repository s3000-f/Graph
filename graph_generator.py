import networkx as nx
# import matplotlib.pyplot as plt


def deterministic_sierpinski(g: nx.Graph, remaining: int, n1: int, n2: int, n3: int, last: int):
    g_in = nx.Graph(g)
    shit = False
    if remaining == 0:
        if n1 == -1:
            g_in.add_cycle([0, 1, 2])
            return g_in
        g_in.add_cycle([last + 1, last + 2, last + 3])
        g_in.add_edge(n1, last + 1)
        g_in.add_edge(n2, last + 1)
        g_in.add_edge(n1, last + 2)
        g_in.add_edge(n3, last + 2)
        g_in.add_edge(n2, last + 3)
        g_in.add_edge(n3, last + 3)
        return g_in
    elif n1 == -1:
        g_in.add_cycle([0, 1, 2])
        n1 = 0
        n2 = 1
        n3 = 2
        last = 2
        shit = True
    else:
        g_in.add_cycle([last + 1, last + 2, last + 3])
        g_in.add_edge(n1, last + 1)
        g_in.add_edge(n2, last + 1)
        g_in.add_edge(n1, last + 2)
        g_in.add_edge(n3, last + 2)
        g_in.add_edge(n2, last + 3)
        g_in.add_edge(n3, last + 3)

    if shit:
        shit = False
        g_in = deterministic_sierpinski(g_in, remaining-1, n1, n2, n3, last)
    else:
        g_in = deterministic_sierpinski(g_in, remaining - 1, last + 1, last + 2, n1, last + 3)
        last += 3
        g_in = deterministic_sierpinski(g_in, remaining - 1, last + 1, n1, n2, last + 3)
        last += 3
        g_in = deterministic_sierpinski(g_in, remaining - 1, last + 1, last + 3, n2, last + 3)
        last += 3
        g_in = deterministic_sierpinski(g_in, remaining - 1, last + 3, n2, n3, last + 3)
        last += 3
        g_in = deterministic_sierpinski(g_in, remaining - 1, last + 3, last + 2, n3, last + 3)
        last += 3
        g_in = deterministic_sierpinski(g_in, remaining - 1, last + 2, n3, n1, last + 3)
        last += 3
    return g_in


def deterministic_apollonian(g: nx.Graph, remaining: int, n1: int, n2: int, n3: int, last: int):
    g_in = nx.Graph(g)
    flag = False
    if remaining == 0:
        if n1 == -1:
            g_in.add_cycle([0, 1, 2])
            return g_in
        g_in.add_edge(n1, last + 1)
        g_in.add_edge(n2, last + 1)
        g_in.add_edge(n3, last + 1)
        return g_in
    elif n1 == -1:
        g_in.add_cycle([0, 1, 2])
        n1 = 0
        n2 = 1
        n3 = 2
        last = 2
        flag = True
    else:
        g_in.add_edge(n1, last + 1)
        g_in.add_edge(n2, last + 1)
        g_in.add_edge(n3, last + 1)
    
    if flag:
        flag = False
        g_in = deterministic_apollonian(g_in, remaining - 1, n1, n2, n3, last)
    else:
        g_in = deterministic_apollonian(g_in, remaining - 1, last + 1, n1, n2, last + 1)
        last += 1
        g_in = deterministic_apollonian(g_in, remaining - 1, last + 1, n2, n3, last + 1)
        last += 1
        g_in = deterministic_apollonian(g_in, remaining - 1, last + 1, n3, n1, last + 1)
        last += 1
    return g_in

# def sierpinski_style2(g: nx.Graph)
#
# gr = deterministic_apollonian(nx.Graph(), 10, -1, -1, -1, 0)
# print(gr.nodes)
# print(gr.edges)
#
# nx.draw_networkx(gr, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()