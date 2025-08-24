class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        i,j = 0, 0
        n = len(nums)
        count_map = defaultdict(int)
        res = []

        while j < n:
            count_map[nums[j]] += 1 
            
            while j-i+1 > k:
                count_map[nums[i]] -= 1
                if count_map[nums[i]] == 0:
                    del count_map[nums[i]] 
                i += 1

            if j-i+1 == k:
                res.append(len(count_map))

            j += 1
        
        return res

            