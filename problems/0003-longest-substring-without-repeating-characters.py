# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
🧠 Pattern: Sliding Window (Dynamic Size)
🎯 Problem: Find the length of the longest substring without repeating characters.

⏰ Time Complexity: O(n)
📦 Space Complexity: O(min(n, k)) — where k is charset size (ASCII = O(1), Unicode = O(n))

Two optimal solutions below:
- Option 1: Set-based sliding window (your approach)
- Option 2: Dictionary-based window with fast skipping (LeetCode editorial approach)
"""

from typing import Set

# ✅ Option 1: Set-based Sliding Window (Your Version)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen: Set[str] = set()
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


# ✅ Option 2: Dictionary-based Sliding Window (Editorial / Fast Skipping)
class SolutionFast:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        start = 0
        max_length = 0

        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            max_length = max(max_length, end - start + 1)
            char_index[char] = end

        return max_length


"""
🧪 Example Test Cases:

s = "abcabcbb"     # Output: 3 ("abc")
s = "bbbbb"        # Output: 1 ("b")
s = "pwwkew"       # Output: 3 ("wke")
s = ""             # Output: 0
s = "au"           # Output: 2
s = "dvdf"         # Output: 3 ("vdf")
"""