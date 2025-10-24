# LeetCode 2043 - Simple Bank System
# https://leetcode.com/problems/simple-bank-system/

# ✅ Problem:
# You are given a list of integers `balance` where balance[i] represents the balance of the (i+1)-th account.
# Implement a Bank class that supports the following:
#   1. transfer(account1, account2, money): move money if valid and enough funds
#   2. deposit(account, money): add money to account if valid
#   3. withdraw(account, money): subtract if valid and enough funds
# Return True if the operation is successful, otherwise False.

# 📚 Pattern: 
# Simulation / Design — direct implementation of state transitions

# 🔍 Core Idea:
# - Validate account number (1-indexed) before operations.
# - Subtract 1 to map to 0-indexed array.
# - Guard conditions for insufficient funds or invalid accounts.

# 🧠 Memory Hook:
# account valid check → 1 <= acc <= n  
# use acc-1 for indexing  
# transfer = withdraw + deposit combined  

# ✅ Time Complexity: O(1) for each operation  
# ✅ Space Complexity: O(n) to store balances  

# 📌 Common Gotchas:
# - Forgetting that accounts are 1-indexed.
# - Accessing invalid index (no acc-1 offset).
# - Skipping balance check before withdrawal or transfer.

class Bank:

    def __init__(self, balance: List[int]):
        # Store initial balances for all accounts
        self.balance = balance
    
    def _valid(self, account: int) -> bool:
        """Check if account number is within valid 1-indexed range."""
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """Transfer money from account1 to account2 if both valid and have funds."""
        if not self._valid(account1) or not self._valid(account2):
            return False 
        
        i, j = account1 - 1, account2 - 1  # convert to 0-indexed
        
        if self.balance[i] < money:
            return False
        
        # Perform the transfer
        self.balance[i] -= money
        self.balance[j] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        """Deposit money into the specified account if valid."""
        if not self._valid(account):
            return False
        
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        """Withdraw money from the specified account if valid and enough funds."""
        if not self._valid(account) or self.balance[account - 1] < money:
            return False
        
        self.balance[account - 1] -= money
        return True


# 🔄 Dry Run:
# Input:
# balance = [10, 100, 20, 50, 30]
# obj = Bank(balance)
# obj.withdraw(3, 10) → True → [10,100,10,50,30]
# obj.transfer(5,1,20) → True → [30,100,10,50,10]
# obj.deposit(5,20) → True → [30,100,10,50,30]
# obj.transfer(3,4,15) → False (insufficient)
# obj.withdraw(10,50) → False (invalid account)