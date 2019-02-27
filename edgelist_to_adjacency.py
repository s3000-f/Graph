import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def read_graph(name):
    f = open(name, "r")
    msg = f.read()
    msg_list = msg.split('\n')
    print(msg_list)
    dat = []
    length = len(msg_list)
    length = int(sqrt(length))
    sub_dat = []
    cnt = 0
    for it in msg_list:
        el = it.split(' ')
        if len(el) == 2:
            dat.append((el[0], el[1]))
    return dat


d = read_graph('r.txt')
g = nx.from_edgelist(d)
f = open('4.txt', 'w')
f.write(str(nx.to_numpy_matrix(g).tolist()).replace(".0", "").replace("],", "\n")
        .replace("[", "").replace("]]", "").replace(" ", ""))
f.close()
nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
plt.draw()
plt.show()
