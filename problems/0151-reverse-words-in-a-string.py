# LeetCode 151 - Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

# ✅ Problem:
# Given a string `s`, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# Return a string with:
# - Words reversed
# - Leading/trailing/multiple spaces removed
# - Words separated by a single space

# 📚 Pattern:
# String Manipulation + Split + Reverse + Join

# 🔍 Key Insight:
# - Use `s.split()` to clean spaces and get word list
# - Reverse the word list
# - Join with `' '.join(...)` to form result

# 🧠 Memory Hook:
# split() cleans space
# reverse list
# ' '.join()

# ✅ Time: O(n)
# ✅ Space: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split by whitespace (auto-cleans multiple/leading/trailing spaces)
        words = s.split()

        # Step 2: Reverse the list of words
        words.reverse()

        # Step 3: Join with single space
        return ' '.join(words)


# 🔄 Dry Run Example
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    s1 = "  hello   world  "
    print(f"Input: {s1!r}")
    print("Output:", sol.reverseWords(s1))  # → "world hello"

    # Example 2
    s2 = "a good   example"
    print(f"\nInput: {s2!r}")
    print("Output:", sol.reverseWords(s2))  # → "example good a"

    # Edge Case: Only spaces
    s3 = "     "
    print(f"\nInput: {s3!r}")
    print("Output:", sol.reverseWords(s3))  # → ""

    # Edge Case: One word
    s4 = "single"
    print(f"\nInput: {s4!r}")
    print("Output:", sol.reverseWords(s4))  # → "single"