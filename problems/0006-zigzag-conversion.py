# LeetCode 6 - Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/

# ✅ Problem:
# Convert a given string `s` into a zigzag pattern with `numRows` rows,
# and then read row by row.

# 📚 Pattern:
# Simulation / String Building

# 🔍 Key Insight:
# - We simulate walking down and up the rows.
# - Use direction flag (+1 for down, -1 for up).
# - Append each character to the correct row bucket.
# - Finally, join all rows together.

# ✅ Time Complexity: O(n), where n = len(s)
# ✅ Space Complexity: O(n), for storing row buckets

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # 2) Prepare row buckets
        rows = ["" for _ in range(numRows)]

        # 3) State for the walk
        row = 0
        dir = 1  # +1 = going down, -1 = going up

        # 3) Simulate the zigzag fill
        for ch in s:
            rows[row] += ch

            # Flip direction at boundaries
            if row == 0:
                dir = 1
            elif row == numRows - 1:
                dir = -1

            row += dir

        # 4) Read row-by-row
        return "".join(rows)


# 🔄 Dry Run Example:
# Input: s = "PAYPALISHIRING", numRows = 3
# Zigzag:
# P   A   H   N
# A P L S I I G
# Y   I   R
# Output: "PAHNAPLSIIGYIR"