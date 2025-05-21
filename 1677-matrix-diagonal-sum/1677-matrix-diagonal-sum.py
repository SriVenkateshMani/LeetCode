class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            #primary diagonal
            res += mat[i][i]
            #secondary diagonal
            res += mat[i][len(mat)-1-i]
        
        return res - (mat[len(mat)//2][len(mat)//2] if len(mat) % 2 else 0)         #ternary operator for negating the middle value