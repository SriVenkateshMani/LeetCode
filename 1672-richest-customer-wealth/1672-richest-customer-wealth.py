class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = float("-inf")
        rows = len(accounts)
        cols = len(accounts[0])

        for i in range(rows):
            amount = 0
            for j in range(cols):
                amount += accounts[i][j]
            
            res = max(res, amount)
        
        return res