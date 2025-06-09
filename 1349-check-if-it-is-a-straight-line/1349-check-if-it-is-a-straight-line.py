class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slopes = set()
        for i in range(len(coordinates)-1):
            dy = coordinates[i+1][1] - coordinates[i][1]
            dx = coordinates[i+1][0] - coordinates[i][0]
            
            if dx == 0:
                slope = float('inf')
            else:
                slope = dy / dx
            
            slopes.add(slope)

        return len(slopes) == 1






