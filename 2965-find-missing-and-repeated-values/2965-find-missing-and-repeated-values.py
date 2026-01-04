class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq_map = defaultdict(int)
        rows = len(grid)
        cols = len(grid[0])
        rep, miss = -1, -1

        for i in range(rows):
            for j in range(cols):
                freq_map[grid[i][j]] += 1

        for num in range(1, rows * rows + 1):
            if freq_map[num] == 2:
                rep = num
            elif freq_map[num] == 0:
                miss = num
        
        return [rep, miss]