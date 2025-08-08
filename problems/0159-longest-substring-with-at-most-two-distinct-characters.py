# LeetCode 159 - Longest Substring with At Most Two Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
#
# ✅ Problem:
# Given a string s, return the length of the longest substring that contains
# at most two distinct characters.
#
# 📚 Pattern:
# Sliding Window (variable size, shrink when > k distinct)
#
# 🔍 Core Idea:
# - Maintain a sliding window [l, r] with at most 2 distinct characters.
# - Expand r one step at a time, count each char in a hashmap.
# - If distinct chars > 2 → shrink from left until distinct ≤ 2.
# - Track max length during expansion.
#
# 🧠 Memory Hook:
# hashmap(char → freq)
# expand right, shrink left if len(map) > 2
# update max_len each step
#
# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1) — at most 3 keys in hashmap
# ✅ NOT a DP problem → safe for E5 full-stack
#
# 📌 Common Gotchas:
# - Use while loop to shrink left until distinct ≤ 2
# - Must decrement and delete keys from hashmap when freq hits 0

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        counts = defaultdict(int)
        max_len = 0

        for r, ch in enumerate(s):
            counts[ch] += 1

            # Shrink window until at most 2 distinct chars
            while len(counts) > 2:
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    del counts[s[l]]
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len


# 🔄 Dry Run:
# s = "eceba"
# r=0: add e → counts={e:1}, max_len=1
# r=1: add c → counts={e:1, c:1}, max_len=2
# r=2: add e → counts={e:2, c:1}, max_len=3
# r=3: add b → counts={e:2, c:1, b:1} → shrink:
#       l=0: e-- → e=1
#       l=1: c-- → c=0 → del c, l=2
#     counts={e:1, b:1}, max_len=3
# r=4: add a → counts={e:1, b:1, a:1} → shrink:
#       l=2: e-- → e=0 → del e, l=3
#     counts={b:1, a:1}, max_len=3 ✅

# 🧪 Example:
# sol = Solution()
# print(sol.lengthOfLongestSubstringTwoDistinct("eceba"))  # 3 ("ece")
# print(sol.lengthOfLongestSubstringTwoDistinct("ccaabbb")) # 5 ("aabbb")