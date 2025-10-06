# LeetCode 76 - Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

# ✅ Problem:
# Given two strings s and t, return the minimum window in s 
# which will contain all the characters in t. 
# If there is no such window, return an empty string "".

# 📚 Pattern: Sliding Window (Dynamic Shrinking Window)
# 🧩 Goal: smallest substring that contains all chars in t (including duplicates)

# 🔍 Core Idea:
# - Use a sliding window [l, r] to expand and contract dynamically.
# - Use Counter(t) to track required frequencies.
# - Expand r → include new char; contract l → remove extras when all matched.
# - Only process chars from s that are present in t (filtering optimization).

# 🧠 Memory Hook:
# window_count == dict_t → formed += 1
# when formed == required → try shrink window
# update min_len when smaller window found
# ans = (length, start, end)
# return s[start:end+1]

# ✅ Time Complexity: O(|s| + |t|) (filtered sliding window)
# ✅ Space Complexity: O(|s| + |t|)

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 🪟 Step 0: Edge case
        if not s or not t:
            return ""

        # 🧮 Step 1: Frequency map for t
        dict_t = Counter(t)
        required = len(dict_t)  # number of unique chars required

        # ⚙️ Step 2: Filter s to only chars in t (optimization)
        filtered_s = []
        for i, ch in enumerate(s):
            if ch in dict_t:
                filtered_s.append((i, ch))  # (index, char)

        # 🧩 Step 3: Initialize window pointers & state
        l = r = 0
        formed = 0  # # of chars meeting desired frequency
        window_counts = {}
        ans = (float("inf"), None, None)  # (window_len, start, end)

        # 🚀 Step 4: Expand window to the right
        while r < len(filtered_s):
            ch = filtered_s[r][1]
            window_counts[ch] = window_counts.get(ch, 0) + 1

            # Check if this char now satisfies required frequency
            if window_counts[ch] == dict_t[ch]:
                formed += 1

            # 🧲 Step 5: Try contracting window from the left when valid
            while l <= r and formed == required:
                ch = filtered_s[l][1]
                start = filtered_s[l][0]
                end = filtered_s[r][0]

                # Update best (shortest) window found
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                # Pop leftmost char out of window
                window_counts[ch] -= 1
                if window_counts[ch] < dict_t[ch]:
                    formed -= 1
                l += 1  # move left pointer forward

            # Move right pointer forward
            r += 1

        # 🏁 Step 6: Return result substring
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


# 🔄 Dry Run Example:
# s = "ADOBECODEBANC", t = "ABC"
# dict_t = {A:1, B:1, C:1}
# filtered_s = [(0,'A'),(3,'B'),(5,'C'),(9,'B'),(10,'A'),(12,'C')]
#
# Sliding window progression:
#   expand → find all chars
#   when window has A,B,C → shrink to smallest
#   final min window = "BANC"