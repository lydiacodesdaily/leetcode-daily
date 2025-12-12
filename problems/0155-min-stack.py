# LeetCode 155 - Min Stack
# https://leetcode.com/problems/min-stack/

# ✅ Problem:
# Design a stack that supports push, pop, top, and retrieving
# the minimum element in constant time.

# 🧩 Pattern:
# Stack + State Tracking
# - Each stack entry stores BOTH:
#   (current_value, min_so_far_at_this_point)

# 🔍 Core Idea:
# Instead of maintaining a separate min stack,
# we snapshot the minimum at every push.
# This guarantees O(1) getMin without synchronization logic.

# 🧠 Memory Hook:
# stack stores (val, minSoFar)
# minSoFar = min(val, previous min)
# getMin → stack[-1][1]

# ✅ Time Complexity:
# push / pop / top / getMin → O(1)

# ✅ Space Complexity:
# O(n) — one tuple per element

# 📌 Why interviewers like this:
# - Single data structure
# - No edge-case sync bugs
# - Very easy to reason about under pressure


class MinStack:

    def __init__(self):
        # Stack will store tuples: (value, min_so_far)
        self.stack = []

    def push(self, val: int) -> None:
        # ── Step 1: Determine current minimum ──
        if not self.stack:
            curr_min = val
        else:
            curr_min = min(val, self.stack[-1][1])

        # ── Step 2: Push (value, min_so_far) ──
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        # ── Step 3: Pop top element (value, min snapshot) ──
        self.stack.pop()

    def top(self) -> int:
        # ── Step 4: Return value part only ──
        return self.stack[-1][0]

    def getMin(self) -> int:
        # ── Step 5: Return min snapshot at top ──
        return self.stack[-1][1]


# 🔄 Embedded Example:
# Operations:
# push(5) → stack = [(5,5)]
# push(3) → stack = [(5,5),(3,3)]
# push(7) → stack = [(5,5),(3,3),(7,3)]
# getMin() → 3
# pop()    → removes (7,3)
# getMin() → 3
# pop()    → removes (3,3)
# getMin() → 5

# 🧠 Interview Tip:
# If asked “why not two stacks?”:
# - This avoids sync issues
# - Still O(1)
# - Clear invariant: top always knows the min