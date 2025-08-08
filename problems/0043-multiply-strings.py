# LeetCode 43 - Multiply Strings
# https://leetcode.com/problems/multiply-strings/
#
# ✅ Problem:
# Given two non-negative integers num1 and num2 represented as strings,
# return the product as a string (without converting them directly to integers).
#
# 📚 Pattern:
# Simulated multiplication (grade school method) + carry handling
#
# 🔍 Core Idea:
# - Reverse iterate over digits of num1 and num2, multiply each pair.
# - Store results in an array where index i+j and i+j+1 represent the carry position.
# - Convert result array back to string, skipping leading zeros.
#
# 🧠 Memory Hook:
# reverse nums → multiply digit by digit
# pos[i+j] += mul // carry
# pos[i+j+1] += mul % carry
# strip leading zeros
#
# ✅ Time Complexity: O(m * n) — m = len(num1), n = len(num2)
# ✅ Space Complexity: O(m + n)
# ✅ NOT a DP problem → safe for E5 full-stack
#
# 📌 Common Gotchas:
# - Don’t forget to handle leading zeros in the final string
# - Indexing: result[i + j + 1] is the current digit; result[i + j] is the carry position
# - Inputs can be "0" → must return "0"

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)  # result array
        
        # Reverse iterate so that least significant digit is at the end
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1  # carry position, digit position
                
                # Add to the current position
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
        
        # Convert list to string, skipping leading zeros
        result_str = ''.join(map(str, res)).lstrip('0')
        return result_str or "0"


# 🔄 Dry Run:
# num1 = "123", num2 = "45"
# m=3, n=2 → res = [0,0,0,0,0]
# i=2 ('3'), j=1 ('5') → mul=15, p1=3, p2=4 → total=15 → res[4]=5, res[3]+=1
# i=2, j=0 ('4') → mul=12, p1=2, p2=3 → total=13 → res[3]=3, res[2]+=1
# ... repeat
# Final res = [0,5,5,3,5] → "5535" ✅

# 🧪 Example:
# sol = Solution()
# print(sol.multiply("2", "3"))      # "6"
# print(sol.multiply("123", "45"))   # "5535"
# print(sol.multiply("0", "456"))    # "0"