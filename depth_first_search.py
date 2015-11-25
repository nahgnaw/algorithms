# -*- coding: utf8 -*-


def depth_first_search(g, u, discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            depth_first_search(g, v, discovered)


def construct_path(u, v, discovered):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[v]
            parent = e.opposite(v)
            path.append(parent)
            walk = parent
        path.reverse()
    return path


def dfs_complete(g):
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            depth_first_search(g, u, forest)
    return forest