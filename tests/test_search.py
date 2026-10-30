import unittest

from search import (
    Node,
    best_first_search,
    bfs_search,
    bfs_traversal,
    dfs_search,
    dfs_traversal,
    dfs_traversal_iterative,
    expansion_order,
)


def sample_tree():
    """
            A(5)
           /    \\
        B(2)    C(4)
        /  \\
      D(1)  E(3)
      |
      F(6)
    """
    return Node("A", 5).add(
        Node("B", 2).add(Node("D", 1).add(Node("F", 6)), Node("E", 3)),
        Node("C", 4),
    )


class TestBFS(unittest.TestCase):
    def test_traversal_is_level_by_level(self):
        self.assertEqual(bfs_traversal(sample_tree()), ["A", "B", "C", "D", "E", "F"])

    def test_search(self):
        tree = sample_tree()
        self.assertTrue(bfs_search(tree, "F"))
        self.assertFalse(bfs_search(tree, "Z"))

    def test_empty_tree(self):
        self.assertEqual(bfs_traversal(None), [])
        self.assertFalse(bfs_search(None, "A"))


class TestDFS(unittest.TestCase):
    def test_traversal_goes_deep_first(self):
        self.assertEqual(dfs_traversal(sample_tree()), ["A", "B", "D", "F", "E", "C"])

    def test_iterative_matches_recursive(self):
        tree = sample_tree()
        self.assertEqual(dfs_traversal_iterative(tree), dfs_traversal(tree))

    def test_iterative_handles_very_deep_tree(self):
        root = node = Node(0)
        for i in range(1, 5000):  # deeper than Python's default recursion limit
            child = Node(i)
            node.add(child)
            node = child
        self.assertEqual(len(dfs_traversal_iterative(root)), 5000)

    def test_search(self):
        tree = sample_tree()
        self.assertTrue(dfs_search(tree, "C"))
        self.assertFalse(dfs_search(tree, "Z"))


class TestBestFirst(unittest.TestCase):
    def test_finds_path_to_goal(self):
        self.assertEqual(best_first_search(sample_tree(), "E"), ["A", "B", "E"])

    def test_missing_goal_returns_none(self):
        self.assertIsNone(best_first_search(sample_tree(), "Z"))

    def test_expands_lowest_heuristic_first(self):
        self.assertEqual(expansion_order(sample_tree()), ["A", "B", "D", "E", "C", "F"])

    def test_equal_heuristics_do_not_crash(self):
        tree = Node("S", 1).add(Node("X", 2), Node("Y", 2))
        self.assertEqual(best_first_search(tree, "Y"), ["S", "Y"])

    def test_tree_is_not_modified(self):
        tree = sample_tree()
        best_first_search(tree, "F")
        self.assertFalse(hasattr(tree, "parent"))


if __name__ == "__main__":
    unittest.main()
