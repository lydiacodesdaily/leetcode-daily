# LeetCode 84 — Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/

# 🧩 Problem:
# Given heights of adjacent bars in a histogram, find the area of the
# largest rectangle that can be formed using these bars.

# 🎯 Use Cases:
# 1. Real estate: largest rectangular buildable land in irregular plots
# 2. Image processing: largest continuous uniform region in binary images
# 3. Layout optimization: maximizing rectangular space usage

# 📚 Pattern:
# Monotonic Increasing Stack (height-index tracking)

# 🔍 Core Idea:
# Maintain a stack of bars in increasing height order.
# When a shorter bar arrives → pop taller bars and compute areas.

# 🧠 Memory Hook:
# - "append 0 sentinel" → flush remaining areas
# - stack stores (start_index, height)
# - while curr_height < top → pop & compute area = height * (i - start_index)
# - update start_index after each pop so new height extends left correctly

# ⏱ Time: O(n) — each bar pushed/popped once
# 📦 Space: O(n) — monotonic stack


from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    stack: List[tuple[int, int]] = []  # Stack of (index, height) pairs
    max_area = 0
    
    # Append 0 to handle remaining elements in stack
    for i, height in enumerate(heights + [0]):
        start = i  # Starting position for current height
        
        # Process stack while we find higher heights
        while stack and stack[-1][1] > height:
            index, h = stack.pop()
            width = i - index
            area = width * h
            max_area = max(max_area, area)
            start = index  # Update start to the leftmost position
        
        stack.append((start, height))
    
    return max_area
