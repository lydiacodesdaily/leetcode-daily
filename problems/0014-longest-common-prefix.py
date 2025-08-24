# LeetCode 14 - Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

# ✅ Problem:
# Given an array of strings, return the longest common prefix string among them.
# If there is no common prefix, return an empty string "".

# 📚 Pattern:
# String Manipulation + Horizontal Scanning

# 🧪 Subtype:
# Prefix reduction – iteratively check & shorten prefix

# 🧠 Memory Hook:
# start with first word as prefix
# loop rest: shrink prefix until it matches s
# return prefix

# ✅ Time Complexity: O(S) — total number of characters in all strings
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Early exit if prefix becomes empty
# - Avoid checking characters one by one if you can use `str.startswith`

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
       
        # Start with the first word as the candidate prefix
        prefix = strs[0]
       
        # Compare with each subsequent string
        for s in strs[1:]:
            # Shrink prefix until it is a prefix of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
       
        return prefix

# 🔄 Dry Run:
# Input: ["flower","flow","flight"]
# prefix = "flower"
# check "flow": not startswith → shrink → "flow"
# check "flight": not startswith → shrink → "flo" → "fl" ✅
# Output: "fl"

# Input: ["dog","racecar","car"]
# prefix = "dog"
# "racecar" does not start with "dog" → shrink until ""
# return ""

"""
🎨 Visual Imagery

Imagine you’re holding a long ribbon (the first string).
	•	You walk along a line of friends (the other strings).
	•	Each friend says: “Nope, my word doesn’t start with that much ribbon — cut it shorter!” ✂️
	•	You keep trimming the ribbon from the end until it fits what they’re saying.
	•	At the end of the walk, the ribbon left in your hand is the longest prefix that everyone agrees on.

🧠 Memory Hook
	•	Start with first string as ribbon.
	•	For each word → shrink ribbon until it fits.
	•	Stop if ribbon disappears (return “”).
	•	Answer = ribbon after the last friend.

"""