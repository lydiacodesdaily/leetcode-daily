# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

"""
🧠 Pattern: Topological Sort (BFS / Kahn's Algorithm)
🎯 Problem: Determine if you can finish all courses given prerequisite pairs.
📌 Use Cases:
- Detecting cycles in a directed graph
- Scheduling tasks with dependencies

⏰ Time Complexity: O(V + E)
   - V = number of courses (nodes)
   - E = number of prerequisites (edges)

📦 Space Complexity: O(V + E)
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build adjacency list and in-degree array
        graph = defaultdict(list)  # prereq -> list of courses depending on it
        # {prereq course: [course2, course3]}
        in_degree = [0] * numCourses # [ course index 0 = [ prereq #], index2 [prereq #]..]

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Step 2: Initialize queue with all courses having no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        taken = 0  # Count of courses we can finish

        # Step 3: Process queue
        while queue:
            current = queue.popleft()
            taken += 1

            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: If we could take all courses, return True
        return taken == numCourses

"""
🧪 Example Usage:
numCourses = 4
prerequisites = [[1,0],[2,1],[3,2]]
# Output: True (1<-0, 2<-1, 3<-2)

numCourses = 2
prerequisites = [[1,0],[0,1]]
# Output: False (cycle)
"""