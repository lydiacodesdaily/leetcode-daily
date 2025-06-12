# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

"""
🧠 Pattern: Two Pointers
🎯 Problem: Determine if a string is a valid palindrome
   - Only consider alphanumeric characters
   - Ignore cases

📌 Use Cases:
- Text validation
- Input sanitization
- Low-latency palindrome checks (chat apps, streaming input)

⏰ Time Complexity: O(n)
📦 Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters case-insensitively
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

"""
🧪 Example Input:
s = "A man, a plan, a canal: Panama"
Output: True

s = "race a car"
Output: False
"""