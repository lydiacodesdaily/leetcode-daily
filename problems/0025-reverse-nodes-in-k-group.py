# LeetCode 25 - Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# ✅ Problem:
# Given a singly linked list, reverse nodes in groups of size k.
# If the number of nodes left is < k, leave them as-is.

# 📚 Pattern:
# Linked List — Reverse in chunks (in-place pointer manipulation)

# 🔍 Core Idea:
# Reverse k nodes at a time by:
#   1️⃣ Locating k nodes ahead (to ensure enough nodes to reverse)
#   2️⃣ Running an in-place reversal between boundaries
#   3️⃣ Reconnecting the reversed chunk back into the list
#   4️⃣ Moving prev pointer forward to next group

# 🧠 Memory Hook:
# - "find kth → reverse inside boundaries → reconnect → move prev"
# - previous = next_group_start is the trick that cleanly ends reversal
# - stop when kth_node is None

# ⏱️ Time Complexity: O(n)
# 🧵 Space Complexity: O(1)

from typing import Optional

# Definition of a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Reverse nodes in groups of size k.
    If remaining nodes < k, leave them unchanged.
    """

    # --------------------------------------------
    # 0. Setup dummy node to simplify head handling
    # --------------------------------------------
    dummy_head = ListNode(0)
    dummy_head.next = head

    # The "prev" pointer before the current k-group
    current_group_prev = dummy_head

    # ---------------------------------------------------------
    # Main loop: process group by group until fewer than k left
    # ---------------------------------------------------------
    while True:

        # -----------------------------------------------
        # 1. Find kth node ahead (to confirm full k group)
        #    If not enough nodes → break
        # -----------------------------------------------
        kth_node = get_kth_node(current_group_prev, k)
        if not kth_node:
            break

        # Store start of next group (k+1-th node)
        next_group_start = kth_node.next

        # ---------------------------------------------------------
        # 2. Reverse nodes between:
        #       current_group_prev.next  -->  kth_node
        #    Use "previous = next_group_start" trick as boundary
        # ---------------------------------------------------------
        previous = next_group_start
        current = current_group_prev.next

        # Reverse the k nodes
        while current != next_group_start:
            temp_next = current.next
            current.next = previous
            previous = current
            current = temp_next

        # ---------------------------------------------------------
        # 3. Reconnect the reversed group back into the main list
        #    previous = kth_node after reversal
        # ---------------------------------------------------------
        temp_start = current_group_prev.next     # original start of group
        current_group_prev.next = kth_node       # new start
        current_group_prev = temp_start          # move pointer forward

    return dummy_head.next


def get_kth_node(current: ListNode, k: int) -> Optional[ListNode]:
    """
    Helper: return the kth node starting from 'current'.
    Return None if fewer than k nodes remain.
    """
    while current and k > 0:
        current = current.next
        k -= 1
    return current


# ---------------------------------------------------------
# Example usage:
# l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(4)
# l1.next.next.next.next = ListNode(5)
# result = reverseKGroup(l1, 2)   # Output: 2 -> 1 -> 4 -> 3 -> 5
# ---------------------------------------------------------