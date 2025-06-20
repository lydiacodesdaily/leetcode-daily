# LeetCode 670 - Maximum Swap
# https://leetcode.com/problems/maximum-swap/

# ✅ Problem:
# Given a number, return the maximum number you can get by swapping two digits at most once.

# 📚 Pattern:
# Greedy with Digit Manipulation
# - Find the highest digit that occurs later and can be swapped to increase value.
# - Only one swap allowed → find optimal opportunity.

# 🧩 Subtype:
# Last Occurrence Tracking + Greedy Swap
# - Greedily swap left digit with the largest possible right digit
# - Store last index of each digit to quickly find swap opportunities

# 🧠 Memory Hook:
# digits = list(str(num))        # convert number to digit chars
# last = {digit: index}          # last seen positions
# loop left to right, try find digit > digits[i] on the right
# swap and return int("".join(digits))
# - Track last_seen[digit]
# - Try swapping i with larger digit j (from 9→digit+1) if j's index > i

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)

# 📌 Common Gotchas:
# - Must convert `num` to list of characters to swap
# - After swap, return int("".join(digits))
# - Only one swap allowed → break after first valid swap

class Solution:
    def maximumSwap(self, num: int) -> int:
        # Step 1: Convert number to list of digits
        digits = list(str(num))  # e.g. '2736' → ['2', '7', '3', '6']

        # Step 2: Track the last seen index for each digit
        last = {int(d): i for i, d in enumerate(digits)}  # e.g. {'2': 0, '7': 1, '3': 2, '6': 3}

        # Step 3: Iterate from left to right and find the first opportunity to swap
        for i, d in enumerate(digits):
            # Check from '9' down to d+1 to find a higher digit
            for bigger in range(9, int(d), -1):
                if last.get(bigger, -1) > i:
                    # Step 4: Swap if a bigger digit occurs later
                    digits[i], digits[last[bigger]] = digits[last[bigger]], digits[i]
                    # Step 5: Convert back to int and return
                    return int("".join(digits))

        # Step 6: If no swap occurred, return original
        return num

# 🔄 Dry Run:
# Input: num = 2736
# digits = ['2', '7', '3', '6']
# last = {2:0, 7:1, 3:2, 6:3}
# i = 0, d = '2'
# check if 9,8,...,3 in last and last[3] > 0 → yes!
# swap '2' and '6' → ['6', '7', '3', '2']
# return int("".join(...)) = 7236 ✅

# Input: num = 9973 → no bigger digit appears after a smaller one
# return 9973 (no swap)