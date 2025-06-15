# LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

# ✅ Problem:
# You are given two nodes `p` and `q` of a binary tree (NOT necessarily rooted),
# where each node has a `.parent` pointer.
# Return their **lowest common ancestor (LCA)**.

# 🔍 Key Insight:
# This is like finding the **intersection of two linked lists** starting from `p` and `q` going upward via `.parent`.

# ✅ Time Complexity: O(h) — where h is the height of the tree
# ✅ Space Complexity: O(1) — no extra data structures

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q
        
        # Traverse up until both meet — either at LCA or both None
        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
        
        return a