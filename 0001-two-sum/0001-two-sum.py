class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in count_map:
                return [count_map[diff], i]

            count_map[n] = i
        
        return
            
            


        


                
            
        