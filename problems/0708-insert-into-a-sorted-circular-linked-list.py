# LeetCode 708 - Insert into a Sorted Circular Linked List
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

# ✅ Problem:
# Given a node from a sorted circular linked list, insert a value so the list remains sorted.
# Return any reference to the updated circular list.

# 🧩 Base Pattern:
# Circular Linked List Traversal
# - Use a `do-while` style traversal to loop at least once from the given node.
# - Insert the node when appropriate conditions are met.

# 🧪 Subtype:
# Insert into Sorted List with Wraparound
# - If value fits between two nodes normally → insert.
# - If at the "end-start boundary" (e.g., max → min) → insert if value is smallest or largest.
# - If all values are same → insert anywhere.

# 🧠 Memory Hook:
# traverse until:
#   1. insertVal fits between curr and next → curr.val ≤ insertVal ≤ next.val
#   2. at wrap point: curr > next → insert if insertVal is ≥ curr or ≤ next
#   3. full loop → insert anywhere
# always insert: newNode.next = curr.next; curr.next = newNode

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Forgetting to handle empty list (head is None)
# - Not accounting for edge transition between max and min (e.g. 4 → 1)
# - Infinite loop if you don't detect a full circle traversal

class Node:
    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        newNode = Node(insertVal)

        if not head:
            newNode.next = newNode  # single node circular
            return newNode

        curr = head
        while True:
            # Case 1: Normal insert between two values
            if curr.val <= insertVal <= curr.next.val:
                break

            # Case 2: At the wraparound point (max → min)
            if curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    break

            # Case 3: Full loop — insert anywhere
            if curr.next == head:
                break

            curr = curr.next

        # Insert the node
        newNode.next = curr.next
        curr.next = newNode
        return head

# 🔄 Dry Run:
# Input: head = [3 → 4 → 1 (→ back to 3)], insertVal = 2
# 1. 3 → 4 → 1 → 3: none satisfy condition 1
# 2. 4 > 1 → wraparound case → 2 lies between max and min → insert between 1 and 3
# Result: [3 → 4 → 1 → 2 → back to 3]

# Edge Case:
# Input: head = [], insertVal = 1
# → Create single node circular: [1]