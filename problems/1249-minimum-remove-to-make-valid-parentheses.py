# LeetCode 1249 - Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# ✅ Problem:
# Given a string s of '(' , ')' and lowercase letters,
# remove the minimum number of parentheses to make the string valid.
# Return the resulting string.

# 📚 Pattern:
# Stack + Greedy Cleanup (Mark-and-Skip Strategy)

# 🔍 Core Idea:
# Use a stack to track unmatched '(' indices.
# In first pass, mark all invalid ')' and unmatched '('.
# In second pass, skip the marked characters to rebuild the valid string.

# 🧠 Memory Hook:
# 1st pass: push index of '(' to stack  
# if ')' → pop if stack not empty else mark for removal  
# add unmatched '(' indices to remove  
# 2nd pass: rebuild string, skip marked indices

# ✅ Time Complexity: O(n) - one pass to mark, one pass to build
# ✅ Space Complexity: O(n) - for stack and set of indices to remove

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []          # Track indices of unmatched '('
        remove = set()      # Indices to remove

        # First pass: mark indices to remove
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()  # matched
                else:
                    remove.add(i)  # unmatched ')'

        # Add unmatched '(' indices
        remove.update(stack)

        # Second pass: rebuild result skipping invalid indices
        result = []
        for i, char in enumerate(s):
            if i not in remove:
                result.append(char)

        return ''.join(result)

# 🔄 Dry Run:
# Input: s = "a)b(c)d"
# Pass 1: 
#   i=0, 'a' → skip
#   i=1, ')' → no matching '(' → mark 1
#   i=2, 'b'
#   i=3, '(' → stack = [3]
#   i=4, 'c'
#   i=5, ')' → match with '(', pop stack
#   i=6, 'd'
# Remove = {1}, stack empty
# Final result = "ab(c)d"

# Another example:
# Input: "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Remove only the unmatched ')' at the end
