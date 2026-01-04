class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        min_row = [float("inf")] * rows
        max_col = [float("-inf")] * cols
        mat = matrix
        res = []

        for i in range(rows):
            for j in range(cols):
                min_row[i] = min(min_row[i], mat[i][j])
                max_col[j] = max(max_col[j], mat[i][j])

        min_row = set(min_row)
        max_col = set(max_col)
        return list(set(min_row) & set(max_col))