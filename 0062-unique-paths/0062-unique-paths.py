class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def func(r, c, memo):
            if r == 1 or c == 1:
                return 1
            
            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = func(r-1, c, memo) + func(r, c-1, memo)
            return memo[(r, c)]
        
        return func(m, n, {})