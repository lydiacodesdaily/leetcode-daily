# LeetCode 21 - Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# ✅ Problem:
# Merge two sorted linked lists into one sorted list and return its head.
# The new list should be made by splicing together the nodes of the first two lists.

# 📚 Pattern:
# Linked List – Two Pointers with Dummy Node

# 🔍 Key Insight:
# - Use a dummy node to simplify edge cases.
# - Walk through both lists with two pointers.
# - At each step, connect the smaller node to the result list.

# 🧠 Memory Hook:
# "Dummy + current pointer"
# - compare l1.val vs l2.val
# - attach smaller one to current.next
# - move pointer forward
# - finally, attach leftover (only one list may remain)

# ✅ Time Complexity: O(n + m) – total number of nodes in both lists
# ✅ Space Complexity: O(1) – in-place merging

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 🧱 Create a dummy head to simplify edge cases
        dummy = ListNode()
        current = dummy

        # 🧭 Traverse both lists and connect nodes in sorted order
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # 🧩 At most one of l1 and l2 is non-empty now
        current.next = l1 if l1 else l2

        # 🎯 Return the head of the merged list
        return dummy.next