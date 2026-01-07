class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if len(path) == k:
                res.append(path[:])
                return None
            
            for v in range(i, n):
                path.append(v+1)
                backtrack(v+1, path)
                path.pop()

        backtrack(0, [])
        return res