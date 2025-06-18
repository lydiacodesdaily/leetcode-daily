# LeetCode 415 - Add Strings
# https://leetcode.com/problems/add-strings/

# ✅ Problem:
# Given two non-negative integers num1 and num2 represented as strings,
# return their sum also as a string.
# You must not use any built-in BigInteger library or convert the inputs directly to integers.

# 📚 Pattern:
# Two Pointers (simulate addition from end)

# 🔍 Key Insight:
# Add digits from the back using two pointers (like elementary school addition).
# Track carry, build result string in reverse.

# 🧠 Memory Hook:
# two pointers → end of both strings
# add digit1 + digit2 + carry
# result digit = total % 10
# carry = total // 10
# build in reverse

# ✅ Time Complexity: O(max(n1, n2))
# ✅ Space Complexity: O(max(n1, n2)) — for result storage

# 📌 Common Gotchas:
# - Don’t forget to handle leftover carry at the end
# - Reverse result before returning (since we add from least to most significant)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        # ➕ Simulate digit-by-digit addition from right to left
        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            total = n1 + n2 + carry

            result.append(str(total % 10))  # Store result digit
            carry = total // 10             # Update carry

            i -= 1
            j -= 1

        # 🔁 Digits were added in reverse, so reverse the result list
        return ''.join(reversed(result))

# 🔄 Example Dry Run:
# num1 = "456", num2 = "77"
#     4 5 6
# +     7 7
# ---------
#     5 3 3  → Output: "533"