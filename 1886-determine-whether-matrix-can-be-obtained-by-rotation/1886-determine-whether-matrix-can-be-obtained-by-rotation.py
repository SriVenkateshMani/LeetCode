class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate(mat):
            rows = len(mat)
            cols = len(mat[0])

            for i in range(rows-1):
                for j in range(i+1, rows):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            for i in range(rows):
                mat[i].reverse()
            
            return mat
        
        for i in range(4):
            if rotate(mat) == target:
                return True
                
        return False
            