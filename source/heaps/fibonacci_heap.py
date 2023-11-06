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


class MinimumFibonacciHeap:
    """A minimum Fibonacci heap."""

    def __init__(self, single_node: Node | None = None) -> None:
        """
        Creates an empty heap, or a single-item heap.
        :param single_node: An optional node for a single-node heap.
        """
        self.minimum: Node | None = single_node     # The heap node with the smallest key

    def get_minimum(self) -> Node:
        """
        :return: The heap node with the smallest key.
        """
        return self.minimum

    def merge(self, other: "MinimumFibonacciHeap") -> None:
        """
        Merges another minimum Fibonacci heap with this one by linking the root levels.
        :param other: The heap to be merged.
        """
        self.minimum.left.right = other.minimum.right
        other.minimum.right.left = self.minimum.left
        self.minimum.left = other.minimum
        other.minimum.right = self.minimum

        # Update the new minimum node
        if self.minimum.key > other.minimum.key:
            self.minimum = other.minimum

    def insert(self, node: Node) -> None:
        """
        Inserts a node into the heap in the root level.
        :param node: The heap node to be inserted.
        """
        single_heap: MinimumFibonacciHeap = MinimumFibonacciHeap(node)  # Create a single-node heap
        self.merge(single_heap)     # Merge the single-node heap with this heap to insert the new node
