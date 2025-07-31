# LeetCode 146 - LRU Cache
# https://leetcode.com/problems/lru-cache/

# ✅ Problem:
# Design a data structure that supports:
# - get(key): return value if key exists, else -1
# - put(key, value): update or insert key-value
# When cache exceeds capacity, evict the least recently used (LRU) item.

# 📚 Pattern:
# Hash Map + Doubly Linked List

# 🔍 Core Idea:
# 1. _remove(node)        → unlink node from list
# 2. _insert_to_front(node) → insert node right after head
# 3. get(key)             → lookup + move node to front
# 4. put(key, val)        → remove if exists, insert new to front, evict tail if needed
# Use a combination of:
# - HashMap (key -> node) for O(1) access
# - Doubly Linked List to track usage order (most recent at head, least recent at tail)

# 🧠 Memory Hook:
# hashmap for fast access
# doubly linked list to track order
# move to front on get/put
# evict from tail when full

# ✅ Time Complexity:
# - get: O(1)
# - put: O(1)

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail nodes to simplify edge operations
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # 🔄 Remove node from its current position
    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # 🔼 Insert node right after head (most recent position)
    def _insert_to_front(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 🔍 Get operation
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert_to_front(node)
            return node.value
        return -1

    # ➕ Put operation
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node first
            self._remove(self.cache[key])

        node = Node(key, value)
        self._insert_to_front(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # Remove from tail (least recently used)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

