# LeetCode 380 - Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
#
# ✅ Problem:
# Implement a data structure that supports:
#   - insert(val): Inserts an item val into the set if not present. Returns True if inserted.
#   - remove(val): Removes an item val from the set if present. Returns True if removed.
#   - getRandom(): Returns a random element from the current set. Each element must have the same probability.
#
# 📚 Pattern:
# HashMap + Dynamic Array (Swap-with-Last Trick)
#
# 🔍 Core Idea:
# Keep values in a list for O(1) random access, and a map {val: index_in_list} for O(1) membership & index lookup.
# For remove, swap the element to delete with the last element, update its index in the map, and pop the list tail.
#
# 🧠 Memory Hook:
# map: val -> idx
# insert: push to end; map[val] = len(list)-1
# remove: swap idx with last; update map[last]; pop; del map[val]
# getRandom: random.choice(list)
#
# ✅ Time Complexity: O(1) average for insert, remove, getRandom
# ✅ Space Complexity: O(n) for list + map
#
# 📌 Common Gotchas:
# - Forgetting to update the moved-last element’s index in the map during remove.
# - Not handling the case when val is already present (insert) or not present (remove).
# - getRandom must be uniform: use random.choice over the array (not map keys).
#
# 🧩 Notes:
# - This is a staple E5-friendly problem (not DP). Very likely in real interviews.
# - The swap-with-last trick avoids O(n) delete in arrays.

import random
from typing import Dict, List

class RandomizedSet:
    def __init__(self):
        # 📦 Storage
        # nums: list of current values (for O(1) random access)
        # pos:  map value -> index in nums (for O(1) membership and index lookup)
        self.nums: List[int] = []
        self.pos: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        """
        Insert val if not present.
        Returns True if inserted, False if already present.

        Steps:
        1) Check existence in pos map.
        2) Append to nums and record index in pos.
        """
        if val in self.pos:
            return False

        # Append and record position
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Remove val if present.
        Returns True if removed, False if not present.

        Steps (Swap-with-Last Trick):
        1) If val not in pos -> False
        2) Get index of val (idx) and last element (last_val)
        3) Move last_val into idx (nums[idx] = last_val), update pos[last_val] = idx
        4) Pop last element from nums
        5) Delete val from pos
        """
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last_val = self.nums[-1]

        # Move last_val to idx if we're not already at the last position
        self.nums[idx] = last_val
        self.pos[last_val] = idx

        # Remove tail
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        """
        Return a uniformly random element from the set.

        Step:
        - Use random.choice over the nums list for uniform O(1) selection.
        """
        return random.choice(self.nums)


# 🔄 Embedded Example:
# r = RandomizedSet()
# print(r.insert(1))   # True  -> nums=[1], pos={1:0}
# print(r.remove(2))   # False -> 2 not present
# print(r.insert(2))   # True  -> nums=[1,2], pos={1:0,2:1}
# print(r.getRandom()) # 1 or 2 with equal probability
# print(r.remove(1))   # True  -> swap idx(1)=0 with last=2 => nums=[2], pos={2:0}
# print(r.insert(2))   # False -> already present
# print(r.getRandom()) # 2

# 🧪 Dry Run (Step-by-Step):
# Start: nums=[], pos={}
# insert(10):
#   - 10 not in pos -> append -> nums=[10]; pos={10:0} -> return True
# insert(20):
#   - 20 not in pos -> append -> nums=[10,20]; pos={10:0,20:1} -> return True
# remove(10):
#   - idx=0; last_val=20
#   - nums[0]=20; pos[20]=0
#   - pop -> nums=[20]; del pos[10] -> pos={20:0} -> return True
# getRandom():
#   - random.choice([20]) -> 20