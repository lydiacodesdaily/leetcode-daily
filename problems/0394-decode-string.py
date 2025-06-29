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
        stack = []        # 🧳 Stack → suitcase storage room (each holds (prev_str, repeat_count))
        curr_str = ""     # 📦 Current working space (what you're building now)
        curr_num = 0      # 🔢 Label for how many times to repeat (repeat count)

        # 🚶 Step through each character
        for char in s:
            if char.isdigit():
                # 🔢 Labeling the suitcase → build multi-digit repeat count
                curr_num = curr_num * 10 + int(char)

            elif char == '[':
                # 🧳 Packing → push (curr_str, curr_num) into storage (stack)
                stack.append((curr_str, curr_num))

                # 🧼 Start fresh → reset working space and label
                curr_str = ""
                curr_num = 0

            elif char == ']':
                # 📤 Unpacking → retrieve last suitcase from storage
                prev_str, repeat = stack.pop()

                # 🔁 Unpack → repeat the current block and attach it to previous string
                curr_str = prev_str + curr_str * repeat

            else:
                # 🔤 Adding characters → keep building in your workspace
                curr_str += char

        # 🎁 Final string after all packing and unpacking is done
        return curr_str

# 🗂️ Memory Hook:
# digit → label suitcase
# '[' → pack → push to stack → reset workspace
# ']' → unpack → pop from stack → repeat and attach
# char → build workspace

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