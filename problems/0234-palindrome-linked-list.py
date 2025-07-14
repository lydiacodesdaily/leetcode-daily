# LeetCode 234 - Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# ✅ Problem:
# Check if a singly linked list is a palindrome.

# 📚 Pattern:
# Linked List + Reverse second half + Two pointer comparison

# 🔍 Key Insight:
# - Use slow and fast pointers to find the midpoint.
# - Reverse the second half of the list.
# - Compare first half and reversed second half.

# 🧠 Memory Hook:
# "Compare up to reversed half → stop at second!"
# - While-loop only needs "second", not both first/second
# - Handles odd-length lists correctly (middle element skipped)

# ✅ Time Complexity: O(n) — one pass to find mid, one pass to reverse, one to compare
# ✅ Space Complexity: O(1) — in-place reversal, no extra data structures

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # 🪜 Step 1: Find midpoint (slow ends at mid)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 🪜 Step 2: Reverse second half of the list
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # 🪜 Step 3: Compare values in first half and reversed second half
        first, second = head, prev
        while second:  # ✅ Only traverse second half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True

# 🔄 Dry Run Example:
# Input: 1 -> 2 -> 3 -> 2 -> 1
# Midpoint: slow at node 3
# Reversed second half: 1 -> 2 (from original tail)
# Compare: 1==1, 2==2 ✅ → return True
