# LeetCode 489 - Robot Room Cleaner
# https://leetcode.com/problems/robot-room-cleaner/

# ✅ Problem:
# Clean an entire room using only four robot APIs: move, turnLeft, turnRight, and clean.
# The robot starts at an unknown position and direction in a grid where 0 = wall and 1 = open space.

# 📚 Pattern:
# DFS + Backtracking + Set for visited tracking

# 🔍 Core Idea:
# Treat the unknown room layout as a graph traversal problem.
# Use DFS to explore and clean all reachable cells.
# Track visited positions using (x, y) coordinates.
# Backtrack correctly by reversing the robot's move and turning it back to its original direction after exploring each path.
# Robot's limited API requires careful control of movement and direction state.

# 🧠 Memory Hook:
# DFS → clean → move → backtrack → rotate
# directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] (up, right, down, left)
# backtrack = turn around → move() → reset orientation

# ✅ Time Complexity: O(N) where N is the number of open cells
# ✅ Space Complexity: O(N) for the visited set and recursion stack

class Solution:
    def cleanRoom(self, robot):
        # Set of visited cells using virtual coordinates
        visited = set()

        # Directions: up, right, down, left → (dx, dy)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # 'd' Corresponds to:
        # 0 → up
        # 1 → right
        # 2 → down
        # 3 → left
        
        def go_back():
            # Turn 180 degrees to reverse direction
            robot.turnRight()
            robot.turnRight()
            robot.move()  # Move back to the previous cell
            # Restore original orientation by turning back 180 degrees
            robot.turnRight()
            robot.turnRight()

        def dfs(x: int, y: int, d: int):
            visited.add((x, y))
            robot.clean()

            for i in range(4):
                new_d = (d + i) % 4  # Calculate new direction index
                dx, dy = directions[new_d]
                new_x, new_y = x + dx, y + dy

                if (new_x, new_y) not in visited:
                    if robot.move():
                        # If move is successful, go deeper in DFS
                        dfs(new_x, new_y, new_d)
                        # Backtrack to previous cell and restore direction
                        go_back()

                # Turn robot right to face the next direction
                robot.turnRight()

        # Start DFS from (0, 0) facing 'up' → direction index 0
        dfs(0, 0, 0)

# 🔄 Dry Run Example:
# Start at (0,0) facing up.
# Try all 4 directions → if move is successful, continue DFS.
# After exploring, go_back() restores position and orientation.

# 📌 Common Gotchas:
# - Must carefully backtrack: move back and restore orientation.
# - Must use virtual coordinates since the robot doesn't know the grid.
# - Must track direction with a modular index (0 to 3).
