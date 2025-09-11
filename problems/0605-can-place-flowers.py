# LeetCode 605 - Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/

# ✅ Problem:
# Given a flowerbed (list of 0s and 1s), and a number n, return True if n new flowers can be planted
# without violating the no-adjacent-flowers rule.

# 📚 Pattern:
# Greedy Linear Scan

# 🔍 Key Insight:
# Only plant a flower at index i if:
#   - flowerbed[i] == 0
#   - and both neighbors are 0 (or out of bounds)
# After planting, skip next spot (i += 2)

# 🧠 Memory Hook:
# plant if: spot empty AND neighbors empty (or bounds)
# then skip next (i += 2)

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Forgetting edge checks (i == 0 or i == len - 1)
# - Not skipping index after planting
# - Modifying input flowerbed is okay unless restricted

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0

        while i < len(flowerbed):
            # 🌱 Check if current spot and its neighbors are all empty or edge
            if flowerbed[i] == 0 and \
               (i == 0 or flowerbed[i - 1] == 0) and \
               (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                # 💐 Plant a flower here
                flowerbed[i] = 1
                count += 1
                i += 2  # 🚫 Skip next to avoid adjacent planting
            else:
                i += 1

        return count >= n

# 🔄 Dry Run:
# Input: flowerbed = [1, 0, 0, 0, 1], n = 1
# Step-by-step:
# i = 0 → 1 (skip)
# i = 1 → check [0, 0, 0] → plant at i=2 → flowerbed = [1, 0, 1, 0, 1]
# i = 4 → 1 (skip)
# count = 1 → ✅ return True
