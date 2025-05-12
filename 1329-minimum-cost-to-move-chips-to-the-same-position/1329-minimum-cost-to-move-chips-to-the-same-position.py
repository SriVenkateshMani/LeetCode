class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                even += 1
            elif position[i] % 2 == 1:
                odd += 1
        
        return min(even, odd)