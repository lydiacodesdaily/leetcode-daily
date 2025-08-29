# LeetCode 207 - Course Schedule
# https://leetcode.com/problems/course-schedule/

# ✅ Problem:
# There are `numCourses` labeled from 0 to numCourses-1.
# You're given a list of prerequisites as pairs [a, b], meaning to take course `a`, you must take course `b` first.
# Return True if you can finish all courses (i.e., there is no cycle), False otherwise.

# 📚 Pattern:
# Graph - Topological Sort (Kahn's Algorithm - BFS)

# 🔍 Core Idea:
# - Build a graph of prerequisites and track in-degrees for each course
# - Start with courses that have 0 in-degree (no prerequisites)
# - Remove them and reduce in-degree of dependent courses
# - If all courses can be visited → no cycle → return True

# 🧠 Memory Hook:
# build graph + in-degree  
# start from in-degree 0 queue  
# each time reduce neighbor's in-degree  
# count visited — if != numCourses → cycle → False

# ✅ Time Complexity: O(V + E)
# ✅ Space Complexity: O(V + E)
# V = number of courses, E = number of prerequisites

from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build graph and in-degree map
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Step 2: Add courses with no prerequisites to queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Step 3: Process courses in topological order
        visited = 0
        while queue:
            current = queue.popleft()
            visited += 1

            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses were visited
        return visited == numCourses

# 🔄 Example:
# numCourses = 2, prerequisites = [[1,0]]
# 0 → 1, no cycle → True
# numCourses = 2, prerequisites = [[1,0],[0,1]]
# cycle detected → False

""" 
🧪 Example Usage:
numCourses = 4
prerequisites = [[1,0],[2,1],[3,2]]
# Output: True (1<-0, 2<-1, 3<-2)

numCourses = 2
prerequisites = [[1,0],[0,1]]
# Output: False (cycle)
"""