# LeetCode 1768 - Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/

# ✅ Problem:
# Given two strings word1 and word2, merge them alternately by character.
# If one string is longer, append the remainder at the end.
# Return the merged result.

# 📚 Pattern:
# Two Pointers

# 🔍 Key Insight:
# - Loop up to the length of the shorter string
# - Append characters alternately
# - Add the remaining part of the longer string at the end

# 🧠 Memory Hook:
# zip shorter length → w1[i] + w2[i]
# then add leftover w1[i:] or w2[i:]

# ✅ Time Complexity: O(n + m)
# ✅ Space Complexity: O(n + m)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        # Loop through both strings using index
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])

        # Append the remaining characters from the longer string
        res.append(word1[i + 1:])
        res.append(word2[i + 1:])

        return ''.join(res)


# 🔄 Example Dry Run:
# Input: word1 = "abc", word2 = "pqr"
# Steps: a+p, b+q, c+r → "apbqcr"
# Output: "apbqcr"

if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeAlternately("abc", "pqr"))        # apbqcr
    print(sol.mergeAlternately("ab", "pqrs"))        # apbqrs
    print(sol.mergeAlternately("abcd", "pq"))        # apbqcd