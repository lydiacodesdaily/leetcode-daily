# LeetCode 118 - Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

# ✅ Problem:
# Given an integer numRows, generate the first numRows of Pascal's Triangle.
# Each row is constructed such that:
# - The first and last elements are 1
# - Each middle element is the sum of the two elements directly above it

# 📚 Pattern:
# Math / Triangle Construction

# 🔍 Key Insight:
# - Each row depends on the previous row
# - Start and end with 1
# - Fill middle with: prev[i-1] + prev[i]

# 🧠 Memory Hook:
# res = []
# for row in range(numRows):
#     middle = prev[i-1] + prev[i]
#     new row = [1] + middle + [1]

# ✅ Time Complexity: O(n^2)
# ✅ Space Complexity: O(n^2)

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []

        for row in range(numRows):
            curr = [1]  # Every row starts with 1

            # Fill in the middle using the previous row
            if res:
                prev = res[-1]
                for i in range(1, len(prev)):
                    curr.append(prev[i - 1] + prev[i])
                curr.append(1)  # End each row with 1

            res.append(curr)

        return res


# 🔄 Dry Run:
# numRows = 5
# Output:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(1))  # [[1]]
    print(sol.generate(2))  # [[1], [1,1]]
    print(sol.generate(5))  # [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]