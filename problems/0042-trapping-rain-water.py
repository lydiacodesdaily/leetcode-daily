# LeetCode 42 - Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

# ✅ Problem:
# Given n non-negative integers representing an elevation map 
# where the width of each bar is 1, compute how much water it can trap after raining.

# 📚 Pattern:
# Two Pointers (with Dynamic Max Tracking)

# 🔍 Core Idea:
# Use two pointers (`left`, `right`) and track the current left and right maximums.
# Water trapped at each step depends on the smaller of the two boundaries.
# Move the pointer corresponding to the smaller max inward.

# 🧠 Memory Hook:
# lMax / rMax → boundary heights
# water = min(lMax, rMax) - height[i]
# move smaller side inward (since that bound is limiting)

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        left, right = 1, len(height) - 2
        lMax, rMax = height[left - 1], height[right + 1]
        res = 0

        # 🧭 Two-pointer inward traversal
        while left <= right:
            if rMax <= lMax:
                # water trapped on right depends on right boundary
                res += max(0, rMax - height[right])
                rMax = max(rMax, height[right])
                right -= 1
            else:
                # water trapped on left depends on left boundary
                res += max(0, lMax - height[left])
                lMax = max(lMax, height[left])
                left += 1
        
        return res


# 🔄 Dry Run Example:
# Input: [2, 1, 5, 3, 1, 0, 4]
# Step-wise trapped water:
# - Left max grows from 2 → 5
# - Right max grows from 4 backward
# Total water = 4

if __name__ == "__main__":
    arr = [2, 1, 5, 3, 1, 0, 4]
    print(Solution().trap(arr))  # Output: 4