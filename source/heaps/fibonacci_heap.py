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

    def __init__(self, node: Node | None = None) -> None:
        """
        Creates an empty heap, or initializes a heap from existing nodes.
        :param node: Optional. Any node in the root-level of existing nodes forming a minimum Fibonacci heap.
        """
        self.minimum: Node | None = self.get_minimum_sibling(node) if node is not None else None

    @staticmethod
    def get_minimum_sibling(node: Node) -> Node:
        """
        Finds the sibling node (including the given node) with the smallest key.
        :param node: Any heap node with or without siblings.
        :return: The sibling node with the smallest key. This could be itself.
        """
        start: Node = node
        smallest_sibling: Node = node
        smallest_key: int | float = node.key

        # Traverse all other siblings to find the one with the smallest key
        while node.right is not node and node.right is not start:
            node = node.right

            if node.key < smallest_key:
                smallest_sibling = node
                smallest_key = node.key

        return smallest_sibling

    @staticmethod
    def set_roots(node: Node) -> None:
        """
        Sets a node and all siblings as roots by removing their parent pointer.
        :param node: A heap node with or without siblings.
        """
        start: Node = node
        node.parent = None

        while node.right is not node and node.right is not start:
            node = node.right
            node.parent = None

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
        # Link the root levels of both heaps
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

    def extract_minimum(self) -> Node:
        """
        Removes and returns the heap item with the smallest key.
        :return: The heap node with the smallest key.
        """
        # Unlink the minimum node from its siblings
        self.minimum.left.right = self.minimum.right
        self.minimum.right.left = self.minimum.left
        current: Node = self.minimum.right  # Save a sibling node for later processing
        self.minimum.left = None
        self.minimum.right = None

        # Form a new heap with any children of the minimum node and merge it with the original heap
        if self.minimum.child_count > 0:
            self.set_roots(self.minimum.child)  # Set the children to be roots of the new child heap
            child_heap: MinimumFibonacciHeap = MinimumFibonacciHeap(self.minimum.child)
            self.merge(child_heap)

    def consolidate(self, start: Node) -> None:
        """
        Combines nodes in the root-level until there is only one root node for a given child count.
        :param start: The node in the root level to start consolidating from.
        """
        auxiliary_array: list[Node | None] = [None for _ in range(10)]  # Maximum child count
        stop: Node = start.left     # TODO: Check for single node in root level
        current: Node = start
        minimum: Node = start

        while current is not stop:
            if current.key < minimum.key:
                minimum = current

            if auxiliary_array[current.child_count] is None:
                auxiliary_array[current.child_count] = current
            else:
                

            current = current.right
