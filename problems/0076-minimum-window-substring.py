# LeetCode 76 - Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

# ✅ Problem:
# Given two strings `s` and `t`, return the minimum window in `s`
# which contains all the characters in `t`. If no such window exists, return "".

# 📚 Pattern:
# Sliding Window (Shrinking) + Hash Map (Char Frequency)

# 🔍 Core Idea:
# - Use a hash map to count frequencies of characters in `t`
# - Expand right to include valid characters
# - Once all required characters are in window → try to shrink from left
# - Track the minimum window when valid

# 🧠 Memory Hook:
# build freq map for t  
# expand right → count matches  
# shrink left when valid  
# update min_len if all chars matched

# ✅ Time Complexity: O(s + t) — linear scan with constant-time operations
# ✅ Space Complexity: O(t) — for frequency map

from collections import Counter
from typing import Tuple

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)  # Frequency map of required characters
        window = {}
        have = 0
        need_count = len(need)

        res = [-1, -1]  # store window bounds
        res_len = float("inf")
        left = 0

        # Expand the window with the right pointer
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            # Try to shrink the window from the left
            while have == need_count:
                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Pop from the left of the window
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""

# 🔄 Dry Run:
# s = "ADOBECODEBANC", t = "ABC"
# → Window "BANC" contains A, B, C with minimum length