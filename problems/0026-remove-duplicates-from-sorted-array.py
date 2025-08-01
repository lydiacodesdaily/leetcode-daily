# LeetCode 26 - Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# ✅ Problem:
# Given a sorted array nums, remove the duplicates in-place such that each unique element appears only once.
# Return the number of unique elements `k`. Modify the input array so that the first `k` elements are the unique values.

# 🧩 Pattern:
# Two Pointers (Read/Write)
# - One pointer reads through the list
# - The other writes the next unique value in place

# 🔍 Key Insight:
# Because the array is sorted, duplicates will always be adjacent.
# So we only need to compare nums[read] with nums[write].
# If they're different, it's a new unique number → move write forward and update.

# 🧠 Memory Hook:
# read = scans forward
# write = last unique value index
# if nums[read] != nums[write] → write += 1; nums[write] = nums[read]
# return write + 1 (since write is index, but we need count)

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Off-by-one errors: `write` is index, so final return is `write + 1`
# - Don't forget to update nums[write] after incrementing write
# - Return length only — don’t worry about cleaning up trailing values

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 0  # Pointer for the last unique value

        for read in range(1, len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]

        return write + 1  # Length = index + 1

# 🔄 Dry Run:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Iterations:
# read = 1 → nums[1] == nums[0] → skip
# read = 2 → nums[2] != nums[0] → write=1, nums[1]=1
# read = 3 → nums[3] == nums[1] → skip
# read = 5 → nums[5] != nums[2] → write=2, nums[2]=2
# ...
# Final: nums[:5] = [0,1,2,3,4] → return 5 ✅