"""Greedy best-first search: always expand the node with the lowest heuristic."""

import heapq
from itertools import count


def best_first_search(start, goal):
    """Return the path (list of values) from ``start`` to ``goal``, or None.

    The frontier is a min-heap keyed on each node's heuristic. A running
    counter breaks ties so nodes themselves are never compared, and parents
    are tracked in a dict so the tree is not modified during the search.
    """
    if start is None:
        return None

    tie = count()
    frontier = [(start.heuristic, next(tie), start)]
    parent = {id(start): None}
    nodes = {id(start): start}

    while frontier:
        _, _, node = heapq.heappop(frontier)
        if node.value == goal:
            return _reconstruct(node, parent, nodes)

        for child in node.children:
            if id(child) not in parent:
                parent[id(child)] = id(node)
                nodes[id(child)] = child
                heapq.heappush(frontier, (child.heuristic, next(tie), child))

    return None


def expansion_order(start):
    """Return node values in the order greedy best-first would expand them."""
    if start is None:
        return []

    tie = count()
    frontier = [(start.heuristic, next(tie), start)]
    order = []
    while frontier:
        _, _, node = heapq.heappop(frontier)
        order.append(node.value)
        for child in node.children:
            heapq.heappush(frontier, (child.heuristic, next(tie), child))
    return order


def _reconstruct(node, parent, nodes):
    path = []
    key = id(node)
    while key is not None:
        path.append(nodes[key].value)
        key = parent[key]
    return path[::-1]
