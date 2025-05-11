class Solution:
    def fillCups(self, amount: List[int]) -> int:
        seconds = 0
        while sum(amount) > 0:
            amount = sorted(amount)
            if amount[2] == 0:
                break
            if amount[1] == 0:
                seconds += amount[2]
                break
            
            amount[2] -= 1
            amount[1] -= 1
            seconds += 1
        
        return seconds