# LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
# https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/
#
# ✅ Problem:
# Given a string s and an integer k, delete the fewest characters so that s contains
# at most k distinct characters.
#
# 📚 Pattern:
# Frequency counting + Greedy "keep top‑k buckets"
#
# 🔍 Core Idea:
# We can delete from anywhere → only total counts per character matter.
# Keep the k biggest frequency buckets; delete everything else.
#
# 🧠 Memory Hook:
# counts → take top k
# deletions = n - sum(top k)
# k ≥ distinct → 0; k == 0 → n
#
# ✅ Time Complexity: O(n + σ log k) using heapq.nlargest (σ = #distinct chars)
# ✅ Space Complexity: O(σ)
#
# 📌 Common Gotchas:
# - k == 0 → must delete all characters
# - k ≥ distinct → 0 deletions
# - This is NOT sliding window / substring; NOT DP

from collections import Counter
import heapq

class Solution:
    def minimumDeletions(self, s: str, k: int) -> int:
        """
        Steps
        1) Count frequency for each distinct char
        2) Handle trivial edges: k == 0 or k >= distinct
        3) Keep the k largest frequency buckets via heapq.nlargest
        4) Answer = total length - sum(kept)
        """
        n = len(s)
        if k == 0:
            return n

        freq = list(Counter(s).values())
        if k >= len(freq):
            return 0

        # Take the k largest counts to keep
        keep = sum(heapq.nlargest(k, freq))
        return n - keep


# 🔄 Dry Run:
# s = "aaabbc", k = 2
# counts: a:3, b:2, c:1 → freq = [3,2,1]
# nlargest(2, freq) = [3,2] → keep = 5 → deletions = 6 - 5 = 1 ✅
#
# s = "abcde", k = 1
# freq = [1,1,1,1,1]; top-1 = [1] → keep = 1 → deletions = 5 - 1 = 4 ✅
#
# s = "aaaa", k = 3
# distinct = 1 ≤ k → deletions = 0 ✅
#
# 🧪 Embedded Example
# print(Solution().minimumDeletions("aaabbc", 2))  # 1
# print(Solution().minimumDeletions("abcde", 1))   # 4
# print(Solution().minimumDeletions("aaaa", 3))    # 0