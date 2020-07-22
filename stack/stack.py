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
from typing import Any, List


class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.storage: List[Any] = []

    def __len__(self) -> int:
        return len(self.storage)

    def push(self, value: Any) -> None:
        self.storage.append(value)
        self.size += 1

    def pop(self) -> Any:
        if self.size == 0:
            return None

        popped = self.storage[-1]
        del self.storage[-1]
        self.size -= 1
        return popped
