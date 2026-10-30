"""Run every algorithm on the same example tree and print the results."""

from neural import backprop
from search import (
    Node,
    best_first_search,
    bfs_traversal,
    dfs_traversal,
    expansion_order,
)


def main():
    #         A(5)
    #        /    \
    #     B(2)    C(4)
    #     /  \
    #   D(1)  E(3)
    #   |
    #   F(6)
    tree = Node("A", 5).add(
        Node("B", 2).add(Node("D", 1).add(Node("F", 6)), Node("E", 3)),
        Node("C", 4),
    )

    print("BFS order:              ", " -> ".join(bfs_traversal(tree)))
    print("DFS order:              ", " -> ".join(dfs_traversal(tree)))
    print("Best-first expansion:   ", " -> ".join(expansion_order(tree)))
    print("Best-first path to E:   ", " -> ".join(best_first_search(tree, "E")))
    print()
    print("Backpropagation (3-2-1 network, one update):")
    backprop.main()


if __name__ == "__main__":
    main()
