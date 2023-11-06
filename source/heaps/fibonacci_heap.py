from typing import Any


class Node:
    """A node in a Fibonacci heap."""

    def __init__(self, key: int | float, data: Any = None) -> None:
        """
        Creates an isolated root node with a key.
        :param key: A numeric key for ordering nodes.
        """
        self.key: int | float = key         # A numeric key for ordering nodes
        self.data: Any = data               # Optional node data
        self.child_count: int = 0           # Number of child nodes
        self.marked: bool = False           # Is the node missing one child (from a binomial tree)
        self.parent: Node | None = None     # Parent node, if not root
        self.child: Node | None = None      # Any one child node, if any
        self.left: Node = self              # Left sibling, or self if none
        self.right: Node = self             # Right sibling, or self if none
