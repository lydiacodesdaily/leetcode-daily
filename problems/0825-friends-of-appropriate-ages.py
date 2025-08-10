# LeetCode 825 - Friends Of Appropriate Ages
# https://leetcode.com/problems/friends-of-appropriate-ages/
#
# ✅ Problem:
# Given a list of people's ages, return the total number of friend requests sent.
# Friend request rules:
# A will NOT send request to B if:
#   1) age[B] <= 0.5 * age[A] + 7
#   2) age[B] > age[A]
#   3) age[B] > 100 and age[A] < 100
#
# 📚 Pattern:
# Counting + Prefix Sums (bucket counting)
#
# 🔍 Core Idea:
# - Ages range from 1 to 120 → we can bucket counts and use prefix sums for fast range queries.
# - For each ageA:
#     * Find minB = floor(ageA / 2 + 7)
#     * Valid recipients are (minB, ageA] → strictly greater than minB and ≤ ageA
#     * total_in_range = how many people fall into that range
#     * Each person of ageA sends to (total_in_range - 1) others (exclude self)
#     * Multiply by count[ageA] for total from that group
#
# 🧠 Memory Hook:
# count[] ages → prefix[] sum
# for ageA >= 15:
#     minB = ageA//2 + 7
#     total_in_range = prefix[ageA] - prefix[minB]
#     res += count[ageA] * (total_in_range - 1)
#
# ✅ Time Complexity: O(121) ≈ O(1)
# ✅ Space Complexity: O(121) ≈ O(1)
#
# 📌 Common Gotchas:
# - Forgetting age < 15 can't send requests (rule 1 eliminates all recipients)
# - Forgetting to subtract 1 to exclude self
# - Not handling empty buckets (count[age] == 0 → skip)
# - Using <= instead of < when applying rule 1
# - The "ageB > 100 and ageA < 100" rule is already covered by minB logic and bounds.
#
# 🔄 Why age >= 15:
# Rule 1: ageB > 0.5 * ageA + 7
# For there to be ANY valid ageB ≤ ageA:
#   0.5 * ageA + 7 < ageA  →  7 < 0.5 * ageA  → 14 < ageA  → ageA >= 15
#
# 🔄 Dry Run Example:
# ages = [16, 16, 17, 18]
# count[16] = 2, count[17] = 1, count[18] = 1
# prefix array = cumulative counts
#
# ageA = 16 → minB = 16//2 + 7 = 15
#   total_in_range = prefix[16] - prefix[15] = (count of ages ≤ 16) - (count ≤ 15)
#                  = (2) - (0) = 2
#   (total_in_range - 1) = 1
#   res += 2 * 1 = 2 requests (each 16-year-old sends to the other)
#
# ageA = 17 → minB = 15
#   total_in_range = prefix[17] - prefix[15] = (2+1) - (0) = 3
#   (total_in_range - 1) = 2
#   res += 1 * 2 = 2 requests
#
# ageA = 18 → minB = 16
#   total_in_range = prefix[18] - prefix[16] = (2+1+1) - (2) = 2
#   (total_in_range - 1) = 1
#   res += 1 * 1 = 1 request
#
# Total = 2 + 2 + 1 = 5 requests

from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # --- 1) Count frequency of each age ---
        count = [0] * 121  # ages 1..120
        for age in ages:
            count[age] += 1

        # --- 2) Build prefix sum for quick range queries ---
        prefix = [0] * 121
        for i in range(1, 121):
            prefix[i] = prefix[i - 1] + count[i]

        # --- 3) Iterate through each possible ageA ---
        res = 0
        for ageA in range(15, 121):  # Below 15 can't send valid requests
            if count[ageA] == 0:
                continue  # skip if no one of this age

            # Rule 1 cutoff: recipients must have ageB > minB
            minB = ageA // 2 + 7

            # total_in_range = number of people with ageB in (minB, ageA]
            total_in_range = prefix[ageA] - prefix[minB]

            # Subtract 1 to exclude self
            res += count[ageA] * (total_in_range - 1)

        return res


# --- Embedded Examples ---
# Example 1:
# Input: ages = [16, 16, 17, 18]
# Expected Output: 5
# Walkthrough in dry run above.
#
# Example 2:
# Input: ages = [20, 30, 100, 110, 120]
# This will test the "ageB > 100 and ageA < 100" rule via minB and bounds.