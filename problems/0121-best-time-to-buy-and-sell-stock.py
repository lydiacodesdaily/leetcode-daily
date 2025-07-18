# LeetCode 121 - Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# ✅ Problem:
# Given an array `prices` where prices[i] is the price of a stock on day i,
# return the maximum profit you can achieve from a single buy/sell.
# You must buy before you sell.

# 📚 Pattern:
# Two Pointers (min tracking + profit comparison)

# 🔍 Core Idea:
# - Track lowest price seen so far (`min_price`)
# - For each price, calculate profit = current_price - min_price
# - Update max profit if current profit is higher

# 🧠 Memory Hook:
# track min_price so far  
# profit = price - min_price  
# update max_profit each day

# ✅ Time Complexity: O(n) — single pass through the array
# ✅ Space Complexity: O(1) — constant space used

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

# 🔄 Dry Run:
# prices = [7,1,5,3,6,4]
# min_price = 1
# profit = max(5-1, 3-1, 6-1, 4-1) = 5
# ✅ return 5