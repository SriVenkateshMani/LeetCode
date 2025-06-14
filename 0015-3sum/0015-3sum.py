class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        #Dealing with the first value

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # regular 2 sum

            l, r = i+1, len(nums)-1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res
            
            