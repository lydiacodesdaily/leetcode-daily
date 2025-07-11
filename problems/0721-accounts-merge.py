# LeetCode 721 - Accounts Merge
# https://leetcode.com/problems/accounts-merge/

# ✅ Problem:
# Given a list of accounts, where each account contains:
# - Name (account[0])
# - List of emails (account[1:])
# Merge accounts if any emails overlap.
# Return merged accounts: [name, sorted_emails...]

# 📚 Pattern:
# Union-Find (Disjoint Set Union)

# 🔍 Key Insight:
# - Each email is a node.
# - If two emails appear in the same account, union them → same group.
# - Use `find` to identify group leaders.
# - Group emails by parent, then map parent to account name.

# 🧠 Memory Hook:
# find(x): get leader
# union(x, y): make x's leader follow y's leader
# group by leader → merge emails

# ✅ Time: O(N * α(N)) — nearly linear (inverse Ackermann)
# ✅ Space: O(N)

from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}            # email → parent email
        email_to_name = {}     # email → name

        # ✅ Step 1: Union emails in the same account
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                if email not in parent:
                    parent[email] = email  # self-parent
                union(email, first_email)
                email_to_name[email] = name

        # ✅ Step 2: Group emails by root parent
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        # ✅ Step 3: Format result
        result = []
        for root_email, email_list in groups.items():
            name = email_to_name[root_email]
            result.append([name] + sorted(email_list))

        return result


# 🔄 Dry Run Example:
# Input:
# [
#   ["John", "a@gmail.com", "b@gmail.com"],
#   ["John", "b@gmail.com", "c@gmail.com"],
#   ["Mary", "d@gmail.com"]
# ]
#
# Union:
# - a ← b ← c (all point to 'a')
# - d is separate
#
# Grouped by leader:
# "a@gmail.com": ["a", "b", "c"]
# "d@gmail.com": ["d"]
#
# Output:
# [["John", "a", "b", "c"], ["Mary", "d"]]

if __name__ == "__main__":
    sol = Solution()
    accounts = [
        ["John", "a@gmail.com", "b@gmail.com"],
        ["John", "b@gmail.com", "c@gmail.com"],
        ["Mary", "d@gmail.com"]
    ]
    merged = sol.accountsMerge(accounts)
    for group in merged:
        print(group)