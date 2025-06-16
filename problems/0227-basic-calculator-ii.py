# LeetCode 227 - Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/

# ✅ Problem:
# Evaluate a simple expression string `s` containing non-negative integers,
# '+', '-', '*', '/', and empty spaces. Return the result as an integer.
# Integer division should **truncate toward zero**.

# 🔍 Key Insight:
# - Use a **stack** to defer + and - operations.
# - Immediately evaluate * and / during parsing.
# - Parse multi-digit numbers, skip spaces.

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'  # Initialize as '+' for first number

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)

            # If we hit an operator or the end of the string, process the last number
            if c in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    prev = stack.pop()
                    stack.append(int(prev / num))  # truncate toward zero
                sign = c
                num = 0  # reset number

        return sum(stack)

# 🔁 Dry Run: s = "3+2*2"
#
# Goal: Evaluate expression with correct operator precedence.
#
# Initialize:
# stack = []
# num = 0
# sign = '+'

# Step 1: char = '3' (digit)
# num = 3

# Step 2: char = '+' (operator)
# sign was '+', so we do: stack.append(3)
# stack = [3]
# Update: sign = '+', num = 0

# Step 3: char = '2' (digit)
# num = 2

# Step 4: char = '*' (operator)
# sign was '+', so we do: stack.append(2)
# stack = [3, 2]
# Update: sign = '*', num = 0

# Step 5: char = '2' (digit and last char)
# num = 2
# Process pending sign '*':
#   stack.pop() = 2
#   stack.append(2 * 2) = 4
# stack = [3, 4]

# Final result = sum(stack) = 3 + 4 = 7 ✅