from typing import Callable, List


class Heap:
    # defaults to a max heap if no comparator is specified
    def __init__(
        self, comparator: Callable[[int, int], bool] = lambda x, y: x > y
    ) -> None:
        self._storage: List[int] = []
        self._comparator = comparator

    @property
    def storage(self):
        return self._storage

    @property
    def comparator(self) -> Callable[[int, int], bool]:
        return self._comparator

    @property
    def size(self) -> int:
        return len(self.storage)

    def insert(self, value: int) -> None:
        self.storage.append(value)
        self._bubble_up(self.size - 1)

    def delete(self) -> int:
        deleted = self.storage[0]
        if self.size == 1:
            del self.storage[0]
            return deleted
        else:
            self._sift_down()
        del self.storage[-1]
        return deleted

    def get_priority(self) -> int:
        return self.storage[0]

    def get_size(self) -> int:
        return self.size

    @staticmethod
    def get_parent_index(index: int) -> int:
        if (index + 1) % 2 == 0:
            return ((index + 1) // 2) - 1
        else:
            return (index // 2) - 1

    def get_child_index(self, index: int) -> int:
        if (index + 1) * 2 > self.size:
            raise IndexError

        if (
            self.comparator(
                self.storage[(index + 1) * 2 - 1], self.storage[(index + 1) * 2]
            )
            or (index + 1) * 2 == self.size
        ):
            return (index + 1) * 2 - 1

        return (index + 1) * 2

    def _bubble_up(self, index: int) -> None:
        child = index
        parent = self.get_parent_index(child)

        while parent >= 0 and self.comparator(
            self.storage[child], self.storage[parent]
        ):
            self.storage[parent], self.storage[child] = (
                self.storage[child],
                self.storage[parent],
            )
            child = parent
            parent = self.get_parent_index(child)

    def _sift_down(self, index: int = 0) -> None:
        if self.size == 2:
            self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        else:
            parent = index
            child = self.get_child_index(parent)

            while (
                child < self.size - 1
                and self.comparator(self.storage[parent], self.storage[child])
                or self.storage[parent] == self.storage[child]
            ):
                self.storage[parent], self.storage[child] = (
                    self.storage[child],
                    self.storage[parent],
                )

                try:
                    parent = child
                    child = self.get_child_index(parent)
                except IndexError:
                    self.storage[parent], self.storage[-1] = (
                        self.storage[-1],
                        self.storage[parent],
                    )
                    break
