# LeetCode 70 - Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# ✅ Problem:
# You are climbing a staircase with `n` steps.
# Each time you can climb either 1 or 2 steps.
# Return the number of distinct ways to reach the top.

# 📚 Pattern:
# 1D Dynamic Programming (Fibonacci Sequence)

# 🔍 Key Insight:
# - To reach step `n`, you can come from:
#     - step `n-1` with 1 step
#     - step `n-2` with 2 steps
# - So: ways(n) = ways(n-1) + ways(n-2)

# 🧠 Memory Hook:
# - Base cases: ways(1)=1, ways(2)=2
# - Like Fibonacci: F(n+1)
# - Use two variables: prev1 (ways to step i-1), prev2 (ways to step i-2)
# - curr = prev1 + prev2

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        # 🧭 Base cases
        if n <= 2:
            return n
        
        # 🔧 Initialize DP for step 1 and 2
        prev1, prev2 = 2, 1

        # 🔁 Build up from step 3 to n
        for i in range(3, n + 1):
            curr = prev1 + prev2  # current step = sum of previous two
            prev2 = prev1         # shift window
            prev1 = curr

        return prev1

# 🔄 Dry Run:
# Input: n = 5
# Step 1: 1 way
# Step 2: 2 ways
# Step 3: 1+2 = 3
# Step 4: 2+3 = 5
# Step 5: 3+5 = 8
# ✅ Output: 8