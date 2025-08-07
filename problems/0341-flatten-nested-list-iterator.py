# LeetCode 341 - Flatten Nested List Iterator
# https://leetcode.com/problems/flatten-nested-list-iterator/

# ✅ Problem:
# Given a nested list of integers (some elements may be integers, others lists),
# implement an iterator to flatten it and return all integers in left-to-right order.

# Example:
# Input: [1,[4,[6]]]
# Output: [1, 4, 6]

# 📚 Pattern:
# Stack-Based Lazy Iterator Traversal
# (Similar to DFS, but flattened just-in-time)

# 🔍 Key Insight:
# - Treat nested lists as a tree-like structure
# - Use a stack to simulate DFS
# - Push list elements in **reversed order** to preserve left-to-right traversal
# - Expand nested lists only as needed inside `hasNext()`

# 🧠 Memory Hook:
# "Stack ← reversed input"
# "hasNext() flattens just enough"
# "next() returns int — nothing more"
# → DFS with deferred expansion

# ✅ Time Complexity: Amortized O(1) per call
# ✅ Space Complexity: O(N) for N total nested integers

# 📌 Common Interview Gotchas:
# - ❌ Flattening everything in __init__ (not lazy!)
# - ❌ Mutating state inside `next()` (should be a pure return)
# - ✅ Must reverse when pushing lists into stack (simulate queue with stack)

# LeetCode interface definition for reference
class NestedInteger:
    def __init__(self, value):
        if isinstance(value, int):
            self._isInteger = True
            self._value = value
        else:
            self._isInteger = False
            self._value = [NestedInteger(x) for x in value]

    def isInteger(self):
        return self._isInteger

    def getInteger(self):
        return self._value if self._isInteger else None

    def getList(self):
        return self._value if not self._isInteger else None


class NestedIterator:
    def __init__(self, nestedList):
        # ✅ Why reverse the list?
        # To process left-to-right using a LIFO stack.
        # e.g. [1,[4,[6]]] becomes stack: [[4,[6]], 1]
        self.stack = nestedList[::-1]

    def next(self):
        # ✅ Assumes hasNext() already made sure the top is an integer.
        return self.stack.pop().getInteger()

    def hasNext(self):
        # ✅ Why flatten in hasNext() and not next()?
        # next() should return immediately.
        # hasNext() is expected to prepare the stack.
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True

            # ✅ Flatten one layer
            # ✅ If the top is a nested list, we pop and expand it.
            # We push its elements onto the stack in reverse order so they come out left-to-right.
            self.stack.pop()
            self.stack.extend(reversed(top.getList()))
        return False