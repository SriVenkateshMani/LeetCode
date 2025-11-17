class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hoursTook(mid, piles):
            total = 0
            for pile in piles:
                total += ceil(pile / mid)
            return total

        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r) // 2
            hours = hoursTook(mid, piles)
            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
        
        return l