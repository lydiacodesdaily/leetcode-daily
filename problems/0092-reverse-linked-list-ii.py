# LeetCode 92 - Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

# ✅ Problem:
# Reverse a portion of a singly linked list from position `left` to `right` (1-indexed), in-place.

# 📚 Pattern:
# Linked List - In-Place Sublist Reversal (Pointer Dance)

# 🔍 Key Insight:
# Instead of reversing the whole list, we:
# 1. Move `prev` to node before position `left`
# 2. Use a front-insertion loop to reverse nodes between `left` and `right`

# 🧠 Memory Hook:
# dummy → prev = left - 1
# curr = prev.next
# repeat (right - left) times:
#     temp = curr.next
#     curr.next = temp.next
#     temp.next = prev.next
#     prev.next = temp

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Misunderstanding 1-indexing: `left = 1` means head changes — dummy handles this
# - Forgetting to use `dummy` for safe head manipulation
# - Mistaking `temp.next = curr` instead of `prev.next`

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 🧱 Step 0: Setup dummy node to simplify edge cases
        dummy = ListNode(0, head)
        prev = dummy

        # 🚶 Step 1: Move prev to node before `left`
        for _ in range(left - 1):
            prev = prev.next

        # 🎯 Step 2: Reverse the sublist from left to right using front-insertion
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next           # Node to be moved
            curr.next = temp.next      # Remove temp from its position
            temp.next = prev.next      # Link temp before curr
            prev.next = temp           # Move temp to front of sublist

        return dummy.next

# 🔄 Dry Run:
# Input: head = 1→2→3→4→5, left = 2, right = 4
# prev = 1
# curr = 2
# Iteration 1: pull 3 to front → 1→3→2→4→5
# Iteration 2: pull 4 to front → 1→4→3→2→5 ✅