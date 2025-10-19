# LeetCode 284 - Peeking Iterator
# https://leetcode.com/problems/peeking-iterator/

# ✅ Problem:
# Design an iterator that supports a `peek()` operation — 
# returning the next element in the iteration *without* advancing it.
#
# Implement the `PeekingIterator` class:
#   - PeekingIterator(Iterator<int> nums): initializes the object with the given iterator.
#   - int peek(): returns the next element without moving the pointer.
#   - int next(): moves to the next element and returns it.
#   - bool hasNext(): returns whether there are more elements.
#
# ⚙️ The base Iterator interface is pre-defined:
# class Iterator:
#     def __init__(self, nums: List[int]): ...
#     def hasNext(self) -> bool: ...
#     def next(self) -> int: ...

# 📚 Pattern: Iterator Wrapper / State Buffer
# - Maintain a one-element lookahead buffer (`_next`)
# - peek() reads buffer only; next() reads + refreshes buffer
# - hasNext() checks whether buffer is empty

# 🔍 Core Idea:
# Cache the next element at all times, so we can peek without advancing.

# 🧠 Memory Hook:
# cache next → _next
# peek → return _next
# next → return _next then refresh cache
# hasNext → _next != None

# ✅ Time Complexity: O(1) for all operations
# ✅ Space Complexity: O(1)

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        # Cache the next element if available
        self._next = iterator.next() if iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next

    def next(self):
        """
        Advances the iterator and returns the next element.
        :rtype: int
        """
        res = self._next
        # Refresh the cache
        if self.iterator.hasNext():
            self._next = self.iterator.next()
        else:
            self._next = None
        return res

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self._next is not None


# 🔄 Dry Run Example:
# nums = [1, 2, 3]
# iter = PeekingIterator(Iterator(nums))
#
# peek() → 1   # preview
# next() → 1   # consume
# peek() → 2
# next() → 2
# hasNext() → True
# next() → 3
# hasNext() → False