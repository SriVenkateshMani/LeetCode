class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def helper(arr):
            n = len(arr)
            if n == 1:
                return arr[0]
            
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            i = 2
            while i < n:
                dp[i] = max(arr[i] + dp[i-2], dp[i-1])
                i += 1
            return dp[-1]
        
        return max(helper(nums[1:]), helper(nums[:-1]))