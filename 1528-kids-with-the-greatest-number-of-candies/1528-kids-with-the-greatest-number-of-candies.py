class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        res = []
        for candy in candies:
            max_candy =  max(i for i in candies)
            if candy + extraCandies >= max_candy:
                res.append(True)
            else:
                res.append(False)
        return res