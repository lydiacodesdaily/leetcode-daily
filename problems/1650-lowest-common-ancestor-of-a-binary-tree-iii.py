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

# Option A: Set-Based Approach 
# ⏱️ Time: O(h), 📦 Space: O(h)
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()
        while p:
            seen.add(p)
            p = p.parent
        while q:
            if q in seen:
                return q
            q = q.parent
        return None
    
# Option B: Two Pointers ** preferred
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q
        
        # Traverse up until both meet — either at LCA or both None
        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
        
        return a

# Dry Run Example for LCA with Parent Pointers

# Tree Structure:
#         T
#        / \
#       U   V
#      /   / \
#     W   X   Y
#        /
#       Z

# Parent relationships:
# W.parent = U
# U.parent = T
# Z.parent = X
# X.parent = V
# V.parent = T

# Inputs:
# p = W
# q = Z

# Two-pointer initialization:
# a = W
# b = Z

# Step-by-step traversal:
# Step 1: a = W       | b = Z
# Step 2: a = U       | b = X
# Step 3: a = T       | b = V
# Step 4: a = None    | b = T
# Step 5: a = Z (switch to q) | b = None
# Step 6: a = X       | b = W (switch to p)
# Step 7: a = V       | b = U
# Step 8: a = T       | b = T  ✅

# Result:
# a == b == T → This is the Lowest Common Ancestor (LCA)

# ✅ This two-pointer technique works like finding the intersection of two linked lists:
# Both pointers traverse p's path + q's path, ensuring equal steps before meeting at LCA.