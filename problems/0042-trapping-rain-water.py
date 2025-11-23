# LeetCode 42 - Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

# ✅ Problem:
# Given elevation heights, compute how much rain water can be trapped between the bars.

# 📚 Pattern:
# Two Pointers with running boundary max (left_max / right_max)

# 🔍 Core Idea:
# - Water above each bar = min(max_left, max_right) - height[i]
# - Instead of precomputing arrays, use two pointers:
#   - Whichever side is *shorter* (left vs right) determines the limiting boundary.
#   - Process that side, update its max, and accumulate water for that index.

# 🧠 Memory Hook:
# water = min(l_max, r_max) - h
# move shorter side:
#   if hL < hR → trust l_max, move L
#   else       → trust r_max, move R
# on chosen side:
#   update side_max
#   add side_max - hSide to answer

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - The core logic: we only compute water on the *shorter* side at each step.
# - Don’t try to compute both sides at once; always move one pointer.
# - Be careful with `left < right` (not `<=`) to avoid double-processing.
# - Remember: `output += side_max - height[side]` (not the other way around).


class Solution:
    def trap(self, height: List[int]) -> int:
        # -----------------------------------------
        # 1️⃣ Edge case: empty or too short
        # -----------------------------------------
        if not height:
            return 0

        # -----------------------------------------
        # 2️⃣ Initialize pointers and boundary maxes
        # -----------------------------------------
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        output = 0

        # -----------------------------------------
        # 3️⃣ Move pointers toward each other
        #    Always process the *shorter side*
        # -----------------------------------------
        while left < right:
            # If left bar is lower, left side is the limiting boundary
            if height[left] < height[right]:
                # Update left_max
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # Water trapped on top of current left bar
                    output += left_max - height[left]
                # Move left inward
                left += 1

            else:
                # Right bar is lower or equal → right side is limiting
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # Water trapped on top of current right bar
                    output += right_max - height[right]
                # Move right inward
                right -= 1

        return output


# 💡 Why does "move the shorter side" work?

# At any step:
#   - We know left_max (best we've seen on the left) and right_max (best on the right).
#   - True water level at index i = min(left_max, right_max).
#
# If height[left] < height[right]:
#   - That means right side is at least as tall as height[right] ≥ height[left].
#   - So the limiting factor on left side is **left_max**, not the right side,
#     because there's guaranteed some bar on the right that's tall enough.
#   - Therefore, the min(left_max, right_max) = left_max (or ≥ left_max),
#     so we can safely compute water at `left` using only left_max.
#
# Symmetrically, if height[right] <= height[left]:
#   - Right side is shorter or equal.
#   - The limiting boundary for index `right` is right_max,
#     so we compute water using right_max and move `right` inward.


# 🔄 Dry Run (short version):
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
#
# Start:
#   left=0, right=11
#   left_max=0, right_max=0, water=0
#
# height[left]=0 < height[right]=1 → process left
#   left_max = max(0,0) = 0
#   water += 0 - 0 = 0
#   left → 1
#
# left=1 (h=1), right=11 (h=1) → else branch (right side)
#   right_max = max(0,1) = 1
#   water += 1 - 1 = 0
#   right → 10
#
# left=1 (h=1), right=10 (h=2) → left side
#   left_max = max(0,1) = 1
#   water += 1 - 1 = 0
#   left → 2
#
# left=2 (h=0), right=10 (h=2) → left side
#   left_max = 1
#   water += 1 - 0 = 1
#   left → 3
#
# ...
# Continue this process → final water = 6 (correct answer).