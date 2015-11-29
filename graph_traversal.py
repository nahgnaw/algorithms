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


def breadth_first_search(g, s, discovered):
    level = [s]
    while len(level) > 0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)
        level = next_level


def topological_sort(g):
    topo = []
    ready = []
    incount = {}
    for u in g.vertices():
        incount[u] = g.degree(u, False)
        if incount[u] == 0:
            ready.append(u)
    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)
        for e in g.incident_edges(u):
            v = e.opposite(u)
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(v)
    return topo
