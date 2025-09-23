class Solution:
    def findMin(self, nums: List[int]) -> int:
       
        def findPivot(nums):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l + r) // 2
                if mid < r and nums[mid] > nums[mid + 1]:
                    return mid
                elif mid > l and nums[mid] < nums[mid - 1]:
                    return mid - 1
                
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return -1

        
        pivot = findPivot(nums)
        return nums[pivot + 1]