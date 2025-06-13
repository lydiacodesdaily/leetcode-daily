# 23. Merge K Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

"""
🧠 Pattern: Heap (Min Heap) / K-way Merge
🎯 Problem: Merge k sorted linked lists into one sorted list
📌 Use Cases:
- Merging K sorted streams of data
- Combining sorted logs or files

⏰ Time Complexity: O(N log k)
   - N = total number of nodes
   - k = number of linked lists
📦 Space Complexity: O(k)
   - For the min heap (at most one node per list)
"""

from typing import List, Optional, Tuple
import heapq

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val} -> {self.next}"

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Dummy head to simplify node merging
    dummy = ListNode()
    curr = dummy

    # Min-heap to store (node value, list index, node)
    min_heap: List[Tuple[int, int, ListNode]] = []

    # Step 1: Initialize the heap with the first node from each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))

    # Step 2: Extract min node and push its next node into the heap
    # Dry run input example:
    # lists = [
    #     1 -> 4 -> 5,
    #     1 -> 3 -> 4,
    #     2 -> 6
    # ]
    # Initial heap after pushing heads:
    # heap = [(1, 0, node_0), (1, 1, node_1), (2, 2, node_2)]

    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        curr.next = node  # Append to result list
        curr = curr.next  # Move pointer forward

        # Push the next node from the same list, if exists
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next

# Final output for the dry run example:
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

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