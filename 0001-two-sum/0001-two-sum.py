class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count_map = defaultdict(int)
        for i, j in enumerate(nums):
            diff = target - j
            if diff in count_map:
                return [count_map[diff], i]
            
            count_map[j] = i


            


        


                
            
        