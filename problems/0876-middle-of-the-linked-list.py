# LeetCode 876 - Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

# ✅ Problem:
# Given the head of a singly linked list, return the middle node of the list.
# If there are two middle nodes, return the second middle node.

# 📚 Pattern: Fast & Slow Pointers
# - Use two pointers moving at different speeds.
# - When fast reaches the end, slow will be at the middle.

# 🔍 Core Idea:
# Fast moves 2 steps, slow moves 1 step.
# When fast reaches None → slow = middle.

# 🧠 Memory Hook:
# fast = 2x speed
# slow = 1x speed
# return slow

# ✅ Time Complexity: O(n) → one traversal
# ✅ Space Complexity: O(1) → constant extra space

# 📌 Common Gotchas:
# - Return the **second middle** when length is even.
#   (Handled automatically since fast pointer ends first)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 🪢 Initialize fast and slow at head
        slow = fast = head 
        
        # 🚀 Move fast 2 steps and slow 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 🎯 Slow is now at the middle
        return slow


# 🔄 Dry Run:
# Input: [1,2,3,4,5]
# Iterations:
# - Step1: slow=2, fast=3
# - Step2: slow=3, fast=5
# - Step3: fast=None → stop → return slow=3
# Output: 3 ✅
#
# Input: [1,2,3,4,5,6]
# Iterations:
# - Step1: slow=2, fast=3
# - Step2: slow=3, fast=5
# - Step3: slow=4, fast=None → stop → return slow=4
# Output: 4 ✅