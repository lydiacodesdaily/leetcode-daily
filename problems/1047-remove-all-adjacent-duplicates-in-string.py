# LeetCode 1047 - Remove All Adjacent Duplicates in String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# ✅ Problem:
# Given a string s, repeatedly remove adjacent duplicate characters
# until no more can be removed. Return the final result string.

# 📚 Pattern:
# Stack (String Reduction)

# 🔍 Key Insight:
# - Use a stack to build the result character by character
# - If the top of the stack matches the current char → pop (remove duplicate)
# - Otherwise, push the character onto the stack

# 🧠 Memory Hook:
# use stack → if c == stack[-1] → pop()
# else → stack.append(c)

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and stack[-1] == c:
                stack.pop()  # Remove adjacent duplicate
            else:
                stack.append(c)  # Keep character

        return ''.join(stack)


# 🔄 Example Dry Run:
# Input: "abbaca"
# Stack trace:
# a → ['a']
# b → ['a', 'b']
# b → pop → ['a']
# a → pop → []
# c → ['c']
# a → ['c', 'a']
# Output: "ca"

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates("abbaca"))  # Output: "ca"
    print(sol.removeDuplicates("azxxzy"))  # Output: "ay"
    print(sol.removeDuplicates("a"))       # Output: "a"