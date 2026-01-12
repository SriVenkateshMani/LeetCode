class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0

        for i in range(n-1):
            x_curr, y_curr = points[i]
            x_des, y_des = points[i+1]

            res += max(abs(x_des - x_curr), abs(y_des - y_curr))
        
        return res