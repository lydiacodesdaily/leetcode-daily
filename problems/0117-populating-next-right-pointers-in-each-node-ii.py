# ======================================================
# Leetcode 116 - Populating Next Right Pointers in Each Node
# ======================================================
# ✅ Problem:
# - Perfect binary tree (all nodes have 2 children, all leaves on same level).
# - Fill `.next` pointers to point to the node's right neighbor.

# 📚 Pattern:
# BFS Level Traversal (no dummy/prev needed in perfect tree)

# 🔍 Key Insight:
# - Since it's perfect, curr.left and curr.right always exist.
# - And curr.next.left will always be the immediate neighbor of curr.right.

# 🧠 Memory Hook:
# "Link left → right, then right → neighbor's left"

class Solution116:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        leftmost = root
        while leftmost.left:                  # ⬅ Guaranteed to exist in perfect tree
            head = leftmost
            while head:
                head.left.next = head.right   # Link same parent
                if head.next:
                    head.right.next = head.next.left  # Link across parents
                head = head.next
            leftmost = leftmost.left
        return root


# ======================================================
# Leetcode 117 - Populating Next Right Pointers in Each Node II
# ======================================================
# ✅ Problem:
# - Not necessarily perfect; children can be missing.
# - Fill `.next` pointers to point to the node's right neighbor.

# 📚 Pattern:
# BFS Level Traversal with Dummy + Prev pointer for next level

# 🔍 Key Insight:
# - Can't hardcode left/right links like 116; must "chain together" existing children.
# - Use dummy/prev to stitch next-level nodes in left-to-right order as we go.

# 🧠 Memory Hook:
# "Dummy = start of next row, Prev = tail; attach kids as we find them"

class Solution117:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        curr = root
        while curr:
            dummy = Node(0)     # imaginary head of next level
            prev = dummy        # tail pointer for next level
            
            while curr:         # loop through current level
                if curr.left:   # if left child exists → attach to tail
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:  # if right child exists → attach to tail
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next  # move to next node in current level
            
            curr = dummy.next    # move down to first node of next level
        
        return root

# ======================================================
# 💡 Difference Summary:
# 116:
# - Tree is perfect → direct links between left/right and across parents.
# - No dummy/prev needed because children always exist.
#
# 117:
# - Tree can be irregular → can't assume neighbors exist.
# - Use dummy/prev to collect all next-level children in order.
# - prev.next = curr.left/right is literally "add this child to the end of the kid line".

# ======================================================
# Dry Run for 117 — Irregular Tree Example
# ======================================================
#
# Tree:
#         1
#       /   \
#      2     3
#       \     \
#        5     7
#
# Expected `.next` connections:
# Level 1: 1 -> None
# Level 2: 2 -> 3 -> None
# Level 3: 5 -> 7 -> None
#
# Step-by-step:
#
# curr = 1
# dummy = Node(0), prev = dummy
#
# --- Visiting 1 ---
# curr.left = 2 → prev.next = 2, prev = 2
# curr.right = 3 → prev.next = 3, prev = 3
# curr = curr.next → None
#
# Move down:
# curr = dummy.next (2)
#
# --- Visiting level 2 ---
# dummy = Node(0), prev = dummy
#
# curr = 2:
# curr.left = None → skip
# curr.right = 5 → prev.next = 5, prev = 5
# curr = curr.next (3)
#
# curr = 3:
# curr.left = None → skip
# curr.right = 7 → prev.next = 7, prev = 7
# curr = curr.next → None
#
# Move down:
# curr = dummy.next (5)
#
# --- Visiting level 3 ---
# dummy = Node(0), prev = dummy
#
# curr = 5:
# no children → skip
# curr = curr.next (7)
#
# curr = 7:
# no children → skip
# curr = curr.next → None
#
# Move down:
# curr = dummy.next → None → End
#
# Final links:
# 1 -> None
# 2 -> 3 -> None
# 5 -> 7 -> None