import networkx as nx
import matplotlib.pyplot as plt
from Subgraphs.Graphlets import *
import numpy as np
from executables import read


def remove_graphlets(graph, gid):
    cnts = list()
    f = open('graphlets/Data/G' + str(gid) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(graph).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnts.append(len(graph.edges))
    cnt, gr = g1.count_g1(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(1) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g2.count_g2(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(2) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g3.count_g3(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(3) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g4.count_g4(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(4) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g5.count_g5(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(5) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g6.count_g6(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(6) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g7.count_g7(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(7) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g8.count_g8(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(8) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g9.count_g9(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(9) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g10.count_g10(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(10) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g11.count_g11(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(11) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g12.count_g12(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(12) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g13.count_g13(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(13) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g14.count_g14(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(14) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g15.count_g15(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(15) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g16.count_g16(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(16) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g17.count_g17(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(17) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g18.count_g18(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(18) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g19.count_g19(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(19) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g20.count_g20(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(20) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g21.count_g21(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(21) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g22.count_g22(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(22) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g23.count_g23(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(23) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g24.count_g24(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(24) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g25.count_g25(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(25) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g26.count_g26(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(26) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g27.count_g27(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(27) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g28.count_g28(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(28) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    cnt, gr = g29.count_g29(graph)
    cnts.append(cnt)
    f = open('graphlets/Data/G' + str(gid) + '_' + str(29) + '.txt', 'w')
    f.write(str(nx.to_numpy_matrix(gr).tolist()).replace(".0", "").replace("],", "\n")
            .replace("[", "").replace("]]", "").replace(" ", ""))
    f.close()
    return cnts


# g = nx.Graph()
# g.add_cycle(range(0, 18))
# g.add_edge(2, 4)
# g.add_edge(5, 7)
# g.add_edge(9, 11)
# g.add_edge(13, 15)
# g.add_edge(16, 0)
# g.add_edge(16, 4)
# g.add_edge(15, 19)
# g.add_edge(19, 5)
# g.add_edge(10, 19)
# g.add_edge(17, 20)
# g.add_edge(3, 21)
# print(remove_graphlets(g, 1))
# print(remove_graphlets(g, 3))   ---> TD1


# r = read.read_graph("2.txt")
# r = read.read_graph("C:/Users/S3000/Desktop/data/TD/td1.txt")
# g = nx.from_numpy_matrix(np.matrix(r))
# g = nx.erdos_renyi_graph(100,0.8)
# nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()
# print(remove_graphlets(g, 444))
# file = open('ASD_edge.csv', 'w')
# for (u, v) in g.edges:
#     file.write(str(u) + ',' + str(v) + '\n')
# file.flush()
# file.close()

# print(remove_graphlets(g, 33))
#
#
#
# r = read.read_graph("3.txt")
# g = nx.from_numpy_matrix(np.matrix(r))
# print(remove_graphlets(g, 6))
#
# r = read.read_graph("2.txt")
# g = nx.from_numpy_matrix(np.matrix(r))
# print(remove_graphlets(g, 7))
# print(g20.count_g20(g), g5.count_g5(g))
# print(remove_graphlets(g, 5))
# r = read.read_graph("1.txt")
# g = nx.from_numpy_matrix(np.matrix(r))
# f = open('TDL.txt', 'w')
# # print(str(nx.laplacian_matrix(g).todense()))
# f.write(str(nx.laplacian_matrix(g).todense().tolist()).replace(".0", "").replace("],", "\n")
#         .replace("[", "").replace("]]", "").replace(" ", ""))
# f.close()
# r = read.read_graph("3.txt")
# g = nx.from_numpy_matrix(np.matrix(r))
# f = open('3L.txt', 'w')
# # print(str(nx.laplacian_matrix(g).todense()))
# f.write(str(nx.laplacian_matrix(g).todense().tolist()).replace(".0", "").replace("],", "\n")
#         .replace("[", "").replace("]]", "").replace(" ", ""))
# f.close()
# r = read.read_graph("2.txt")
# g = nx.from_numpy_matrix(np.matrix(r))
# f = open('2L.txt', 'w')
# # print(str(nx.laplacian_matrix(g).todense()))
# f.write(str(nx.laplacian_matrix(g).todense().tolist()).replace(".0", "").replace("],", "\n")
#         .replace("[", "").replace("]]", "").replace(" ", ""))
# f.close()
# r = read.read_graph("4.txt")
# g = nx.from_numpy_matrix(np.matrix(r))
# f = open('4L.txt', 'w')
# # print(str(nx.laplacian_matrix(g).todense()))
# f.write(str(nx.laplacian_matrix(g).todense().tolist()).replace(".0", "").replace("],", "\n")
#         .replace("[", "").replace("]]", "").replace(" ", ""))
# f.close()
# nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()
g = nx.karate_club_graph()
print(remove_graphlets(g, 3))

# nx.draw_networkx(g, with_labels=True, edge_color='red', node_color='blue', node_size=9)
# plt.draw()
# plt.show()
