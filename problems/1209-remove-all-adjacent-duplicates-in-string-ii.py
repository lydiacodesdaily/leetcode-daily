# LeetCode 1209 - Remove All Adjacent Duplicates in String II
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

# ✅ Problem:
# Given a string s and an integer k, remove all k adjacent duplicates in s
# repeatedly until no more adjacent k duplicates can be removed.

# 📚 Pattern: Stack
# Track (char, count). If count == k, pop the element.

# 🔍 Key Insight:
# Use a stack to count consecutive characters. When a count reaches k, remove it.
# Rebuild final string from the stack.

# 🧠 Memory Hook:
# stack = [(char, count)]
# if stack[-1][0] == ch → increment count
# if count == k → pop
# join char * count to build result

# ✅ Time Complexity: O(n) — one pass through string
# ✅ Space Complexity: O(n) — stack stores up to n characters in worst case

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # (char, frequency)

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()  # remove when k duplicates found
            else:
                stack.append([ch, 1])  # push as [char, count]

        # Rebuild final string
        return ''.join(char * count for char, count in stack)

# 🔄 Dry Run:
# Input: s = "deeedbbcccbdaa", k = 3
# Stack step-by-step:
# → [d,1]
# → [d,1],[e,1]
# → [d,1],[e,2]
# → [d,1],[e,3] → pop
# → [d,1]
# → d again → [d,2]
# → b → [d,2],[b,1]
# → b again → [d,2],[b,2]
# → c → [d,2],[b,2],[c,1]
# → c → [d,2],[b,2],[c,2]
# → c → [d,2],[b,2],[c,3] → pop
# → [d,2],[b,2]
# → b → [d,2],[b,3] → pop
# → [d,2]
# → d → [d,3] → pop
# → []
# → a → [a,1]
# → a → [a,2]
# Final → "aa"

# ✅ Output: "aa"

# 🔁 Follow-Up:
# If k = 1 → remove every character as soon as it appears
# If k > len(s) → return s untouched
