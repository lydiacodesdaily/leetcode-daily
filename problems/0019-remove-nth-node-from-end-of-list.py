# LeetCode 19 - Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# ✅ Problem:
# Given the head of a linked list, remove the nth node from the end and return the head.

# 📚 Pattern:
# Two Pointers (Fast & Slow) + Dummy Node

# 🔍 Core Idea:
# Use a dummy node before the head to simplify edge cases.
# Move `fast` pointer n steps ahead, then move both `fast` and `slow` until `fast` hits end.
# `slow` will be right **before** the node to remove.

# 🧠 Memory Hook:
# dummy before head → handles removing head case  
# fast moves n ahead → then move both  
# when fast hits None → slow before target  
# slow.next = slow.next.next

# ✅ Time Complexity: O(n) – one pass through list
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Forgetting to use dummy to handle removing head node
# - Off-by-one when advancing `fast` n steps

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Step 1: Add dummy node
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Step 2: Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Step 3: Move both until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Step 4: Remove nth node
        slow.next = slow.next.next

        return dummy.next

# 🔄 Dry Run:
# Input: head = [1,2,3,4,5], n = 2
# After dummy: [0,1,2,3,4,5]
# fast moves to 3, slow at 0
# both move until fast hits None
# slow at 3 → skip next → result = [1,2,3,5]