# LeetCode 249 - Group Shifted Strings
# https://leetcode.com/problems/group-shifted-strings/

# ✅ Problem:
# Group strings that belong to the same shifting sequence.
# A shifting sequence shifts each letter to the next letter, wrapping from 'z' to 'a'.

# 📚 Pattern:
# Hash Map (grouping) + Modulo for circular alphabet shifts

# 🔍 Core Idea:
# - Normalize each string by shifting all characters relative to the first character.
# - This forms a unique "shift signature" that can be used to group strings.
# - Use modulo 26 to correctly handle wrap-around shifts (like 'z' to 'a').

# 🧠 Memory Hook:
# Build key: (ord(c) - ord(s[0])) % 26 → normalize by first char
# Modulo wraps correctly → z to a
# Group by same normalized pattern using hashmap

# ✅ Time Complexity: O(n * m)
# n = number of strings, m = average length of strings

# ✅ Space Complexity: O(n * m) → storing groupings and keys

from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strings:
            # Step 1: Build shift key relative to first character
            shift_key = [(ord(c) - ord(s[0])) % 26 for c in s]
            key = tuple(shift_key)

            # Step 2: Group by shift key
            groups[key].append(s)

        return list(groups.values())

# 🔄 Dry Run Example:
# Input: ["abc", "bcd", "xyz", "az", "ba"]
# Normalized keys:
# "abc" → [0, 1, 2]
# "bcd" → [0, 1, 2]
# "xyz" → [0, 1, 2]
# "az"  → [0, 25]
# "ba"  → [0, 25]
# Grouped: [["abc", "bcd", "xyz"], ["az", "ba"]]

# 📌 Common Gotchas:
# - Forgetting modulo when calculating shift → won't wrap z to a correctly
# - Using mutable lists as keys → must convert to tuple for hashmap keys
