"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from typing import List, Any


class Queue:
    def __init__(self) -> None:
        self.size = 0
        self.storage: List[Any] = []

    def __len__(self) -> int:
        return len(self.storage)

    def enqueue(self, value) -> None:
        self.storage.insert(0, value)
        self.size += 1

    def dequeue(self) -> Any:
        if self.size == 0:
            return

        dequeued = self.storage[-1]
        del self.storage[-1]
        self.size -= 1
        return dequeued
