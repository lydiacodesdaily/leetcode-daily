# Leetcode 19: Remove Nth Node From End of List
# --------------------------------------------------
# Problem:
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Time Complexity: O(L) where L is the length of the list
# Space Complexity: O(1)
#
# Strategy:
# Use a dummy node and two-pointer technique.
# Move fast pointer n + 1 steps ahead.
# Then move both fast and slow until fast reaches the end.
# Slow pointer will be just before the node to remove.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Create dummy node
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Step 2: Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Step 3: Move both pointers until fast reaches end
        while fast:
            slow = slow.next
            fast = fast.next

        # Step 4: Skip the target node
        slow.next = slow.next.next

        # Step 5: Return the new head (could be new if head was deleted)
        return dummy.next

# --------------------------------------------------
# 