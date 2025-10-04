# LeetCode 380 - Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
#
# ✅ Problem:
# Design a set-like structure with:
#   insert(val) -> bool     # True if inserted (not present), else False
#   remove(val) -> bool     # True if removed (present), else False
#   getRandom() -> int      # Uniform random among current elements
#
# 📚 Pattern:
# HashMap + Dynamic Array (swap-with-last to delete in O(1))
#
# 🔍 Core Idea:
# - Keep values in a list for O(1) random access.
# - Keep a dict mapping value -> index in the list for O(1) existence & index lookup.
# - On remove, swap the element to delete with the last element, update the moved
#   element’s index in the dict, then pop from the end (O(1)).
#
# 🧠 Memory Hook:
# dict: val -> idx
# insert: append; dict[val] = len(list)-1
# remove: idx = dict[val]; last = list[-1]
#         list[idx] = last; dict[last] = idx; pop; del dict[val]
# getRandom: random.choice(list)
# ⚠️ Don’t: `val in list` (O(n)), `list.pop(index)` (O(n) unless index is last)
#
# ✅ Time Complexity: O(1) average for insert, remove, getRandom
# ✅ Space Complexity: O(n)
#
# 📌 Common Gotchas (from your questions):
# - Using `self.list.pop(val)` treats `val` as an index (bug) and is O(n) if mid-pop.
# - Checking `if val in self.list` is O(n); use a dict for membership O(1).
# - After swapping during remove, MUST update dict for the moved `last` element.
# - Always `pop()` from the end for O(1).
#
# ------------------------------------------------------------

import random
from typing import Dict, List

class RandomizedSet:
    def __init__(self):
        # list: store values for O(1) random access
        # dict: map value -> index in list for O(1) lookup
        self.list: List[int] = []
        self.dict: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        # 1) If present, return False
        if val in self.dict:
            return False
        # 2) Append to list; record index in dict
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        # 1) If absent, return False
        if val not in self.dict:
            return False

        # 2) Get index of target and last element
        idx = self.dict[val]
        last_idx = len(self.list) - 1
        last_val = self.list[last_idx]

        # 3) Move last_val into idx (only if idx != last_idx, but harmless either way)
        self.list[idx] = last_val
        self.dict[last_val] = idx

        # 4) Pop tail and delete val from dict
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        # Uniform random: each index equally likely
        return random.choice(self.list)


# 🔄 Embedded Example:
# r = RandomizedSet()
# print(r.insert(1))   # True  -> list=[1], dict={1:0}
# print(r.remove(2))   # False -> 2 not present
# print(r.insert(2))   # True  -> list=[1,2], dict={1:0,2:1}
# print(r.getRandom()) # 1 or 2
# print(r.remove(1))   # True  -> swap idx(1)=0 with last=2 => list=[2], dict={2:0}
# print(r.insert(2))   # False -> already present
# print(r.getRandom()) # 2

# 🧪 Dry Run (Step-by-step state):
# Start: list=[], dict={}
# insert(10):
#   - dict has no 10 -> dict[10]=0; list=[10]
#   => list=[10], dict={10:0}, returns True
# insert(20):
#   - dict has no 20 -> dict[20]=1; list=[10,20]
#   => list=[10,20], dict={10:0,20:1}, returns True
# remove(10):
#   - idx=dict[10]=0; last_idx=1; last_val=20
#   - list[0]=20; dict[20]=0
#   - pop() -> list=[20]; del dict[10]
#   => list=[20], dict={20:0}, returns True
# getRandom() -> 20