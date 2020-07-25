"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value: int) -> None:
        self._value = value
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = BSTNode(value)

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = BSTNode(value)

    # Insert the given value into the tree
    def insert(self, value: int) -> None:
        if value < self.value:
            if self.left:
                return self.left.insert(value)

            self.left = value
        else:
            if self.right:
                return self.right.insert(value)

            self.right = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target: int) -> bool:
        if target is self.value:
            return True

        if target < self.value and self.left:
            return self.left.contains(target)

        if target > self.value and self.right:
            return self.right.contains(target)

        return False

    # Return the maximum value found in the tree
    def get_max(self) -> int:
        if not self.right:
            return self.value

        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn) -> None:
        if not self:
            return

        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, root) -> None:
        if not root:
            return

        self.in_order_print(root.left)
        print(root.value)
        self.in_order_print(root.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    @staticmethod
    def bft_print(root) -> None:
        if not root:
            return

        queue = Queue()
        current = root
        while current:
            print(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
            current = queue.dequeue()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    @staticmethod
    def dft_print(root) -> None:
        if not root:
            return

        stack = Stack()
        current = root
        while current:
            print(current.value)
            if current.left:
                if current.right:
                    stack.push(current.right)

                current = current.left
            elif current.right:
                current = current.right
            else:
                current = stack.pop()

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, root) -> None:
        if not root:
            return

        print(root.value)
        self.pre_order_dft(root.left)
        self.pre_order_dft(root.right)

    def in_order_dft(self, root) -> None:
        if not root:
            return

        self.in_order_dft(root.left)
        print(root.value)
        self.in_order_dft(root.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, root) -> None:
        if not root:
            return

        self.post_order_dft(root.left)
        self.post_order_dft(root.right)
        print(root.value)


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print(bst)
bst.dft_print(bst)

print("elegant methods")
print("pre order")
bst.pre_order_dft(bst)
print("in order")
bst.in_order_dft(bst)
print("post order")
bst.post_order_dft(bst)
