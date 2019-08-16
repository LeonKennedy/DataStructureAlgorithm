#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: TopologicalSort.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-08-16 15:39
# @Last Modified: 2019-08-16 15:39

from Graph import AdjacencyMap



def topological_sort(graph: AdjacencyMap):
    incount = dict()
    queue = list()
    for vertex in graph.vertices:
        incount[vertex] = graph.degree(vertex, False)

    walk = None
    while len(incount):
        if walk == incount:
            break
        walk = incount.copy()
        for k,v in walk.items():
            if v == 0:
                queue.append(k)
                for e in graph.incident_edges(k):
                    incount[e.destination] -= 1
                del incount[k]
    return queue



if __name__ == '__main__':
    dg = AdjacencyMap(is_directed=True)
    dg.insert_edges(1, 2)
    dg.insert_edges(1, 3)
    dg.insert_edges(4, 3)
    dg.insert_edges(3, 5)
    dg.insert_edges(3, 6)
    dg.insert_edges(4, 6)
    dg.insert_edges(5, 7)
    dg.insert_edges(1, 7)
    dg.insert_edges(7, 8)
    dg.insert_edges(2, 8)

    # dg.insert_edges(5, 1)   # 如果有环 就退出
    # dg.insert_edges(9, 8)
    # dg.insert_edges(8, 9)
    print(topological_sort(dg))
