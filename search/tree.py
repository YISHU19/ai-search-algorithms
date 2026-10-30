"""A minimal tree node used by all the search algorithms."""


class Node:
    """A tree node with a value, optional heuristic and a list of children."""

    def __init__(self, value, heuristic=0):
        self.value = value
        self.heuristic = heuristic
        self.children = []

    def add(self, *children):
        """Attach children to this node and return the node (for chaining)."""
        self.children.extend(children)
        return self

    def __repr__(self):
        return f"Node({self.value!r})"
