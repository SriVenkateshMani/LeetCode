class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, curr = [], []

        def backtrack(i):
            if len(curr) == k:
                res.append(curr[:])
                return None
            
            for i in range(i, n):
                curr.append(i+1)
                backtrack(i+1)
                curr.pop()

        backtrack(0)
        return res