class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        mat = matrix
        rows = len(mat)
        cols = len(mat[0])
        res = [[0]*rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                res[j][i] = mat[i][j]
        return res