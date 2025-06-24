# LeetCode 791 - Custom Sort String
# https://leetcode.com/problems/custom-sort-string/

# ✅ Problem:
# Rearrange string `s` so that characters match the relative order defined in `order`.
# Characters in `s` not in `order` can appear in any position.

# 📚 Pattern: HashMap (frequency count) + Custom Sorting

# 🔍 Key Insight:
# - Count how many times each character appears in `s`.
# - Output characters in the order defined by `order`, followed by leftovers.
# - `order` defines priority → build result based on that order.

# 🧠 Memory Hook:
# use Counter(s) → freq of all chars in s
# add chars in order if in s → result.append(c * count[c])
# delete from count after adding → avoid duplicates
# leftover chars (not in order) → add at end (any order)

# ✅ Time Complexity:
# - O(n + m), where n = len(s), m = len(order)
# ✅ Space Complexity: O(1) — constant space since alphabets are fixed (≤26)

from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        result = []

        # Add characters in the order specified
        for c in order:
            if c in count:
                result.append(c * count[c])
                del count[c]  # Remove from count once handled

        # Add remaining characters not in order
        for c, freq in count.items():
            result.append(c * freq)

        return ''.join(result)

# 🔁 Example:
# order = "cba", s = "abcd"
# count = {'a':1, 'b':1, 'c':1, 'd':1}
# result: ['c', 'b', 'a'] + ['d'] => "cbad"

# 📌 Common Gotchas:
# - Be sure to delete characters from the counter after adding them in `order`
# - The final part must include characters not in `order`, in any order

# 🧠 Concepts Reinforced:
# - Frequency counting with `collections.Counter`
# - Ordered character output using custom logic