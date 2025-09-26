class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = j = max_sum = 0
        count_map = defaultdict(int)
        n = len(nums)
        run_sum = 0
        while j < n:
            run_sum += nums[j]
            count_map[nums[j]] += 1

            if j-i+1 > k:
                count_map[nums[i]] -= 1
                run_sum -= nums[i]
                if count_map[nums[i]] == 0:
                    del count_map[nums[i]]
                i += 1
        
            if len(count_map) == k and j-i+1 == k:
                max_sum = max(max_sum, run_sum)
            j += 1
            
        return max_sum