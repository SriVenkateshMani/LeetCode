class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        i,j = 0,0
        res = []
        consec_count = 1

        while j < n:
            if j > 0 and nums[j-1] + 1 == nums[j]:
                consec_count += 1

            if j-i+1 > k:
                if nums[i] + 1 == nums[i+1]:
                    consec_count -= 1
                i += 1

            if j-i+1 == k:
                if consec_count == k:
                    res.append(nums[j])
                else:
                    res.append(-1)
            j += 1
            
        return res

