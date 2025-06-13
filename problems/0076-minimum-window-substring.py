# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

"""
🧠 Pattern: Sliding Window + Hash Map
🎯 Problem: Return the minimum window substring of `s` such that every character in `t` 
            (including duplicates) is included in the window.

📌 Use Cases:
- Finding shortest segment with full coverage (e.g., logs, search queries)
- Real-time filtering and substring optimization

⏰ Time Complexity: O(|s| + |t|) — each character is visited at most twice
📦 Space Complexity: O(|t|) — for hash maps to store character counts
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Step 1: Count required characters in t
        t_count = Counter(t)
        window = {}

        # Step 2: Initialize pointers and result tracking
        have, need = 0, len(t_count) # len unique characters
        res, res_len = [-1, -1], float('inf')
        left = 0

        # Step 3: Expand right pointer
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # If character is fulfilled in window, increment 'have'
            if char in t_count and window[char] == t_count[char]:
                have += 1

            # Step 4: Try shrinking from left if window is valid
            while have == need:
                # Update result if smaller window is found
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Shrink from the left
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        # Step 5: Return result
        l, r = res # not using "left", "right" 
        return s[l:r+1] if res_len != float('inf') else ""

"""
🧪 Example Test Cases:

s = "ADOBECODEBANC"
t = "ABC"
# Output: "BANC"

s = "a"
t = "a"
# Output: "a"

s = "a"
t = "aa"
# Output: ""

s = "aaflslflsldkalskaaa"
t = "aaa"
# Output: "aaa"
"""