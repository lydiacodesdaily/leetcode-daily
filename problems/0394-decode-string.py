# LeetCode 394 - Decode String
# https://leetcode.com/problems/decode-string/

# ✅ Problem:
# Given an encoded string, return its decoded version.
# Rules: k[encoded_string] means repeat encoded_string k times.
# Nested encodings like "3[a2[c]]" are allowed.

# 📚 Pattern: Stack
# 🧩 Subtype: Bracketed Nested Repetition Parsing

# 🧠 Memory Hook:
# - Use (prev_str, repeat) stack snapshot on '['
# - On ']', repeat current string and append to prev
# - Multi-digit repeat counts → curr_num = curr_num * 10 + int(char)

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n) for stack and intermediate strings

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []        # 🧳 stack holds (prev_str, repeat_count)
        curr_str = ""     # 🧱 current working string being built
        curr_num = 0      # 🔢 repeat count accumulator

        # 🚶 Step through each character
        for char in s:
            if char.isdigit():
                # 🔢 Build multi-digit numbers (e.g., "12[ab]")
                curr_num = curr_num * 10 + int(char)

            elif char == '[':
                # 🧳 Push current string and repeat count to stack
                stack.append((curr_str, curr_num))
                # 🧼 Reset for substring inside brackets
                curr_str = ""
                curr_num = 0

            elif char == ']':
                # 📤 Pop last state and apply repeat logic
                prev_str, repeat = stack.pop()
                # 🧱 Append repeated current block to previous
                curr_str = prev_str + curr_str * repeat

            else:
                # 🔤 Append character to current working string
                curr_str += char

        return curr_str


# 🔄 Dry Run: Input → "3[a2[c]]"
# Step-by-step:
# → char='3' → curr_num = 3
# → char='[' → push ("", 3), reset curr_str
# → char='a' → curr_str = "a"
# → char='2' → curr_num = 2
# → char='[' → push ("a", 2), reset curr_str
# → char='c' → curr_str = "c"
# → char=']' → pop → prev="a", num=2 → curr_str = "a" + "c"*2 = "acc"
# → char=']' → pop → prev="", num=3 → curr_str = "" + "acc"*3 = "accaccacc"
# ✅ Output: "accaccacc"