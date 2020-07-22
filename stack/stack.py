"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""
from typing import Any
from singly_linked_list import LinkedList


class Stack:
    def __init__(self) -> None:
        self.storage: LinkedList = LinkedList()
        self.size = self.storage.__len__()

    def __len__(self) -> int:
        return self.storage.__len__()

    def push(self, value: Any) -> None:
        self.storage.add_to_tail(value)

    def pop(self) -> Any:
        if self.__len__() == 0:
            return None

        return self.storage.remove_tail()
