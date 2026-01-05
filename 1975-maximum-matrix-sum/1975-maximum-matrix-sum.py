class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_abs_val = float("inf")
        neg_count = 0
        mat = matrix
        row = len(mat)
        col = len(mat[0])

        for i in range(row):
            for j in range(col):
                total += abs(mat[i][j])
                if mat[i][j] < 0:
                    neg_count += 1
                min_abs_val = min(min_abs_val, abs(mat[i][j]))
        
        if neg_count % 2 != 0:
            total -= 2 * min_abs_val
        
        return total

