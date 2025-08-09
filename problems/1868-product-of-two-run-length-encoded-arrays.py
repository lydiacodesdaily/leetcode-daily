# LeetCode 1868 - Product of Two Run-Length Encoded Arrays
# https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/
#
# ✅ Problem (in plain words)
# You’re given two arrays A and B already in Run-Length Encoding (RLE) form:
#   A = [[val1, cnt1], [val2, cnt2], ...]
#   B = [[val1, cnt1], [val2, cnt2], ...]
# If you decoded them, they would have the SAME total length.
# Return the RLE of the element-wise product Decode(A)[k] * Decode(B)[k].
#
# 📚 Pattern
# Two pointers over runs (merge-like scan) + "consume the min count" each step.
#
# 🔍 Core Idea (bird's-eye view so it feels grounded)
# Think of each pair [value, count] as a "run" = value repeated 'count' times.
# When multiplying A and B element-wise, we advance through both run lists in lockstep:
#   - Look at the current runs (val1, count1) and (val2, count2).
#   - We can multiply k = min(count1, count2) positions right now.
#   - Their product is prod = val1 * val2, repeated k times.
#   - Emit that k-run (merging with the previous run if it has the same product).
#   - Decrease both counts by k; if a run hits 0, move to the next run in that array.
#
# 🧠 Memory Hooks
# - "Consume min count → emit product → decrement → advance"
# - "If last output run has same product, MERGE it (increase its count)"
#
# ✅ Why we merge adjacent runs in the result?
#   If the product of the next chunk is the same as the last product we emitted,
#   we shouldn't create a new run — just extend the last one. That keeps output compressed.
#
# ✅ Complexity
# - Time:  O(m + n) where m, n are the number of runs (NOT the decoded lengths!)
# - Space: O(1) extra (besides the output)
#
# ⚠️ What we DO NOT do
# - We NEVER decode the arrays. That would be linear in the total decoded length and unnecessary.
#
# ------------------------------------------------------------------------------

from typing import List

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        """
        Walk through both encoded lists of runs in lockstep.
        At each step, consume the minimum remaining count between the two current runs.
        Emit/merge the product run into the result.
        """

        i, j = 0, 0                       # pointers into encoded1 and encoded2
        res: List[List[int]] = []         # output RLE: [[product_value, count], ...]

        # Iterate while both still have runs left
        while i < len(encoded1) and j < len(encoded2):
            val1, count1 = encoded1[i]
            val2, count2 = encoded2[j]

            # k = how many positions we can multiply RIGHT NOW
            # (limited by whichever run runs out first)
            k = min(count1, count2)

            # product for these k positions
            prod = val1 * val2

            # If the last emitted run has the same product, extend that run instead of appending a new pair.
            # This keeps the result compressed (still valid RLE).
            if res and res[-1][0] == prod:
                res[-1][1] += k
            else:
                res.append([prod, k])

            # We just consumed k positions from BOTH current runs.
            # Reduce their counts by k; if a count hits zero, that run is exhausted,
            # so we advance the corresponding pointer to the next run.
            encoded1[i][1] -= k
            encoded2[j][1] -= k

            if encoded1[i][1] == 0:  # done with this run in encoded1
                i += 1
            # Note: not elif; both may hit zero at the same time
            if encoded2[j][1] == 0:  # done with this run in encoded2
                j += 1

        return res


# ---------------------------------------------------------------------------
# 🧪 Commented Dry Runs (non-executable; for mental tracing)

# Example A (shows merging):
# encoded1 = [[1,3], [2,3]]          # decode: [1,1,1, 2,2,2]
# encoded2 = [[6,3], [3,3]]          # decode: [6,6,6, 3,3,3]
#
# i=0 [1,3], j=0 [6,3]
#   k=min(3,3)=3, prod=6
#   res=[] → append [6,3]
#   decrement: [1,0], [6,0] → advance i=1, j=1
#
# i=1 [2,3], j=1 [3,3]
#   k=min(3,3)=3, prod=6
#   res last is [6,3] → merge → [6,6]
#   decrement: [2,0], [3,0] → advance i=2, j=2 → done
#
# res = [[6,6]]

# Example B (partial consumes):
# encoded1 = [[1,2], [3,3], [2,1]]     # decode: [1,1, 3,3,3, 2]
# encoded2 = [[2,1], [1,3], [4,2]]     # decode: [2, 1,1,1, 4,4]
#
# Start: i=0 [1,2], j=0 [2,1]
#   k=1, prod=2 → res=[[2,1]]
#   A: [1,1], B: [2,0] → j=1
#
# i=0 [1,1], j=1 [1,3]
#   k=1, prod=1 → res=[[2,1],[1,1]]
#   A: [1,0] → i=1, B: [1,2]
#
# i=1 [3,3], j=1 [1,2]
#   k=2, prod=3 → res=[[2,1],[1,1],[3,2]]
#   A: [3,1], B: [1,0] → j=2
#
# i=1 [3,1], j=2 [4,2]
#   k=1, prod=12 → res=[[2,1],[1,1],[3,2],[12,1]]
#   A: [3,0] → i=2, B: [4,1]
#
# i=2 [2,1], j=2 [4,1]
#   k=1, prod=8 → res=[[2,1],[1,1],[3,2],[12,1],[8,1]]
#   A: [2,0] → i=3, B: [4,0] → j=3 → done
#
# res = [[2,1],[1,1],[3,2],[12,1],[8,1]]

# ---------------------------------------------------------------------------
# 📌 Quick Checklist (for interviews)
# - Use two pointers over runs; never decode.
# - Compute k = min(count1, count2).
# - Emit product run; MERGE if same as previous.
# - Decrement both counts by k; advance exhausted runs.
# - Complexity speaks to runs, not decoded length: O(m+n).