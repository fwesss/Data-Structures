"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
from typing import Any


class ListNode:
    def __init__(self, value: Any, prev=None, next_node=None) -> None:
        self.prev = prev
        self.value = value
        self.next = next_node


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node: ListNode = None) -> None:
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value: Any) -> None:
        if self.head is None:
            self.head = self.tail = ListNode(value)
            self.length += 1
        else:
            new_node = ListNode(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self) -> Any:
        if self.head is None:
            return None

        if self.head == self.tail:
            previous = self.head.value
            self.head = self.tail = None
            self.length -= 1
            return previous

        previous = self.head.value
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        return previous

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value: Any) -> None:
        if self.tail is None:
            self.head = self.tail = ListNode(value)
            self.length += 1
        else:
            new_node = ListNode(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self) -> None:
        if self.tail is None:
            return None

        if self.tail == self.head:
            previous = self.tail.value
            self.tail = self.head = None
            self.length -= 1
            return previous

        previous = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return previous

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node: ListNode) -> None:
        if self.head is None or self.head.next is None or node is self.head:
            return

        if node is self.tail:
            self.add_to_head(node.value)
            self.remove_from_tail()
        else:
            node.next = self.head
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.head.prev = node
            self.head = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node: ListNode) -> None:
        if self.tail is None or self.tail.prev is None or node is self.tail:
            return

        if node is self.head:
            self.add_to_tail(node.value)
            self.remove_from_head()
        else:
            node.prev = self.tail
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.tail.next = node
            self.tail = self.tail.next

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node: ListNode) -> None:
        if self.head is self.tail is node:
            self.head = self.tail = None
            self.length -= 1
        elif self.head is None or node is self.head:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        elif self.tail is None or node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        else:
            current = self.head
            while current:
                if current is node:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self) -> Any:
        if self.length == 0:
            return None

        if self.head is None:
            return self.tail.value

        if self.tail is None:
            return self.head.value

        max = self.head.value
        current = self.head
        while current:
            if current.value > max:
                max = current.value

            current = current.next

        return max

    def traverse(self) -> None:
        current = self.head
        nodes = []
        while current:
            nodes.append(current.value)
            current = current.next

        print(nodes)
