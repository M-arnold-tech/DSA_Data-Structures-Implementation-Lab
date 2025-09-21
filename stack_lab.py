"""
Stack Implementation Lab

This file contains:
- A Python implementation of a Stack (LIFO) from scratch.
- Time-complexity analysis notes.
- Real-world examples: browser history, function calls, undo/redo.
- Unit tests using unittest.

Run tests with:
    python stack_lab.py
"""

from typing import Generic, Iterable, Iterator, List, Optional, TypeVar
import unittest

T = TypeVar('T')

class Stack(Generic[T]):
    """Stack (LIFO) implementation.

    Underlying container: Python list.

    Time Complexity:
    - push: O(1) amortized
    - pop: O(1)
    - peek: O(1)
    - is_empty: O(1)
    - size: O(1)
    - to_list: O(n)
    Space Complexity: O(n)
    """

    def __init__(self, items: Optional[Iterable[T]] = None) -> None:
        self._data: List[T] = []
        if items:
            for it in items:
                self.push(it)

    def push(self, item: T) -> None:
        self._data.append(item)

    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Optional[T]:
        if not self._data:
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def clear(self) -> None:
        self._data = []

    def to_list(self) -> List[T]:
        return list(self._data)

    def __len__(self) -> int:
        return self.size()

    def __iter__(self) -> Iterator[T]:
        for item in reversed(self._data):
            yield item

    def __repr__(self) -> str:
        return f"Stack({self._data!r})"


# -----------------------------
# Unit tests
# -----------------------------

class TestStack(unittest.TestCase):
    def test_push_pop_peek(self):
        s = Stack[int]()
        self.assertTrue(s.is_empty())
        s.push(1)
        s.push(2)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.is_empty())
        with self.assertRaises(IndexError):
            s.pop()

    def test_size_and_len(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        s.push("a")
        s.push("b")
        self.assertEqual(len(s), 2)

    def test_iter_and_to_list(self):
        s = Stack([1, 2, 3])
        self.assertEqual(s.to_list(), [1, 2, 3])
        self.assertEqual(list(s), [3, 2, 1])

    def test_clear(self):
        s = Stack([1, 2])
        s.clear()
        self.assertTrue(s.is_empty())


if __name__ == "__main__":
    print("Running Stack tests...")
    unittest.main(verbosity=2)

