# LeetCode 122 - Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# ✅ Problem:
# You may complete as many transactions as you like (buy then sell), but
# you must sell before you buy again. Maximize profit.

# 📚 Pattern:
# Greedy on Adjacent Increases

# 🔍 Key Insight:
# With unlimited transactions, the global optimum is to
# **sum every positive price rise between consecutive days**.
# Intuition: any rising run p[i] < ... < p[j] is captured by
# (p[i+1]-p[i]) + ... + (p[j]-p[j-1]) = p[j] - p[i].

# 🧠 Memory Hook:
# "Add all ups" → profit += max(0, prices[i] - prices[i-1])

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

# 🔄 Example:
# prices = [7,1,5,3,6,4]
# ups: (1->5)=4, (3->6)=3 → total = 7

# 📌 Notes:
# - No need to track explicit buy/sell days—summing all positive deltas
#   is equivalent to buying at each local valley and selling at the next peak.
# - If prices are non-increasing → profit stays 0.