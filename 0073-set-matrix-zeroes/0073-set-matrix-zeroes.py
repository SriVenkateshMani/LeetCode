class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_row = []
        zero_col = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_row.append(i)
                    zero_col.append(j)
                    

        for i in range(rows):
            for j in range(cols):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0
        

        