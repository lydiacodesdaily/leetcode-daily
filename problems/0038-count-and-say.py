# LeetCode 38 - Count and Say
# https://leetcode.com/problems/count-and-say/
#
# ✅ Problem:
# The "count-and-say" sequence is a sequence of digit strings defined as:
#  - Term 1 is "1".
#  - Each subsequent term describes the previous term.
#
# Given an integer n, return the n-th term of the sequence.
#
# Example:
# n = 4 → "1211"
# Term 1: "1"
# Term 2: "11"   (one 1)
# Term 3: "21"   (two 1s)
# Term 4: "1211" (one 2, then one 1)
#
# 📚 Pattern:
# String Construction / Run-Length Encoding
#
# 🔍 Core Idea:
# - Start with base case "1" (term 1).
# - For each step, scan the current string:
#   * Count consecutive identical digits.
#   * Append "<count><digit>" to the new string.
# - Repeat until reaching the n-th term.
#
# 🧠 Memory Hook:
# base = "1"
# build n-1 times → say count + digit
#
# ✅ Time Complexity: O(n * m), where m = length of the string at step n
# ✅ Space Complexity: O(m)
#
# 📌 Common Gotchas:
# - Loop runs n-1 times (because term 1 is given).
# - Don’t read beyond string → use condition `if i < len(result)` before accessing result[i].
# - Reset count when digits change.

class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: term 1
        result = "1"
        
        # 🔄 Build terms from 2 → n (n-1 iterations)
        for _ in range(n - 1):
            current = ""
            count = 1
            
            # 🧭 Scan current result
            for i in range(1, len(result) + 1):
                if i < len(result) and result[i] == result[i - 1]:
                    # Still same digit → increase count
                    count += 1
                else:
                    # Digit changed or end reached → append count + digit
                    current += str(count) + result[i - 1]
                    count = 1  # reset count
            
            # Move to next term
            result = current
        
        return result


# 🔄 Dry Run for n = 4:
# result = "1"
# Step 1 → "11"   (one 1)
# Step 2 → "21"   (two 1s)
# Step 3 → "1211" (one 2, one 1)
# Final answer = "1211"