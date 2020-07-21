from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = self.tail = None

    def add_to_tail(self, value: Any) -> None:
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next

            new_node = Node(value)
            current.next = new_node
            self.tail = new_node

    def contains(self, value: Any) -> bool:
        if self.head is None:
            return False

        current = self.head
        while current:
            if current.value == value:
                return True

            current = current.next

        return False

    def remove_head(self) -> Any:
        if self.head is None:
            return None
        elif self.head == self.tail:
            previous = self.head.value
            self.head = self.tail = None
            return previous

        previous = self.head.value
        self.head = self.head.next
        return previous

    def get_max(self) -> Any:
        if self.head is None:
            return None

        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value

            current = current.next

        return max_value
