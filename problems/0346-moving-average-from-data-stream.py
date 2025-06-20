# LeetCode 346 - Moving Average from Data Stream
# https://leetcode.com/problems/moving-average-from-data-stream/

# ✅ Problem:
# Design a class that accepts a stream of integers and calculates
# the moving average of the last `size` values.

# 📚 Pattern:
# Sliding Window (Fixed Size)

# 🧠 Memory Hook:
# use deque to maintain last `size` elements  
# keep running sum → O(1) average calculation  
# if len > size: pop left, subtract from sum

# ✅ Time Complexity: O(1) per `next()` call
# ✅ Space Complexity: O(size) for storing window

from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        # Initialize fixed-size window and running sum
        self.window = deque()
        self.max_size = size
        self.current_sum = 0

    def next(self, val: int) -> float:
        # Add new value to window
        self.window.append(val)
        self.current_sum += val

        # If window exceeds max size, pop left and subtract
        if len(self.window) > self.max_size:
            removed = self.window.popleft()
            self.current_sum -= removed

        # Return moving average
        return self.current_sum / len(self.window)

# 🔄 Dry Run:
# obj = MovingAverage(3)
# obj.next(1) -> returns 1.0
# obj.next(10) -> returns (1+10)/2 = 5.5
# obj.next(3) -> returns (1+10+3)/3 = 4.66...
# obj.next(5) -> window = [10,3,5], returns (10+3+5)/3 = 6.0