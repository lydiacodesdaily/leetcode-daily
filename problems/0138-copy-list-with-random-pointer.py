# LeetCode 138 - Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/

# ✅ Problem:
# You're given a linked list where each node has two pointers: `next` and `random`.
# Create a deep copy of the list where every node is a completely new node,
# and both `next` and `random` pointers are correctly replicated.

# 📚 Pattern:
# Hash Map (original → clone)

# 🔍 Core Idea:
# First pass: clone each node and store mapping in a dictionary.
# Second pass: use that mapping to assign both `.next` and `.random` pointers.

# 🧠 Memory Hook:
# - build map {old: new}
# - clone.val = original.val
# - clone.next = map[original.next]
# - clone.random = map[original.random]

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)

# 📌 Common Gotchas:
# - Be sure to map `None → None` to avoid KeyErrors
# - Don't try to build next/random in one pass; two passes are cleaner and safer
# ✅ Why DFS/BFS is needed in other problems:
#	•	For problems like Clone Graph, the structure is non-linear and cyclic.
#	•	You need DFS or BFS to explore neighbors and avoid infinite loops.
#	•	The random pointers here don’t cause cycles in traversal — we don’t “walk” through them like edges in a graph. We just copy them once.

class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 🧱 Step 1: Create a mapping from original node → cloned node
        original_to_clone = {None: None}

        current = head
        while current:
            clone_node = Node(current.val)
            original_to_clone[current] = clone_node
            current = current.next

        # 🔗 Step 2: Assign next and random pointers using the map
        current = head
        while current:
            clone_node = original_to_clone[current]
            clone_node.next = original_to_clone[current.next]
            clone_node.random = original_to_clone[current.random]
            current = current.next

        return original_to_clone[head]

# 🔄 Dry Run:
# Input:
#   A -> B -> C
#   A.random = C
#   B.random = A
#   C.random = B

# Step 1: Map created:
#   { A: A', B: B', C: C', None: None }

# Step 2:
#   A'.next = B'
#   A'.random = C'
#   ...
#   Fully deep copied list is returned starting at A'

# Output:
#   A' -> B' -> C' with correct random links