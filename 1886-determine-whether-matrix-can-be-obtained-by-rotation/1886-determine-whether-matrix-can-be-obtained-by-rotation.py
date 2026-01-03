class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate(mat):
            n = len(mat)

            for i in range(n-1):
                for j in range(i+1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            for i in range(n):
                mat[i].reverse()
            
            return mat
        
        for i in range(4):
            if rotate(mat) == target:
                return True

        return False
            