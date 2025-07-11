# LeetCode 229 - Majority Element II
# https://leetcode.com/problems/majority-element-ii/

# ✅ Problem:
# Find all elements in an integer array that appear more than ⌊n / 3⌋ times.
# You must solve it in O(n) time and O(1) space.

# 📚 Pattern:
# Extended Boyer-Moore Voting Algorithm

# 🔍 Key Insight:
# - There can be at most 2 elements that appear more than ⌊n / 3⌋ times.
# - First pass: Find up to 2 candidates using voting logic.
# - Second pass: Verify which ones actually appear > n/3 times.

# 🧠 Memory Hook:
# count = 0 → set candidate
# same → count++
# different → count--
# final result = candidates with actual count > n/3

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Step 1: Find candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify actual counts
        result = []
        for candidate in [candidate1, candidate2]:
            if nums.count(candidate) > len(nums) // 3:
                result.append(candidate)

        return result


# 🔄 Dry Run Example:
# Input: [1,1,1,3,3,2,2,2]
# - First pass candidates → candidate1 = 1, candidate2 = 2
# - Second pass counts → 1 appears 3 times, 2 appears 3 times
# ✅ Output: [1, 2]

if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3]))              # [3]
    print(sol.majorityElement([1,1,1,3,3,2,2,2]))     # [1, 2]
    print(sol.majorityElement([1,2]))                # [1, 2]
    print(sol.majorityElement([1,2,3,4]))            # []