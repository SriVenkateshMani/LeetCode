class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i,j = 0, 0
        count_map = defaultdict(int)
        max_size = 0
        n = len(nums)

        while j < n:
            count_map[nums[j]] += 1
            while count_map[nums[j]] > k:
                count_map[nums[i]] -= 1
                i += 1
                
            max_size = max(max_size, j-i+1)
            j += 1

        return max_size
        
