# LeetCode 636 - Exclusive Time of Functions
# https://leetcode.com/problems/exclusive-time-of-functions/

# ✅ Problem:
# Given `n` functions and a list of logs of function calls in the form of 
# ["function_id:start_or_end:timestamp"], compute the exclusive execution time for each function.
# A function's exclusive time is the time it runs excluding the time spent in child calls.

# 🧩 Base Pattern:
# Stack for Nested Function Execution
# - Use stack to track the active function call chain.
# - Push on "start", pop on "end", and update exclusive time accordingly.

# 🧪 Subtype:
# Simulation with Timestamp Tracking
# - Track the previous timestamp to calculate duration since last log.
# - Use `+1` on end timestamps because intervals are inclusive.

# 🧠 Memory Hook:
# stack = current call chain (function ID)
# on "start": push and add time to top-of-stack
# on "end": pop and add (curr - prev + 1), then prev = curr + 1
# use prev_time to track gap length
# key formula: res[stack[-1]] += curr_time - prev_time (for start)
#              res[func] += curr_time - prev_time + 1 (for end)
#              prev_time = curr_time + 1 after popping

# ✅ Time Complexity: O(L), where L = number of logs
# ✅ Space Complexity: O(n + L) — result array + stack

# 📌 Common Gotchas:
# - Forgetting to add +1 on "end" logs (timestamps are inclusive)
# - Not updating `prev_time` correctly after an "end" log
# - Not handling nested function calls properly with stack

from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn_id_str, typ, time_str = log.split(":")
            fn_id = int(fn_id_str)
            curr_time = int(time_str)

            if typ == "start":
                if stack:
                    # Add elapsed time to the function on top of the stack
                    res[stack[-1]] += curr_time - prev_time
                stack.append(fn_id)
                prev_time = curr_time
            else:
                # End of current function
                res[stack.pop()] += curr_time - prev_time + 1
                prev_time = curr_time + 1

        return res

# 🔄 Dry Run:
# Input: n = 2
# logs = [
#   "0:start:0",
#   "1:start:2",
#   "1:end:5",
#   "0:end:6"
# ]
# 
# Timeline:
# 0: 0 starts  → stack = [0], prev = 0
# 2: 1 starts  → add 2 to res[0], stack = [0, 1], prev = 2
# 5: 1 ends    → add 4 to res[1], stack = [0], prev = 6
# 6: 0 ends    → add 1 to res[0], stack = [], prev = 7
#
# Final output: [3, 4]