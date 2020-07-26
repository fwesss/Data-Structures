from typing import Any
from doubly_linked_list import DoublyLinkedList


class Storage(dict):
    def __setitem__(self, key: str, value: Any) -> None:
        super().__setitem__(key, value)


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10) -> None:
        self._limit = limit
        self._size = 0
        self._storage: Storage = Storage()
        self._dll = DoublyLinkedList()

    @property
    def limit(self) -> int:
        return self._limit

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int) -> None:
        self._size = value

    @property
    def storage(self) -> Storage:
        return self._storage

    @property
    def dll(self) -> DoublyLinkedList:
        return self._dll

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key: str) -> Any:
        if key in self.storage:
            self.dll.move_to_front(self.storage[key])
            return self.storage[key].value

        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key: str, value: Any) -> None:
        if key not in self.storage:
            if self.size == self.limit:
                old = self.dll.remove_from_tail()
                for old_key, node in self.storage.items():
                    if node.value == old:
                        self.storage.pop(old_key)
                        break
            else:
                self.size += 1

        head = self.dll.add_to_head(value)
        self.storage[key] = head
