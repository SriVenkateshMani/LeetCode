class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        res = set()
        for i in range(len(coordinates) - 1):
            dx = coordinates[i+1][0] - coordinates[i][0]
            dy = coordinates[i+1][1] - coordinates[i][1]
            if dx == 0:
                slope = float('inf')  # vertical line
            else:
                slope = dy / dx
            res.add(slope)
        
        if len(res) != 1:
            return False
        
        return True






