# LeetCode 23 - Merge K Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# ✅ Problem:
# Merge k sorted linked lists and return it as one sorted list.

# 📚 Pattern:
# Heap / Priority Queue

# 🔍 Core Idea:
# Use a min-heap to always extract the smallest head among the lists.
# When popping a node, push its next into the heap (if available).

# 🧠 Memory Hook:
# use min-heap of (val, node)
# push head of each list
# pop smallest, append to result, push next of popped node

# ✅ Time Complexity: O(N log k)
# - N = total number of nodes across all lists
# - k = number of lists
# ✅ Space Complexity: O(k) - size of the heap

from typing import List, Optional
from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        # Define less-than for heapq to work correctly with ListNode
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Step 1: Push the head node of each list into heap
        for i, node in enumerate(lists):
            if node:
                heappush(min_heap, (node.val, i, node))  # index prevents comparison issues

        dummy = ListNode(0)
        current = dummy

        # Step 2: Pop the smallest node, attach to result, push its next
        while min_heap:
            val, i, node = heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next

"""
🧪 Example Input:
lists = [
    1 -> 4 -> 5,
    1 -> 3 -> 4,
    2 -> 6
]

Expected Output:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
"""