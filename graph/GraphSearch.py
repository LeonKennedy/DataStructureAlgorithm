#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: GraphSearch.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 
# @Create: 2019-08-14 16:25
# @Last Modified: 2019-08-14 16:25

from Graph import AdjacencyMap
from collections import deque


def board_first_search(graph: AdjacencyMap, vertex):
    visited = set()
    vertices_list = deque([vertex])
    while len(vertices_list) > 0:
        v = vertices_list.popleft()
        yield v
        visited.add(v)
        for edge in graph.incident_edges(v):
            if edge.destination not in visited and edge.destination not in vertices_list:
                vertices_list.append(edge.destination)


def deep_first_search(graph: AdjacencyMap, vertex):
    visited = set()

    def _dfs(g, v):
        visited.add(v)
        yield v
        for edge in g.incident_edges(v):
            if edge.destination not in visited:
                yield from _dfs(g, edge.destination)

    for vv in _dfs(graph, vertex):
        yield vv





if __name__ == '__main__':
    g = AdjacencyMap(is_directed=False)
    g.insert_edges(1, 2)
    g.insert_edges(2, 4)
    g.insert_edges(1, 3)
    g.insert_edges(3, 4)
    g.insert_edges(1, 4)
    print("[undirected] dfs:", end='')
    for v in deep_first_search(g, 1):
        print(v , end=" ")
    print()
    print("[undirected] BFS:", end='')
    for v in board_first_search(g, 1):
        print(v, end=" ")
    print()

    dg = AdjacencyMap(is_directed=True)
    dg.insert_edges(1, 2)
    dg.insert_edges(2, 4)
    dg.insert_edges(1, 3)
    dg.insert_edges(3, 4)
    dg.insert_edges(1, 4)

    print("[directed] dfs:", end='')
    for v in deep_first_search(g, 1):
        print(v, end=" ")
    print()
    print("[directed] BFS:", end='')
    for v in board_first_search(g, 1):
        print(v, end=" ")
    print()