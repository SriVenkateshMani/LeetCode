class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i,j):
            nonlocal count
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return None
            else:
                grid[i][j] = 0
                count += 1
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i,j-1)  
                
            return count

        max_islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count = 0
                    dfs(i,j)
                    max_islands = max(max_islands, count)
                    
        return max_islands