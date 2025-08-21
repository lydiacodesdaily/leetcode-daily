# LeetCode 784 - Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/
#
# ✅ Problem:
# Given a string s, return all possible strings by toggling the case of each alphabetic character.
# Digits remain unchanged. Order of output doesn't matter.
#
# 📚 Pattern:
# Backtracking / DFS over positions (branch on letters; single path on digits)
#
# 🔍 Core Idea:
# Walk the string left→right. For each index:
#   - If s[i] is a digit → only one choice: keep it.
#   - If s[i] is a letter → two choices: lowercase and uppercase → recurse both.
#
# 🧠 Memory Hook:
# "digit = 1 branch; letter = 2 branches (lower/UPPER)"
# DFS build path; append when i == n
#
# ✅ Time Complexity:
# Let k = # of alphabetic characters in s.
# - #outputs = 2^k
# - Building each string costs O(n)
# → Total = O(n * 2^k)
#
# ✅ Space Complexity:
# - Aux (recursion/path): O(n)
# - Output storage: O(n * 2^k)
#
# 📌 Common Gotchas:
# - Don’t branch on digits.
# - Use list for path (mutable), then ''.join at leaf for speed.
# - Be careful with in-place edits; always backtrack (pop) after push.
#
# ————————————————————————————————————————————————————————————————

from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res: List[str] = []
        path: List[str] = []
        n = len(s)

        def dfs(i: int) -> None:
            # Base: built a full string
            if i == n:
                res.append(''.join(path))
                return

            ch = s[i]
            if ch.isalpha():
                # branch 1: lowercase
                path.append(ch.lower())
                dfs(i + 1)
                path.pop()

                # branch 2: uppercase
                path.append(ch.upper())
                dfs(i + 1)
                path.pop()
            else:
                # digit: single path
                path.append(ch)
                dfs(i + 1)
                path.pop()

            # (No return value; res is captured by closure)

        dfs(0)
        return res

# ————————————————————————————————————————————————————————————————
# 🔄 Dry Run:
# s = "a1b"
# i=0 'a' → branches: 'a' and 'A'
#   path='a', i=1 '1' → only '1'
#     path='a1', i=2 'b' → 'b' and 'B'
#       -> 'a1b', 'a1B'
#   path='A', i=1 '1' → only '1'
#     path='A1', i=2 'b' → 'b' and 'B'
#       -> 'A1b', 'A1B'
# Output: ["a1b","a1B","A1b","A1B"]
#
# ————————————————————————————————————————————————————————————————
# 🧪 Alternative (Iterative BFS-style):
#
# from collections import deque
#
# def letterCasePermutation_bfs(s: str) -> List[str]:
#     q = deque([''])
#     for ch in s:
#         size = len(q)
#         if ch.isalpha():
#             for _ in range(size):
#                 base = q.popleft()
#                 q.append(base + ch.lower())
#                 q.append(base + ch.upper())
#         else:
#             for _ in range(size):
#                 base = q.popleft()
#                 q.append(base + ch)
#     return list(q)
#
# Same complexity: O(n * 2^k). Pick DFS or BFS based on your preference.