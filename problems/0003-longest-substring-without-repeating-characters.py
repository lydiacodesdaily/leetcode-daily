# LeetCode 3 - Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# ✅ Problem:
# Given a string `s`, find the length of the longest substring without repeating characters.

# 🧠 Memory Hook:
# sliding window + set() → track unique chars
# if duplicate: shrink from left until valid
# update max length at each step

# 📚 Pattern: Sliding Window + Hash Set

# ✅ Time Complexity: O(n) — each character is visited at most twice
# ✅ Space Complexity: O(min(n, a)) — at most O(n) where n is length of `s`, a is alphabet size

# 📌 Common Gotchas:
# - Use set to check for duplicates
# - Don’t forget to shrink the window on duplicate
# - Don’t mix up characters and indices in hashmap version

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                # shrink from the left
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

# 🔁 Example:
# Input: s = "abcabcbb"
# Window: [a,b,c] → [b,c,a] → [c,a,b] → [a,b,c] → max_len = 3

# Alternate version using Hash Map (if you need index tracking)
# Faster for interviews if asked to return the substring as well