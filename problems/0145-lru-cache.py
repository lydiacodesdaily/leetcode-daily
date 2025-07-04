# LeetCode 146 - LRU Cache
# https://leetcode.com/problems/lru-cache/

# ✅ Problem:
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# ✅ Time Complexity:
# - get: O(1)
# - put: O(1)

# ✅ Space Complexity: O(capacity)

# ------------------------------------------------------------
# VERSION 1: OrderedDict (Python built-in)
# OrderedDict ordering: LEFT = LRU, RIGHT = MRU
# move_to_end(key) → move to most recent (right)
# popitem(last=False) → remove least recent (left)

from collections import OrderedDict

class LRUCacheOrderedDict:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # move to end to mark as most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            # pop the least recently used item
            self.cache.popitem(last=False)

# ------------------------------------------------------------
# VERSION 2: Doubly Linked List + Hash Map
# Manual design:
# head = MRU (most recent)
# tail = LRU (least recent)

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCacheManual:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Dummy head and tail for easy node management
        self.head = Node(0, 0)  # MRU side
        self.tail = Node(0, 0)  # LRU side
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper: Add node right after head (most recent position)
    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    # Helper: Remove node from linked list
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move node to most recent position
        self._remove(node)
        self._add(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to front
            self._remove(self.cache[key])

        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # Remove least recently used node from tail
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

# ------------------------------------------------------------
# 📝 Design Explanation:
# In OrderedDict version:
#   LEFT side = LRU, RIGHT side = MRU
#   move_to_end → makes item MRU
#   popitem(last=False) → removes LRU from LEFT

# In Manual Linked List version:
#   HEAD = MRU, TAIL = LRU
#   _add → always add after head (most recent)
#   _remove → remove from any position
#   Remove from tail when over capacity (least recent)

# 🔑 Big Takeaway:
# Both versions are correct because each consistently applies its own "direction" rule.
# OrderedDict: Python's convention is LEFT = old, RIGHT = new.
# Linked List: Custom convention is HEAD = new, TAIL = old.