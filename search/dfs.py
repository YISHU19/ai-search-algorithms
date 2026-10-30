"""Depth-first search: follow each branch to the bottom before backtracking."""


def dfs_traversal(start):
    """Return node values in depth-first (pre-order) order, recursively."""
    order = []

    def visit(node):
        order.append(node.value)
        for child in node.children:
            visit(child)

    if start is not None:
        visit(start)
    return order


def dfs_traversal_iterative(start):
    """Same order as :func:`dfs_traversal`, using an explicit stack.

    Useful for very deep trees, where recursion would hit Python's limit.
    """
    if start is None:
        return []

    order = []
    stack = [start]
    while stack:
        node = stack.pop()
        order.append(node.value)
        # Push children in reverse so the leftmost child is visited first
        stack.extend(reversed(node.children))
    return order


def dfs_search(start, target):
    """Return True if a node with value ``target`` is reachable from ``start``."""
    if start is None:
        return False
    if start.value == target:
        return True
    return any(dfs_search(child, target) for child in start.children)
