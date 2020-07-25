from typing import Any, Optional


class Node:
    def __init__(self, value: Any, next_node: Optional[Any] = None) -> None:
        self.value = value
        self.next = next_node

    def get_value(self) -> Any:
        return self.value

    def get_next(self) -> object:
        return self.next

    def set_next(self, new_next) -> None:
        self.next = new_next


class LinkedList:
    def __init__(self) -> None:
        self.head = self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def add_to_head(self, value: Any) -> None:
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node

        self.length += 1

    def add_to_tail(self, value: Any) -> None:
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

        self.length += 1

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
            self.length -= 1
            return previous

        previous = self.head.value
        self.head = self.head.next
        self.length -= 1
        return previous

    def remove_tail(self) -> Any:
        if self.tail is None:
            return None
        elif self.tail == self.head:
            previous = self.tail.value
            self.tail = self.head = None
            self.length -= 1
            return previous

        current = self.head
        while current.next:
            if current.next is self.tail:
                previous = self.tail.value
                self.tail = current
                self.tail.next = None
                self.length -= 1
                return previous

            current = current.next

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
