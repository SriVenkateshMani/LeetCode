class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def func(r, c):
            if r == 1 or c == 1:
                return 1
            
            if (r, c) in cache:
                return cache[(r, c)]

            cache[(r, c)] = func(r-1, c) + func(r, c-1)
            return cache[(r, c)]
        
        return func(m, n)