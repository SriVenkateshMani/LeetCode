class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count_map = defaultdict(int)

        for i in nums:
            count_map[i] += 1
        
        unique_nums = sorted(count_map.keys())
        n = len(unique_nums)
        
        dp = [0] * n
        dp[0] = unique_nums[0] * count_map[unique_nums[0]]

        if n == 1:
            return dp[0]
        
        if unique_nums[1] == unique_nums[0] + 1:
            dp[1] = max(dp[0], unique_nums[1] * count_map[unique_nums[1]])
        else:
            dp[1] = dp[0] + unique_nums[1] * count_map[unique_nums[1]]
        
        i = 2
        while i < n:
            if unique_nums[i] == unique_nums[i-1] + 1:
                dp[i] = max(dp[i-1], dp[i-2] + unique_nums[i] * count_map[unique_nums[i]])
            else:
                dp[i] = dp[i-1] + unique_nums[i] * count_map[unique_nums[i]]

            i += 1
        
        return dp[-1]        