class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l = 0
        r = len(colors)-1
        res = 0
        while l < r:
            if colors[l] != colors[r]:
                res = r-l
                break
            l+=1

        l = 0
        r = len(colors)-1
        while l < r:
            if colors[l] != colors[r]:
                res = max(res,(r-l))
            r -= 1
        return res

            
        




          