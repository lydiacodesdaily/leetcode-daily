# LeetCode 2 - Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# ✅ Problem:
# Add two non-empty linked lists representing two non-negative integers.
# Digits are stored in reverse order (least significant digit at head).
# Return the sum as a linked list.

# 🔁 Pattern: Linked List + Carry Tracking
# 🧠 Key Idea: Use dummy node and simulate manual addition digit-by-digit
# ⏰ Time Complexity: O(max(m, n))
# 🧠 Space Complexity: O(max(m, n)) for output list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()      # Dummy node to simplify result list
    curr = dummy            # Pointer to build result
    carry = 0               # Initialize carry

    # Traverse both lists
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0  # Value from l1 or 0
        val2 = l2.val if l2 else 0  # Value from l2 or 0

        total = val1 + val2 + carry
        carry = total // 10         # Carry to next digit
        digit = total % 10          # Current digit

        curr.next = ListNode(digit) # Append digit to result
        curr = curr.next            # Move forward in result

        # Advance input list pointers
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

# --- 🧪 Dry Run Example ---
# l1 = 2 -> 4 -> 3 (represents 342)
# l2 = 5 -> 6 -> 4 (represents 465)
# Expected Output: 7 -> 0 -> 8 (342 + 465 = 807)
#
# Step-by-step:
#   total = 2 + 5 + 0 = 7  -> digit: 7, carry: 0
#   total = 4 + 6 + 0 = 10 -> digit: 0, carry: 1
#   total = 3 + 4 + 1 = 8  -> digit: 8, carry: 0
# Final output: 7 -> 0 -> 8
