# LeetCode 739 - Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

# 📚 Pattern:
# Monotonic Stack (BUT this solution uses the optimized reverse scan + jump technique)

# 🔍 Core Idea:
# - Scan from right → left.
# - Track `hottest` temperature seen so far.
# - If current temp ≥ hottest → no warmer future day.
# - Otherwise jump forward using precomputed answers (avoid scanning cold days).
# - This makes the algorithm near O(n).

# 🧠 Memory Hook:
# reverse scan  
# if >= hottest → answer = 0  
# hottest = max(hottest, curr_temp)  
# else jump → days += answer[i+days]  
# store days

# 🧩 Why This Works:
# - Each future index already knows how long *it* waits for a warmer day.
# - So if you land on a cold day, skip its entire wait time in one hop.
# - This reuses future information like DP and avoids repeated comparisons.

# ✅ Time Complexity: O(n) amortized  
# ✅ Space Complexity: O(n)  

# 📌 Common Gotchas:
# - Must use reverse loop.
# - Must update `hottest` only when curr_temp >= hottest.
# - The jump logic (days += answer[i+days]) is the key to speed.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # --- Step 0: Setup ---
        n = len(temperatures)
        answer = [0] * n              # result array
        hottest = 0                   # track max temp seen from the right
        
        # --- Step 1: Reverse scan ---
        for curr_day in range(n - 1, -1, -1):
            curr_temp = temperatures[curr_day]

            # --- Step 2: If this is the new hottest, no warmer day ahead ---
            if curr_temp >= hottest:
                hottest = curr_temp
                # answer stays 0
                continue

            # --- Step 3: Find next warmer day by jumping ---
            days = 1
            while temperatures[curr_day + days] <= curr_temp:
                # Jump using precomputed answers to skip cold days
                days += answer[curr_day + days]

            # --- Step 4: Store result ---
            answer[curr_day] = days

        return answer


# 🔄 Dry Run Example:
# temperatures = [73,74,75,71,69,72,76,73]
# Start from right:
# Day 7 (73): hottest=73, ans=0
# Day 6 (76): new hottest=76, ans=0
# Day 5 (72): next warmer at day 6 → ans=1
# Day 4 (69): next warmer at day 5 → ans=1
# Day 3 (71): 71<72? jump → next warmer at day5 → ans=2
# Day 2 (75): jump day3→day5→day6 → ans=4
# Day 1 (74): next warmer at day2 → ans=1
# Day 0 (73): next warmer at day1 → ans=1

# Output: [1,1,4,2,1,1,0,0]
