# LeetCode 49 - Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# ✅ Problem:
# Given an array of strings, group the anagrams together.
# An anagram is a word formed by rearranging the letters of another word.

# 📚 Pattern:
# Hashing with Tuple Key (Character Frequency)

# 🔍 Key Insight:
# - All anagrams have the same letter counts.
# - Use a 26-length array to count each character.
# - Convert the array to a tuple → use as a hashable key in a dictionary.

# 🧠 Memory Hook:
# tuple of counts = anagram signature
# key = [0]*26 → count[ord(c) - ord('a')]++
# same count tuple → same group

# ✅ Time Complexity: O(n * k), where:
#   - n = number of words
#   - k = max length of a word (for counting letters)
# ✅ Space Complexity: O(n * k) — for storing groups

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # 🔠 Count the frequency of each character
            count = [0] * 26  # 26 lowercase English letters
            for c in word:
                index = ord(c) - ord('a')
                count[index] += 1

            # 🗝️ Use tuple of counts as a hashable key
            key = tuple(count)
            anagrams[key].append(word)

        # 📦 Return grouped anagrams
        return list(anagrams.values())

"""
🔄 Dry Run Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

Groupings:
- "eat", "tea", "ate" → key: (1,0,0,...,1,0,...,1,...)
- "tan", "nat"        → key: (1,0,0,...,1,...,1,...)
- "bat"               → key: (1,1,0,...,1,...)

Output:
[
  ["eat", "tea", "ate"],
  ["tan", "nat"],
  ["bat"]
]
"""