class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        i, j = 0, 0
        n = len(nums)
        max_element = max(nums)
        count = 0
         
        while j < n:
            if nums[j] == max_element:
                count += 1
                
            while count >= k and i <= j:
                if nums[i] == max_element:
                    count -= 1
                i += 1
                
            res += i
            j += 1
        return res


