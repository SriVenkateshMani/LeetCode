class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        some_map = defaultdict(int)
        d = len(set(nums))
        res = 0
        i, j = 0,0
        n = len(nums)

        while j < n:
            some_map[nums[j]] += 1
            
            while len(some_map) == d:
                res += (n - j)
                some_map[nums[i]] -= 1
                if some_map[nums[i]] == 0:
                    del some_map[nums[i]]
                i += 1
            j += 1
        
        return res



