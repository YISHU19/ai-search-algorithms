"""Breadth-first search: explore the tree level by level using a FIFO queue."""

from collections import deque


def bfs_traversal(start):
    """Return node values in breadth-first order."""
    if start is None:
        return []

    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node.value)
        queue.extend(node.children)
    return order


def bfs_search(start, target):
    """Return True if a node with value ``target`` is reachable from ``start``."""
    if start is None:
        return False

    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node.value == target:
            return True
        queue.extend(node.children)
    return False
