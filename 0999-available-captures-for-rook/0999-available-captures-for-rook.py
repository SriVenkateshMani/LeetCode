class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        b = board
        count = 0

        for i in range(8):
            for j in range(8):
                if b[i][j] == 'R':
                    r,c = i, j
        
        # Up

        for i in range(1, r+1):
            if b[r-i][c] == 'p':
                count += 1
                break

            elif b[r-i][c] == 'B':
                break

            else:
                continue
        
        # Down

        for i in range(1, 8-r):
            if b[r+i][c] == 'p':
                count += 1
                break
            
            elif b[r+i][c] == 'B':
                break
            
            else:
                continue
        
        # Left

        for i in range(1, c+1):
            if b[r][c-i] == 'p':
                count += 1
                break
            
            elif b[r][c-i] == 'B':
                break
            
            else:
                continue
        
        # Right
        
        for i in range(1, 8-c):
            if b[r][c+i] == 'p':
                count += 1
                break
            
            elif b[r][c+i] == 'B':
                break
            
            else:
                continue
        
        return count