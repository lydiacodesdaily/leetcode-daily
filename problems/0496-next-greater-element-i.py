# LeetCode 496 - Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

# ✅ Problem:
# For each element in nums1 (which is a subset of nums2), find the first element
# to its right in nums2 that is greater. If none, return -1.

# 📚 Pattern:
# Monotonic (decreasing) stack + hashmap lookup

# 🔍 Key Insight:
# - Scan nums2 once. Keep a stack of elements that are still "waiting" to find a bigger element.
# - When current num > stack top, pop and map: next_greater[popped] = current.
# - Push current num; leftovers get -1.
# - Finally, answer nums1 by hashmap lookups.

# 🧠 Memory Hook:
# "Waiting room" = decreasing stack.
# Pop smaller → map to current.

# ✅ Time: O(n) over nums2 (each element pushed/popped once) + O(m) lookups
# ✅ Space: O(n) for stack + map

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []            # monotonic decreasing stack of values from nums2
        next_greater = {}     # value -> its next greater value in nums2

        for x in nums2:
            # Resolve all smaller values that were waiting for a greater one
            while stack and stack[-1] < x:
                smaller = stack.pop()
                next_greater[smaller] = x
            stack.append(x)

        # Remaining values have no greater element to the right
        for x in stack:
            next_greater[x] = -1

        # Build answers for nums1 by direct lookup
        return [next_greater[x] for x in nums1]


# 🔄 Mini Dry Run:
# nums1 = [4,1,2], nums2 = [1,3,4,2]
# Iterate nums2:
# 1: stack=[] -> push 1       stack=[1]
# 3: pop 1 -> map[1]=3        stack=[]; push 3   stack=[3]
# 4: pop 3 -> map[3]=4        stack=[]; push 4   stack=[4]
# 2: 2 < 4? no -> push 2      stack=[4,2]
# End: leftovers 4,2 -> map[4]=-1, map[2]=-1
# Answer: [map[4], map[1], map[2]] = [-1, 3, -1]