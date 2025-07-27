class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atmost(nums, k):
            i, j = 0, 0
            res = 0
            hash_map = defaultdict(int)

            while j < len(nums):
                hash_map[nums[j]] += 1

                if len(hash_map) <= k:
                    res += j-i+1

                else:
                    while i <= j and len(hash_map) > k:
                        hash_map[nums[i]] -= 1
                        if hash_map[nums[i]] == 0:
                            del hash_map[nums[i]]
                        i += 1

                    if len(hash_map) <= k:
                        res += j-i+1
                   
                j += 1

            return res 

        return atmost(nums, k) - atmost(nums, k-1)

    



    