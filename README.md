# AI Search Algorithms and Backpropagation

![tests](https://github.com/YISHU19/ai-search-algorithms/actions/workflows/tests.yml/badge.svg)

Clean, tested Python implementations of classic AI fundamentals:

| Module | Algorithm | Notes |
|---|---|---|
| `search/bfs.py` | **Breadth-first search** | FIFO queue, level-by-level traversal and goal search |
| `search/dfs.py` | **Depth-first search** | Recursive and iterative (explicit stack) versions; the iterative one handles trees deeper than Python's recursion limit |
| `search/best_first.py` | **Greedy best-first search** | Min-heap on the heuristic, tie-safe ordering, and path reconstruction without changing the tree |
| `neural/backprop.py` | **Backpropagation by hand** | One forward pass and one weight update on a 3-2-1 sigmoid network, the classic textbook worked example |

No third-party dependencies, just the Python standard library.

## Example

```text
$ python demo.py
BFS order:                A -> B -> C -> D -> E -> F
DFS order:                A -> B -> D -> F -> E -> C
Best-first expansion:     A -> B -> D -> E -> C -> F
Best-first path to E:     A -> B -> E

Backpropagation (3-2-1 network, one update):
Output before update: 0.4739
Output after update:  0.5152  (target 1)
```

The tree used in the demo (heuristic values in brackets):

```text
        A(5)
       /    \
    B(2)    C(4)
    /  \
  D(1)  E(3)
  |
  F(6)
```

Best-first expands B before C because B's heuristic is lower. It then expands D before E, and only reaches C once that whole branch has better candidates exhausted.

## Usage

```python
from search import Node, bfs_traversal, best_first_search

tree = Node("A", 5).add(Node("B", 2), Node("C", 4))
bfs_traversal(tree)             # ['A', 'B', 'C']
best_first_search(tree, "C")    # ['A', 'C']
```

## Tests

```bash
python -m unittest discover -s tests -t . -v
```

16 tests cover traversal order, goal search, empty trees, a 5,000-level tree for the iterative DFS, heuristic ties, and the backpropagation numbers against the worked example. They run on every push with GitHub Actions.

## Tech

Python · unittest · GitHub Actions
