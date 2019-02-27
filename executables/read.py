from math import sqrt
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def read_graph(name):
    f = open(name, "r")
    msg = f.read()
    msg_list = msg.split()
    dat = []
    length = len(msg_list)
    length = int(sqrt(length))
    sub_dat = []
    cnt = 0
    for it in msg_list:
        if cnt == (length - 1):
            cnt = 0
            i = int(ord(it[0]) - 48)
            sub_dat.append(i)
            dat.append(sub_dat)
            sub_dat = []
        else:
            i = int(ord(it[0]) - 48)
            sub_dat.append(i)
            cnt += 1
    return dat


def read_samples():
    ret = []
    for i in range(1, 4):
        for j in range(1, 5):
            name = "Matrises/" + str(i) + "/" + str(j) + ".txt"
            ret.append(read_graph(name))
    return ret


# r = read_graph("C:/Users/S3000/Desktop/data/TD/td1.txt")
# g = nx.from_numpy_matrix(np.matrix(r))

# nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()