# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
🧠 Pattern: Sliding Window / Greedy
🎯 Problem: Given an array where the i-th element is the price of a given stock on day i,
            return the maximum profit you can achieve from a single buy-sell transaction.
📌 Constraints:
- You must buy before you sell.
- Return 0 if no profit is possible.

⏰ Time Complexity: O(n)
📦 Space Complexity: O(1)

Strategy:
- Track the minimum price so far (buy low)
- At each step, calculate the profit if sold today
- Keep track of the max profit seen
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Track the lowest price so far
        max_profit = 0            # Track the maximum profit so far

        for price in prices:
            # Update min_price if we find a lower price
            if price < min_price:
                min_price = price
            # Calculate potential profit and update max_profit
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
    
"""
🧪 Example Test Cases:

prices = [7,1,5,3,6,4]
# Output: 5 (Buy at 1, sell at 6)

prices = [7,6,4,3,1]
# Output: 0 (No profit possible)

prices = [1,2]
# Output: 1 (Buy at 1, sell at 2)
"""