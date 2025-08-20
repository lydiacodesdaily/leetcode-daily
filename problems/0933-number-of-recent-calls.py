# LeetCode 933 - Number of Recent Calls
# https://leetcode.com/problems/number-of-recent-calls/
#
# ✅ Problem:
# Implement RecentCounter:
#   - ping(t): record a call at time t (ms) and return # of calls in [t-3000, t].
#   - t is strictly increasing across calls.
#
# 📚 Pattern:
# Sliding Window with Queue (FIFO) — maintain only timestamps in the last 3000ms.
#
# 🔍 Core Idea:
# Keep a queue of recent timestamps. On each ping:
#   1) Push t.
#   2) Pop from the left while q[0] < t - 3000 (expired).
#   3) Answer is len(q).
#
# 🧠 Memory Hook:
# deque = window of last 3000ms
# push t → pop expired (< t-3000) → return size
#
# ✅ Time Complexity:
# - Each ping: Amortized O(1) (each timestamp enqueued/dequeued once)
# ✅ Space Complexity: O(W) where W = # of pings within 3000ms window
#
# 📌 Common Gotchas:
# - Use while loop to remove *all* expired pings, not just one.
# - Window is inclusive: [t-3000, t], so keep times >= t-3000.
# - t is strictly increasing → makes amortized O(1) possible.
#
# 🧩 Why not Binary Search?
# - We only ever query at the latest t, and only append on the right.
# - Queue eviction from the left is simpler and O(1) amortized.
# - BS is useful if you needed arbitrary-time queries.

from collections import deque

class RecentCounter:
    def __init__(self):
        # queue holds timestamps within the active 3000ms window
        self.q = deque()

    def ping(self, t: int) -> int:
        # --- Step 1: add the new ping ---
        self.q.append(t)

        # --- Step 2: evict expired pings (< t - 3000) ---
        cutoff = t - 3000
        while self.q and self.q[0] < cutoff:
            self.q.popleft()

        # --- Step 3: current window size = answer ---
        return len(self.q)

# 🔄 Dry Run:
# Calls: ping(1), ping(100), ping(3001), ping(3002)
# After ping(1):     q=[1]                  → len=1
# After ping(100):   q=[1,100]              → len=2
# After ping(3001):  cutoff=1; evict <1 → none; q=[1,100,3001] → len=3
# After ping(3002):  cutoff=2; evict 1 → q=[100,3001,3002]     → len=3