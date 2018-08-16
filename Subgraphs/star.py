import operator as op
import networkx as nx
import functools


def ncr(n, r):
    r = min(r, n - r)
    if r == 0:
        return 1
    numer = functools.reduce(op.mul, iter(range(n, n - r, -1)))
    denom = functools.reduce(op.mul, iter(range(1, r + 1)))
    return numer // denom


def count_star(graph, r):
    sums = 0
    for node in graph.node():
        length = len(list(graph.neighbors(node)))
        if length >= r:
            sums += ncr(length, r)
    return sums
