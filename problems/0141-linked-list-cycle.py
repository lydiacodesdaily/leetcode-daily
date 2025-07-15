# LeetCode 141 - Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

# ✅ Problem:
# Given the head of a linked list, determine if the linked list has a cycle in it.

# 🧩 Pattern:
# Fast & Slow Pointers (Floyd’s Cycle Detection)

# 🔍 Key Insight:
# If there's a cycle, a fast pointer moving 2x speed will eventually meet the slow pointer.

# 🧠 Memory Hook:
# slow = 1x, fast = 2x
# if there's a loop, fast will "lap" slow → they meet
# if fast hits None → no cycle

# ✅ Time Complexity: O(n) — worst case traverses every node once
# ✅ Space Complexity: O(1) — two pointers, no extra memory

# 📌 Common Gotchas:
# - Forgetting to check fast and fast.next in while loop
# - Confusing cycle detection vs cycle start problems (this is just detection)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Step 1: Initialize slow and fast pointers
        slow = head
        fast = head

        # Step 2: Traverse with two pointers at different speeds
        while fast and fast.next:
            slow = slow.next          # move 1 step
            fast = fast.next.next     # move 2 steps

            # Step 3: If they meet, there's a cycle
            if slow == fast:
                return True

        # Step 4: If fast reaches end, no cycle
        return False


# 🔄 Dry Run:
# Input: head = 3 → 2 → 0 → -4
#                   ⬑--------⬋  (tail connects to node index 1)
# slow: 3 → 2 → 0 → -4 → 2 ...
# fast: 3 → 0 → 2 → -4 → 0 ...
# Eventually: slow == fast at node 2 → cycle exists → return True