# LeetCode 2 - Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# ✅ Problem:
# Add two numbers represented as linked lists where each node contains a single digit.
# Digits are stored in reverse order.
# Return the sum as a new linked list.

# 📚 Pattern:
# Linked List + Elementary Math

# 🔍 Core Idea:
# Traverse both lists while tracking the carry.
# Add corresponding digits and carry, store new digit in result node.
# Continue until both lists and carry are exhausted.

# 🧠 Memory Hook:
# dummy head → result builder  
# loop while l1 or l2 or carry  
# val = l1 + l2 + carry → node = val % 10, carry = val // 10

# ✅ Time Complexity: O(max(m, n))
# ✅ Space Complexity: O(max(m, n)) for result list

# 📌 Common Gotchas:
# - Handling different lengths (check if node exists before accessing val)
# - Remembering to handle final carry (e.g., 5 + 5 = 10)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Dummy node to simplify result list construction
        dummy = ListNode()
        current = dummy
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Safe access
            val2 = l2.val if l2 else 0

            # Add values and carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry
            current.next = ListNode(total % 10)  # Create new node with digit

            # Move pointers
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

# 🔄 Dry Run:
# l1 = [2,4,3], l2 = [5,6,4] → represents 342 + 465
# Iteration 1: 2+5=7 → node=7, carry=0
# Iteration 2: 4+6=10 → node=0, carry=1
# Iteration 3: 3+4+1=8 → node=8
# Output: [7,0,8] (807)