class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        m = len(mat)//2
        n = len(mat)-1
        for i in range(len(mat)):
            res += mat[i][i]
            res += mat[i][n-i]
            
        if len(mat) % 2 == 1:
            res -= mat[m][m]
        
        return res