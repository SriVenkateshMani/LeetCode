class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {}
        max_element = 0
        max_count = 0
        for i in nums:
            count_map[i] = count_map.get(i,0) + 1

        for key,value in count_map.items():
            if value > max_count:
                max_count = value
                max_element = key
        

        return max_element

                

        