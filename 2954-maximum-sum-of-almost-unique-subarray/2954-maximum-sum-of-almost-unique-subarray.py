class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int: 
        max_sum = run_sum = i = j = 0
        count_map = defaultdict(int)
        n = len(nums)

        while j < n:
            run_sum += nums[j]
            count_map[nums[j]] += 1

            if j-i+1 > k:
                run_sum -= nums[i]
                count_map[nums[i]] -= 1
                if count_map[nums[i]] == 0:
                    del count_map[nums[i]]
                i += 1
            
            if len(count_map) >= m and j-i+1 == k:
                max_sum = max(max_sum, run_sum)
            j += 1
        
        return max_sum
