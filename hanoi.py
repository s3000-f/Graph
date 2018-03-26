from Subgraphs import read as r
import networkx as nx
import numpy as np
import planarity_networkx as pn
import planarity as pl

adr = "/Users/s3000/Desktop/hanoi/" + str(35) + ".txt"
raw = r.read_graph(adr)
g: nx.Graph = nx.from_numpy_matrix(np.matrix(raw))
nx.write_gexf(g, "test.gexf")
print(pl.is_planar(pn.pgraph_graph(g)))
