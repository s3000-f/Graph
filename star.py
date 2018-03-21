import operator as op
import networkx as nx


def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom


def count_star(graph):
    sums = 0
    for node in graph.node():
        length = len(list(graph.neighbors(node)))
        if length > 2:
            sums += ncr(length, 3)
    return sums