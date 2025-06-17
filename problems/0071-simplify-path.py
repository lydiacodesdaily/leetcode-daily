# LeetCode 71 - Simplify Path
# https://leetcode.com/problems/simplify-path/

# ✅ Problem:
# Given an absolute path for a Unix-style file system, return the simplified canonical path.

# 🔍 Key Insight:
# Use a **stack** to simulate directory traversal:
# - "." → skip
# - ".." → pop from stack (go up one level)
# - valid names → push onto stack
# At the end, join the stack with slashes.

# ✅ Time Complexity: O(n) — where n is the length of the path
# ✅ Space Complexity: O(n) — stack holds the path components

# 📚 Pattern: Stack (Path Traversal)

class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []

        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)

# 🔁 Example Dry Run:
# Input: "/a/./b/../../c/"
# Split: ['','a','.','b','..','..','c','']
# Stack process:
# - '' → skip
# - 'a' → stack = ['a']
# - '.' → skip
# - 'b' → stack = ['a', 'b']
# - '..' → pop → stack = ['a']
# - '..' → pop → stack = []
# - 'c' → stack = ['c']
# - '' → skip
# Return: "/c"

# 📌 Common Gotchas:
# - Don’t forget to skip empty strings from splitting on multiple slashes
# - Don’t pop if the stack is empty (e.g., leading with "..")
# - Ensure result starts with "/" and doesn’t end with "/"

# 🧠 Follow-Up:
# - This logic also works for building virtual file system paths or resolving relative imports.