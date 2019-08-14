#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: Dijkstra.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-07-14 09:19
# @Last Modified: 2019-07-14 09:19

import heapq
from collections import defaultdict, namedtuple

import numpy as np

Vertex = namedtuple('Vertex', 'dst, d')



class Graph:

    def __init__(self):
        self._graph = defaultdict(dict)
        self._nodes = set()

    def add(self, s, w, d):
        self._graph[s][d] = w
        self._nodes.add(s)
        self._nodes.add(d)

    def dijkstra(self, s, d):
        predecessor = np.full((len(self._nodes), len(self._nodes)), 99)
        queue = list()
        inqueue = set()
        heapq.heappush(queue, Vertex(0, s))
        while len(queue) > 0:
            min_vertex = heapq.heappop(queue)
            if min_vertex.d == d:
                route = self.route(predecessor, d)
                return min_vertex.dst, route
            if min_vertex.d not in inqueue:
                inqueue.add(min_vertex.d)
                for k, v in self._graph[min_vertex.d].items():
                    heapq.heappush(queue, Vertex(min_vertex.dst + v, k))
                    if predecessor[k, min_vertex.d] > v:
                        predecessor[k, min_vertex.d] = v
        return -1

    def route(self, predecessor, d):
        route = list()
        route.append(d)
        c = d
        while 1:
            try:
                c = predecessor[c].argmin()
            except KeyError:
                return reversed(route)
            else:
                route.append(int(c))
            if (predecessor[c] == 99).all():
                return reversed(route)


def fixture():
    g = Graph()
    g.add(0, 10, 1)
    g.add(0, 15, 4)
    g.add(1, 15, 2)
    g.add(1, 2, 3)
    g.add(3, 1, 2)
    g.add(2, 5, 5)
    g.add(3, 12, 5)
    g.add(4, 10, 5)
    print(g._graph)
    return g


if __name__ == "__main__":
    g = fixture()
    dst, route = g.dijkstra(0, 5)
    print(f'route is({dst}): {list(route)}')
