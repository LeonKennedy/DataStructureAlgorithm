#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: Graph.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-08-13 15:27
# @Last Modified: 2019-08-13 15:27

from collections import defaultdict
from typing import List


class Graph: pass


class Vertex:
    __slots__ = "_element"

    def __init__(self, element):
        self._element = element

    def __hash__(self):
        return hash(id(self))


class Edge:

    def __init__(self, u, v, x):
        self._origin = u
        self._destination = v
        self._element = x

    def __hash__(self):
        return hash((self._origin, self._destination))

    @property
    def origin(self):
        return self._origin

    @property
    def destination(self):
        return self._destination


class AdjacencyMap(Graph):

    def __init__(self, is_directed=True):
        self._is_directed = is_directed
        self._incoming = defaultdict(dict)
        if is_directed:
            self._outgoing = defaultdict(dict)
        else:
            self._outgoing = self._incoming

        self._vertex_count = 0
        self._edge_count = 0

    @property
    def is_directed(self):
        return self._is_directed

    @property
    def vertex_count(self):
        return len(set(self._incoming.keys()) | set(self._outgoing.keys()))

    @property
    def edge_count(self):
        return self._edge_count

    @property
    def vertices(self) -> List:
        if self._is_directed:
            return set(self._incoming.keys()) | set(self._outgoing.keys())
        else:
            return set(self._incoming.keys())

    @property
    def edges(self):
        out = set()
        for c in self._outgoing.values():
            out.update(c)
        return out

    def insert_vertex(self, x):
        v = Vertex(x)
        self._outgoging[v] = dict()
        self._vertex_count += 1

    def insert_edges(self, u, v, x=1):
        e = Edge(u, v, x)
        self._edge_count += 1
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def get_edge(self, u, v):
        try:
            return self._outgoing[u][v]
        except KeyError:
            return None

    def degree(self, u, out=True):
        return len(self._outgoing[u] if out else self._incoming[u])

    def incident_edges(self, u, out=True):
        return self._outgoing[u].values() if out else self._incoming[u].values()

    def remove_vertex(self, v):
        for k in self._outgoing[v].keys():
            del self._incoming[k][v]
            self._edge_count -= 1
        del self._outgoing[v]

        if self.is_directed:
            for k in self._incoming[v].keys():
                del self._outgoing[k][v]
                self._edge_count -= 1
            del self._incoming[v]

    def remove_edge(self, e):
        del self._outgoing[e.origin][e.destination]
        del self._incoming[e.destination][e.origin]
        self._edge_count -= 1


if __name__ == '__main__':
    s = AdjacencyMap(is_directed=False)
    s.insert_edges(1, 2)
    s.insert_edges(2, 4)
    s.insert_edges(1, 3)
    s.insert_edges(3, 4)
    s.insert_edges(1, 4)
    assert s.edge_count == 5
    assert s.vertex_count == 4
    assert {1, 2, 3, 4} == s.vertices
    assert isinstance(s.get_edge(1, 2), Edge)
    assert s.get_edge(2, 3) is None
    assert s.degree(2) == 2
    s.remove_edge(s.get_edge(1, 3))
    assert s.edge_count == 4
    s.remove_vertex(3)
    assert s.edge_count == 3

    s = AdjacencyMap()
    s.insert_edges(1, 2)
    s.insert_edges(2, 4)
    s.insert_edges(1, 3)
    s.insert_edges(3, 4)
    s.insert_edges(4, 1)
    assert s.edge_count == 5
    assert s.vertex_count == 4
    assert {1, 2, 3, 4} == s.vertices
    assert s.degree(1) == 2
    assert s.degree(1, out=False) == 1
    s.remove_vertex(3)
    assert s.edge_count == 3
    assert s.vertex_count == 3
