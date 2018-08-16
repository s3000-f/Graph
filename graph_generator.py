import networkx as nx
import matplotlib.pyplot as plt


def deterministic_sierpinski(g: nx.Graph, remaining: int, n1: int, n2: int, n3: int, last: list):
    g_in = nx.Graph(g)
    shit = False
    if remaining == 0:
        if n1 == -1:
            g_in.add_cycle([0, 1, 2])
            return g_in
        n = last[0]
        g_in.add_cycle([n + 1, n + 2, n + 3])
        g_in.add_edge(n1, last[0] + 1)
        g_in.add_edge(n2, last[0] + 1)
        g_in.add_edge(n1, last[0] + 2)
        g_in.add_edge(n3, last[0] + 2)
        g_in.add_edge(n2, last[0] + 3)
        g_in.add_edge(n3, last[0] + 3)
        return g_in
    elif n1 == -1:
        g_in.add_cycle([0, 1, 2])
        n1 = 0
        n2 = 1
        n3 = 2
        last[0] = 2
        shit = True
    else:
        g_in.add_cycle([last[0] + 1, last[0] + 2, last[0] + 3])
        g_in.add_edge(n1, last[0] + 1)
        g_in.add_edge(n2, last[0] + 1)
        g_in.add_edge(n1, last[0] + 2)
        g_in.add_edge(n3, last[0] + 2)
        g_in.add_edge(n2, last[0] + 3)
        g_in.add_edge(n3, last[0] + 3)

    if shit:
        shit = False
        g_in = deterministic_sierpinski(g_in, remaining - 1, n1, n2, n3, last)
    else:
        m = last[0] + 1;
        last[0] += 3
        g_in = deterministic_sierpinski(g_in, remaining - 1, m, m + 1, n1, last)
        last[0] += 3
        g_in = deterministic_sierpinski(g_in, remaining - 1, m, n1, n2, last)
        last[0] += 3
        g_in = deterministic_sierpinski(g_in, remaining - 1, m, m + 2, n2, last)
        last[0] += 3
        g_in = deterministic_sierpinski(g_in, remaining - 1, m + 2, n2, n3, last)
        last[0] += 3
        g_in = deterministic_sierpinski(g_in, remaining - 1, m + 2, m + 1, n3, last)
        last[0] += 3
        g_in = deterministic_sierpinski(g_in, remaining - 1, m + 1, n3, n1, last)
    return g_in


def deterministic_apollonian(g: nx.Graph, remaining: int, n1: int, n2: int, n3: int, last):
    g_in = nx.Graph(g)
    flag = False
    if remaining == 0:
        if n1 == -1:
            g_in.add_cycle([0, 1, 2])
            return g_in
        g_in.add_edge(n1, last[0] + 1)
        g_in.add_edge(n2, last[0] + 1)
        g_in.add_edge(n3, last[0] + 1)
        return g_in
    elif n1 == -1:
        g_in.add_cycle([0, 1, 2])
        n1 = 0
        n2 = 1
        n3 = 2
        last[0] = 2
        flag = True
    else:
        g_in.add_edge(n1, last[0] + 1)
        g_in.add_edge(n2, last[0] + 1)
        g_in.add_edge(n3, last[0] + 1)

    if flag:
        flag = False
        g_in = deterministic_apollonian(g_in, remaining - 1, n1, n2, n3, last)
    else:
        m = last[0] + 1
        last[0] += 1
        g_in = deterministic_apollonian(g_in, remaining - 1, m, n1, n2, last)
        last[0] += 1
        g_in = deterministic_apollonian(g_in, remaining - 1, m, n2, n3, last)
        last[0] += 1
        g_in = deterministic_apollonian(g_in, remaining - 1, m, n3, n1, last)
    return g_in


def sn4(g: nx.Graph, n, last):
    if n == 1:
        if g is None:
            g = nx.Graph()
        g.add_cycle([last, last + 1, last + 2, last + 3])
        g.add_edge(last, last + 2)
        g.add_edge(last + 1, last + 3)
        return [g, [last, last + 1, last + 2, last + 3, last + 4]]
    d1 = sn4(g, n - 1, last)
    d2 = sn4(g, n - 1, d1[1][4])
    d3 = sn4(g, n - 1, d2[1][4])
    d4 = sn4(g, n - 1, d3[1][4])
    g1 = d1[0]
    g2 = d2[0]
    g3 = d3[0]
    g4 = d4[0]
    gf: nx.Graph = nx.compose(g1, g2)
    gf = nx.compose(gf, g3)
    gf = nx.compose(gf, g4)
    gf.add_edge(d1[1][0], d2[1][0])
    gf.add_edge(d2[1][2], d3[1][2])
    gf.add_edge(d3[1][0], d4[1][0])
    gf.add_edge(d4[1][2], d1[1][2])
    gf.add_edge(d1[1][1], d3[1][1])
    gf.add_edge(d2[1][1], d4[1][1])
    return [gf, [d1[1][3], d2[1][3], d3[1][3], d4[1][3], d4[1][4]]]


def sn3(g: nx.Graph, n, last):
    if n == 1:
        if g is None:
            g = nx.Graph()
        g.add_cycle([last, last + 1, last + 2])
        return [g, [last, last + 1, last + 2, last + 3]]
    d1 = sn3(g, n - 1, last)
    d2 = sn3(g, n - 1, d1[1][3])
    d3 = sn3(g, n - 1, d2[1][3])
    g1 = d1[0]
    g2 = d2[0]
    g3 = d3[0]
    gf: nx.Graph = nx.compose(g1, g2)
    gf = nx.compose(gf, g3)
    gf.add_edge(d1[1][0], d2[1][0])
    gf.add_edge(d2[1][1], d3[1][1])
    gf.add_edge(d3[1][0], d1[1][1])
    return [gf, [d1[1][2], d2[1][2], d3[1][2], d3[1][3]]]


def sn3p(n):
    ret = sn3(None, n, 0)
    ret[0].add_edge(ret[1][0], ret[1][3])
    ret[0].add_edge(ret[1][1], ret[1][3])
    ret[0].add_edge(ret[1][2], ret[1][3])
    return ret[0]


def sn4p(n):
    ret = sn4(None, n, 0)
    ret[0].add_edge(ret[1][0], ret[1][4])
    ret[0].add_edge(ret[1][1], ret[1][4])
    ret[0].add_edge(ret[1][2], ret[1][4])
    ret[0].add_edge(ret[1][3], ret[1][4])
    return ret[0]


def sn3pp(n):
    ret1 = sn3(None, n, 0)
    ret2 = sn3(None, n - 1, ret1[1][3])
    ret = nx.compose(ret1[0], ret2[0])
    ret.add_edge(ret1[1][0], ret2[1][0])
    ret.add_edge(ret1[1][1], ret2[1][1])
    ret.add_edge(ret1[1][2], ret2[1][2])
    return ret


def sn4pp(n):
    ret1 = sn4(None, n, 0)
    ret2 = sn4(None, n - 1, ret1[1][4])
    ret = nx.compose(ret1[0], ret2[0])
    ret.add_edge(ret1[1][0], ret2[1][0])
    ret.add_edge(ret1[1][1], ret2[1][1])
    ret.add_edge(ret1[1][2], ret2[1][2])
    ret.add_edge(ret1[1][3], ret2[1][3])
    return ret


# def sierpinski_style2(g: nx.Graph)


gr = deterministic_sierpinski(nx.Graph(), 3, -1, -1, -1, [0])
# gr = sn4pp(2)
npm = nx.to_numpy_array(gr)
data = ""
for dat in npm:
    for k in dat:
        data += str(k).replace(".0", "")
        data += ", "
    data += "\n"
# data = str(nx.to_numpy_array(gr))
# data = data.replace("[", "")
# data = data.replace("\n", "")
# data = data.replace("]", "\n")
# data = data.replace(".", ",")
# data = data.replace("  ", " ")
# data = data.replace("  ", " ")
# data = data.replace("  ","\n")
print(data)
nx.draw_networkx(gr, with_labels=True, edge_color='red', node_color='blue', node_size=9)
plt.draw()
plt.show()
