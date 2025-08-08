# LeetCode 3527 - Find the Most Common Response
# https://leetcode.com/problems/find-the-most-common-response/
#
# ✅ Problem (paraphrased):
# responses[i] is the array of survey answers for day i.
# Within each day, treat duplicate answers as one (dedupe per day).
# Return the response that appears on the MOST days.
# If there's a tie, return the LEXICOGRAPHICALLY smallest string.
#
# 📚 Pattern:
# Hashing / Frequency Count with per-bucket deduplication
#
# 🔍 Key Insight:
# - We count **presence per day**, not raw occurrences.
#   So for each day, convert to a set first.
# - Then tally across all days; pick max frequency, tie-break by min lexicographically.
#
# 🧠 Memory Hook:
# "set per day → Counter across days → max freq, min lex"
#
# ✅ Time Complexity: O(T) where T = total number of strings across all days
# ✅ Space Complexity: O(U) where U = number of unique strings overall

from typing import List
import collections

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = collections.Counter()

        # 1) Deduplicate within each day, then count presence across days
        for day in responses:
            for resp in set(day):
                count[resp] += 1

        # 2) Find the max frequency
        max_freq = max(count.values())

        # 3) Among items with max frequency, return lexicographically smallest
        candidates = [resp for resp, freq in count.items() if freq == max_freq]
        return min(candidates)