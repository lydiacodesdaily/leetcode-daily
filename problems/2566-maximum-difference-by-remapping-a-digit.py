# LeetCode 2566 - Maximum Difference by Remapping a Digit
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

# ✅ Problem:
# You are given a positive integer `num`.
# You must choose **one digit** (0–9) and replace **all** of its occurrences
# with another digit (also 0–9, but different), and do this:
#  - once to get the **maximum value**
#  - once to get the **minimum value**
# Return the difference between max and min values after remapping.

# 📚 Pattern:
# Greedy Digit Remapping

# 🔍 Key Insight:
# - For max → replace first non-9 digit with 9 (maximize high digits first)
# - For min → replace first digit with 0 (unless that creates leading zero)
# - Only one digit can be replaced per operation, and all occurrences are replaced.

# 🧠 Memory Hook:
# - max → replace first d ≠ 9 with '9'
# - min → replace s[0] with '0'
# - use .replace(d, r) on entire number string

# ✅ Time Complexity: O(n) — n = number of digits (max 9)
# ✅ Space Complexity: O(1)

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # 🔺 Get max by replacing first non-'9' with '9'
        for d in s:
            if d != '9':
                max_num = int(s.replace(d, '9'))
                break
        else:
            max_num = int(s)  # Already all 9s

        # 🔻 Get min by replacing first digit with '0'
        min_num = int(s.replace(s[0], '0'))

        return max_num - min_num

# 🔄 Dry Run:
# num = 11891
# str(num) = "11891"
# max: replace '1' → '9' → "99899"
# min: replace '1' → '0' → "00890" → int = 890
# return 99899 - 890 = 99009 ✅