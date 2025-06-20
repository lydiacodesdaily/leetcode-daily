# LeetCode 921 - Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

# ✅ Problem:
# Given a parentheses string `s`, return the minimum number of parentheses insertions needed to make it valid.

# 📚 Pattern: Stack (or Greedy Counter)

# 🔍 Key Insight:
# - Track unmatched left and right parentheses using two counters:
#   - `open`: how many unmatched '(' we’ve seen
#   - `insertions`: how many unmatched ')' we’ve seen (i.e., we need '(' for them)

# ✅ Time Complexity: O(n) — one pass through string
# ✅ Space Complexity: O(1) — constant space (no stack needed)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0       # Count of unmatched '('
        insertions = 0 # Count of unmatched ')'

        for c in s:
            if c == '(':
                open += 1
            else: # c == ')'
                if open > 0:
                    open -= 1  # Match with previous '('
                else:
                    insertions += 1  # Need to insert a '('

        return open + insertions  # Remaining unmatched '(' + unmatched ')'

# 🔁 Dry Run:
# Input: s = "())"
# Step 1: '(' → open = 1
# Step 2: ')' → open = 0
# Step 3: ')' → insertions = 1 (no '(' left to match)
# Output: 1

# 📌 Common Gotchas:
# - Don't use an actual stack — a counter is more efficient.
# - Be careful to count unmatched right parens when `open == 0`

# 🧠 Concepts Reinforced:
# - Stack balancing with counters
# - Greedy match and repair strategy