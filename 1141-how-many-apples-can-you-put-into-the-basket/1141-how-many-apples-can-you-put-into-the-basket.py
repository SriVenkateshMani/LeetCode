class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        limit = 0
        res = 0
        weight = sorted(weight)
        for i in weight:
            if i <= 5000 and limit + i <= 5000:
                limit += i
                res += 1
        return res
            
