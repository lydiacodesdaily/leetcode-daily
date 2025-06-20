# LeetCode 219 - Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

# ✅ Problem:
# Given an integer array `nums` and an integer `k`, return `True` if there are
# two distinct indices `i` and `j` in the array such that:
#     - nums[i] == nums[j]
#     - abs(i - j) <= k

# 📚 Pattern: 
# Sliding Window (Fixed-size k), Set-based duplicate detection

# 🧠 Memory Hook:
# use set() as window of size k  
# if num already in window → duplicate within range → return True  
# add num, remove leftmost if size > k

# ✅ Time Complexity: O(n) — loop through all elements once  
# ✅ Space Complexity: O(k) — store at most k elements in the set

# 📌 Common Gotchas:
# - Using set correctly: unordered, but fine for membership check
# - Make sure to pop the correct element when shrinking window
# - Don’t use `popleft()` — set is unordered; use `remove()`

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            # ❗Duplicate found within window size k
            if nums[right] in window:
                return True

            window.add(nums[right])

            # 🧹 Shrink window if it exceeds size k
            if right - left >= k:
                window.remove(nums[left])
                left += 1

        return False

# 🔄 Dry Run:
# nums = [1, 2, 3, 1], k = 3
# i = 0 → window = {1}
# i = 1 → window = {1, 2}
# i = 2 → window = {1, 2, 3}
# i = 3 → 1 in window → ✅ return True

# nums = [1, 2, 3, 1], k = 2
# i = 0 → window = {1}
# i = 1 → window = {1, 2}
# i = 2 → window = {1, 2, 3}
# i = 3 → remove 1 → 1 not in window → return False