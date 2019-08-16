#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: TransitiveClosure.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-08-15 15:05
# @Last Modified: 2019-08-15 15:05

from copy import deepcopy

from Graph import AdjacencyMap


def floyd_warshall(graph: AdjacencyMap):
    g = deepcopy(graph)
    vertices = list(g.vertices)
    for k in vertices:
        for i in vertices:
            if i != k and g.get_edge(i, k) is not None:
                for j in vertices:
                    if i!=j!=k and g.get_edge(k, j) is not None:
                        g.insert_edges(i, j)
    return g


if __name__ == '__main__':
    dg = AdjacencyMap(is_directed=True)
    dg.insert_edges(1, 2)
    dg.insert_edges(2, 4)
    dg.insert_edges(1, 3)
    dg.insert_edges(3, 4)
    dg.insert_edges(4, 1)
    dg.insert_edges(4, 5)

    assert dg.get_edge(1, 4) is None
    ng = floyd_warshall(dg)
    assert ng.get_edge(1,5) is not None

