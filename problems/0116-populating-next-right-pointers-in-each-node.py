# LeetCode 116 - Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# ✅ Problem:
# Given a perfect binary tree, connect each node’s next pointer to its right neighbor.
# If there is no right neighbor, set `.next = None`.

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