# LeetCode 424 - Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
#
# ✅ Problem:
# Given a string s and an integer k, return the length of the longest substring
# you can get by replacing at most k characters so that all characters in the substring are the same.
#
# 📚 Pattern:
# Dynamic Sliding Window (expand right, shrink left when invalid)
#
# 🔍 Core Idea:
# Keep a window [left..right]. Let:
#   window_len = right - left + 1
#   max_freq   = count of the most frequent char *seen so far in the window*
# Window is valid if we can fix it with ≤ k replacements:
#   window_len - max_freq <= k
# If invalid, move left forward to shrink until valid again.
#
# 🧠 Memory Hook:
# window_len - max_freq <= k  → valid
# track max_freq ↑ only (don’t decrease on shrink)
# update ans = max(ans, window_len) after ensuring validity
#
# ⏱️ Time: O(n) — each index enters/leaves window at most once
# 💾 Space: O(1) — at most 26 uppercase letters
#
# ⚠️ Common Gotchas:
# - Do NOT recompute/decrease max_freq when shrinking; let it be the historical max.
#   This keeps correctness because if (window_len - max_freq) > k, we always shrink.
#   Even if max_freq is stale-high, the invalidity test is conservative and still triggers shrinks.
# - Don’t return right - left + 1 at the very end; track the best length along the way.
#
# —————————————————————————————————————————————————————————————————————————————

from typing import List
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Sliding window with frequency map and historical max_freq.
        Steps:
          1) Expand right, count s[right].
          2) Update max_freq to the highest count ever seen in the current window.
          3) If window_len - max_freq > k → invalid, move left (shrink).
          4) Update answer with current valid window length.
        """
        freq = defaultdict(int)
        left = 0
        max_freq = 0  # historical max of any single character count in the window
        best = 0

        for right, c in enumerate(s):
            freq[c] += 1
            # Only increase max_freq; never force it down when we move left.
            if freq[c] > max_freq:
                max_freq = freq[c]

            # If we need more than k changes to make the window uniform, shrink from left
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Now valid: update best
            best = max(best, right - left + 1)

        return best

# —————————————————————————————————————————————————————————————————————————————
# 🔄 Dry Run:
# s = "AABABBA", k = 1
# Window moves; max_freq tracks the highest frequency seen in window:
# - At "AABA": window_len=4, max_freq=3 ('A'), window_len - max_freq = 1 → valid, best=4
# - Later "ABBA": window_len=4, max_freq still 3 (historical), 4 - 3 = 1 → valid, best remains 4
# Answer: 4
#
# 📝 Note on `right - left + 1`:
# You *do* compute window length as `right - left + 1`, but ONLY after shrinking
# until `(window_len - max_freq) <= k`. The final answer is the maximum of those
# valid lengths observed during the scan — not simply the last window length.
# —————————————————————————————————————————————————————————————————————————————

# ✅ Embedded Example
# Input:  s = "ABAB", k = 2
# Output: 4   (Replace two 'A'→'B' or two 'B'→'A' to make "BBBB" or "AAAA")