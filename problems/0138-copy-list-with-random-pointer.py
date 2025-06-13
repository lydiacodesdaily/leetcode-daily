# LeetCode 138 – Copy List with Random Pointer
# ✅ HashMap-based approach for clarity and simplicity
# 🧠 Time Complexity: O(n) – we visit each node twice
# 📦 Space Complexity: O(n) – we store a mapping from original -> copied nodes
# 📌 Use Case: When correctness and clarity are prioritized, especially in early interview stages

from typing import Optional

class Node:
    def __init__(self, val: int = 0, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    # Edge case: empty list
    if not head:
        return None

    # Dictionary to map original nodes to their cloned versions
    original_to_clone = {None: None}

    # First pass: clone all nodes and build the mapping
    current = head
    while current:
        clone_node = Node(current.val)
        original_to_clone[current] = clone_node
        current = current.next

    # Second pass: assign next and random pointers
    current = head
    while current:
        clone = original_to_clone[current]
        clone.next = original_to_clone[current.next]
        clone.random = original_to_clone[current.random]
        current = current.next

    return original_to_clone[head]

# 🧪 Dry Run Example:
# Original: 7 → 13 → 11 → 10 → 1
# Random:    ↘    ↘    ↖    ↘
#           None   7   1   11
# After pass 1: cloned nodes created but not linked
# After pass 2: next and random pointers set using mapping
