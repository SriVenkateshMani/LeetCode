class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        max_height = float("-inf")
        n = len(heights)
        for i in reversed(range(n)):
            if max_height < heights[i]:
                res.append(i)
                max_height = heights[i]
        
        res.reverse()
        return res