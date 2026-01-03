class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = matrix
        rows = len(mat)
        cols = len(mat[0])

        for i in range(rows-1):
            for j in range(i+1, rows):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        for i in range(rows):
            mat[i].reverse()