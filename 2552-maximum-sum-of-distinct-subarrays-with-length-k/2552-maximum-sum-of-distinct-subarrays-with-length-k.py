class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count_map = {}
        max_sum = 0
        cur_sum = 0
        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            count_map[nums[r]] = count_map.get(nums[r],0) + 1

            if r-l+1 > k:
                count_map[nums[l]] -= 1
                if count_map[nums[l]] == 0:
                    count_map.pop(nums[l])
                cur_sum -= nums[l]
                l += 1
            
            if len(count_map) == k and r-l+1 == k:
                max_sum = max(max_sum, cur_sum)

        return max_sum