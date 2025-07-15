# LeetCode 328 - Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# ✅ Problem:
# Rearrange a linked list so that all nodes at odd indices come before nodes at even indices.
# Maintain the relative order of both odd and even indexed nodes.

# 📚 Pattern:
# Linked List - Pointer Rearrangement

# 🔍 Key Insight:
# - Use two separate pointers for odd and even positions.
# - Keep track of the start of the even list (even_head) to reconnect later.

# 🧠 Memory Hook:
# odd, even = head, head.next
# even_head = even
# while even and even.next:
#     odd.next = even.next; odd = odd.next
#     even.next = odd.next; even = even.next
# odd.next = even_head

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Forgetting to reconnect odd list to even_head
# - Moving even pointer incorrectly

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 🪄 Step 1: Initialize odd, even and store even_head to reconnect later
        odd = head
        even = head.next
        even_head = even

        # 🔁 Step 2: Rearranging pointers in-place
        while even and even.next:
            odd.next = even.next      # Point odd to next odd node
            odd = odd.next            # Move odd pointer forward

            even.next = odd.next      # Point even to next even node
            even = even.next          # Move even pointer forward

        # 🔗 Step 3: Connect odd list to even list
        odd.next = even_head

        return head

# 🔄 Dry Run:
# Input: 1 -> 2 -> 3 -> 4 -> 5
# After rearranging:
# Odd list: 1 -> 3 -> 5
# Even list: 2 -> 4
# Final list: 1 -> 3 -> 5 -> 2 -> 4 ✅
