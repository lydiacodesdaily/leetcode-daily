# LeetCode 249 - Group Shifted Strings
# https://leetcode.com/problems/group-shifted-strings/

# ✅ Problem:
# Group strings that belong to the same "shifting sequence".
# A shifting sequence means characters have the same relative distance
# between adjacent letters, modulo 26.
# You’re given a list of strings, and you need to group all strings that are part of the same shifting sequence.

# A shifting sequence means:
# • Characters are shifted forward by the same distance.
# • Shifting wraps around: 'z' → 'a'.

# 🧩 Base Pattern:
# Hashing / String Normalization
# Normalize each string into a unique key that represents its shifting pattern.

# 🧠 Memory Hook:
# Normalize by:
# - shifting all letters so first char becomes 'a'
# - key = tuple of (char_i - char_0 + 26) % 26
# Use hash map: key → group list

# ✅ Time Complexity: O(n * k)
# - n = number of strings
# - k = max length of string
# ✅ Space Complexity: O(n * k)
# - For storing results and intermediate normalized keys

from collections import defaultdict

class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for s in strings:
            # Step 1: Normalize the string by relative difference from first char
            shift = [(ord(c) - ord(s[0])) % 26 for c in s]
            key = tuple(shift)
            groups[key].append(s)

        return list(groups.values())

# 🔄 Example Dry Run:
# Input: ["abc", "bcd", "xyz"]
# Normalize "abc": [0,1,2]
# Normalize "bcd": [0,1,2]
# Normalize "xyz": [0,1,2]
# → All grouped together

# Input: ["az", "ba"]
# Normalize "az": [0, 25]
# Normalize "ba": [0, 25]
# → Same group

# 📌 Common Gotchas:
# - Not using modulo 26 → negative values will break pattern
# - Using string diff directly instead of relative shift to first char
# - Forgetting tuple() for dictionary key (lists are unhashable)