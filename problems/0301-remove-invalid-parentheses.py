# LeetCode 301 - Remove Invalid Parentheses
# https://leetcode.com/problems/remove-invalid-parentheses/

# ✅ Problem:
# Remove the minimum number of invalid parentheses in order to make the input string valid.
# Return all possible results. You may return the answer in any order.

# 🧩 Base Pattern:
# Breadth-First Search (BFS) – Level-wise generation of states
# Try all possible removals by deleting one character at a time.

# 🧪 Subtype:
# String State Search via BFS + Set for pruning duplicates

# 🧠 Memory Hook:
# - BFS to guarantee min removal
# - Visited set to skip repeats
# - Check valid at each level
# - Return early when valid found

# ✅ Time Complexity: O(n * 2^n)
# ✅ Space Complexity: O(n * 2^n)

from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Check if a string has valid parentheses
        def is_valid(expr):
            count = 0
            for c in expr:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        res = []
        visited = set()
        queue = deque()
        
        queue.append(s)
        visited.add(s)
        found = False

        while queue:
            curr = queue.popleft()

            if is_valid(curr):
                res.append(curr)
                found = True

            if found:
                continue  # Don't generate more strings once we've found valid ones at current level

            for i in range(len(curr)):
                if curr[i] not in '()':
                    continue
                next_str = curr[:i] + curr[i+1:]
                if next_str not in visited:
                    queue.append(next_str)
                    visited.add(next_str)

        return res

# 🔄 Dry Run:
# Input: "()())()"
# Level 0: "()())()" → invalid
# Level 1: remove one paren → ["())()", "()()()", "()()))", etc]
# Valid ones at this level: ["()()()", "(())()"]
# Stop BFS here since we found valid expressions with min removals

# 📌 Gotchas:
# - Don’t continue BFS once valid expressions are found at a level
# - Need to skip non-parenthesis characters during deletion
# - Use visited set to prevent repeat processing