# LeetCode 408 - Valid Word Abbreviation
# https://leetcode.com/problems/valid-word-abbreviation/

# ✅ Problem:
# Given a word and an abbreviation, determine if the abbreviation correctly
# represents the word. Abbreviations can replace non-adjacent substrings with
# positive integers (no leading zeros allowed).

# 📚 Pattern:
# Two Pointers (word[i], abbr[j])

# 🔍 Core Idea:
# - Use two pointers to walk through both strings.
# - When abbr[j] is a digit:
#     - Read the full number (multiple digits)
#     - Skip that many characters in `word`
# - When abbr[j] is a letter:
#     - Must match the current letter in `word`

# 🧠 Memory Hook:
# - walk both with i, j
# - if abbr[j] is digit → build number → i += num
# - if letter → must match word[i]
# - leading zero → invalid

# ✅ Time Complexity: O(n + m)
# ✅ Space Complexity: O(1)

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0  # i for word, j for abbr

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False  # ❌ leading zero not allowed

                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                i += num  # ⏩ skip `num` characters in word
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        # ✅ must consume both strings fully
        return i == len(word) and j == len(abbr)