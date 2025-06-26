# LeetCode 65 - Valid Number
# https://leetcode.com/problems/valid-number/

# ✅ Problem:
# Validate whether the given string represents a valid number.

# A valid number can include:
# - Digits (0–9)
# - A decimal point (.)
# - An exponent (e or E)
# - A plus or minus sign (+ or -)
# - Leading and trailing whitespaces (which should be trimmed)

# Examples of valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"
# Examples of invalid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"

# 📚 Pattern: String Parsing / State Machine (Manual Flag Tracking)

# 🧪 Subtype: Flag-based Manual Parsing
# - Track states using booleans:
#     - seen_digit: at least one digit seen
#     - seen_dot: dot has been seen (only allowed once and not after 'e')
#     - seen_exp: 'e' or 'E' has been seen (only allowed once and must be after a digit)
# - Sign '+'/'-' allowed only at beginning or right after an exponent

# 🧠 Memory Hook:
# strip whitespace
# scan char-by-char
# ⚙️ Flags: seen_digit, seen_dot, seen_exp
# ➕ Sign only at start or after 'e'
# ⚪ Dot: only once, never after 'e'
# 🔡 'e': only once, must follow digit, must see digit after
# ❌ Anything else → invalid

# ✅ Time Complexity: O(n) — scan the entire string once
# ✅ Space Complexity: O(1)

# 📌 Common Gotchas:
# - Don't allow signs anywhere: must be at beginning or just after 'e'
# - Must reset seen_digit = False after 'e'
# - Just "." or "e" without digits are invalid

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        if not s:
            return False

        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True

            elif char in ['+', '-']:
                # ✅ Sign is valid only at start or right after 'e'
                if i > 0 and s[i - 1].lower() != 'e':
                    return False

            elif char == '.':
                # ✅ Dot allowed only once and not after exponent
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            elif char.lower() == 'e':
                # ✅ Exponent must come after digit and only once
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False  # must see digit after e

            else:
                return False

        return seen_digit


# 🔄 Dry Run:

# Input: "46.e3"
# → s.strip() → "46.e3"
# i=0 → '4' → digit → seen_digit = True
# i=1 → '6' → digit → seen_digit = True
# i=2 → '.' → valid since !seen_dot and !seen_exp → seen_dot = True
# i=3 → 'e' → valid since seen_digit is True → seen_exp = True, seen_digit = False
# i=4 → '3' → digit → seen_digit = True
# Final: seen_digit is True → ✅ return True

# Input: "."
# → s.strip() → "."
# i=0 → '.' → seen_dot = True
# Final: seen_digit = False → ❌ return False

# Input: "1e"
# i=0 → '1' → seen_digit = True
# i=1 → 'e' → seen_exp = True, seen_digit = False
# Final: seen_digit = False → ❌ return False

# 🔁 Final result: True only if valid number formatting rules satisfied