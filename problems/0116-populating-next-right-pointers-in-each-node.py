# LeetCode 116 - Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# ✅ Problem:
# Given a perfect binary tree, populate each node's `next` pointer to point to its
# right neighbor on the same level. If no neighbor exists, set `next = None`.

# 📚 Pattern:
# Tree Traversal with Constant Space using Next Pointers

# 🔍 Key Insight:
# - Use the perfect binary tree structure to connect children top-down.
# - Connect:
#     1. left → right (within the same parent)
#     2. right → next.left (across neighboring parents)
# - Traverse level by level using already established `next` pointers.

# 🧠 Memory Hook:
# node.left.next = node.right
# node.right.next = node.next.left  # only if node.next exists
# No queue needed — O(1) space

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1) extra space (excluding recursion stack)

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # 🧭 Start at the leftmost node of the current level
        leftmost = root

        # Keep going until we reach the leaf level
        while leftmost.left:
            head = leftmost
            while head:
                # 1️⃣ Connect left → right (same parent)
                head.left.next = head.right

                # 2️⃣ Connect right → next.left (across neighboring parents)
                if head.next:
                    head.right.next = head.next.left

                # 🏃 Move to next node on the current level
                head = head.next

            # ⬇ Move to the leftmost node of the next level
            leftmost = leftmost.left

        return root

# Version II: 

# 📚 Pattern: Binary Tree BFS - Level Order Traversal

# 🔍 Key Insight:
# Use queue to traverse the tree level by level.
# For each level, connect node[i].next = node[i+1]
# Last node in each level → .next = None (default)

# 🧠 Memory Hook:
# BFS → queue of levels
# node.next = queue[0] within level
# return root after mutation

# ✅ Time: O(n) — each node visited once
# ✅ Space: O(n) — worst case queue holds n/2 nodes at the bottom level

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        from collections import deque
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # Connect to the next node in queue if not the last node in level
                if i < level_size - 1:
                    node.next = queue[0]
                
                # Enqueue child nodes
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root