# LeetCode 708 - Insert into a Sorted Circular Linked List
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

# ✅ Problem:
# Insert a value into a sorted circular linked list so that the list remains sorted.
# The list may start at any node and can be empty.

# 📚 Pattern:
# Linked List Insertion with Circular Traversal

# 🔍 Core Idea:
# - Traverse the circular list to find the correct insertion point.
# - Handle 3 cases:
#   1. Normal insert: insertVal fits between current and next node.
#   2. Insert at wrap-around point (from max to min).
#   3. All nodes have the same value or full loop without finding a spot → insert anywhere.

# 🧠 Memory Hook:
# Traverse circularly → find node where curr.val <= insertVal <= curr.next.val
# At max → min wrap → insert if insertVal is smallest or largest.
# If full loop → insert anywhere.

# ✅ Time Complexity: O(n) in the worst case (single traversal)
# ✅ Space Complexity: O(1)

class Node:
    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal)

        # Case 0: Empty list → create new circular list
        if not head:
            new_node.next = new_node
            return new_node

        curr = head
        while True:
            # Case 1: Normal insert between two nodes
            if curr.val <= insertVal <= curr.next.val:
                break

            # Case 2: At the maximum → minimum wrap-around point
            if curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    break

            # Case 3: Full loop without finding spot → insert anywhere
            if curr.next == head:
                break

            curr = curr.next

        # Insert new_node between curr and curr.next
        new_node.next = curr.next
        curr.next = new_node

        return head

# 🔄 Dry Run Example:
# Input: head = [3, 4, 1] (circular), insertVal = 2
# Step 1: Traverse → 3 → 4 → 1 → wrap-around detected → 2 fits between 1 and 3
# Step 2: Insert 2 between 1 and 3 → return head

# 📌 Common Gotchas:
# - Handling empty list correctly → must create a self-loop.
# - Carefully handle wrap-around point → where current node is larger than next node.
# - Full loop → ensure insertion happens even if all nodes have same value or no valid slot is found.