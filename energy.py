import mathchem as mc


# graph: adjacency matrix as a list
def graph_energy(graph):
    ch = mc.Mol()
    ch.read_matrix(graph)
    return ch.energy()