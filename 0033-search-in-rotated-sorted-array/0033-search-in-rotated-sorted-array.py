class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(nums, target, l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            
            return -1

        def findPivot(nums):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l + r) // 2
                if mid < r and nums[mid] > nums[mid + 1]:
                    return mid
                elif mid > l and nums[mid] < nums[mid - 1]:
                    return mid - 1
                elif nums[mid] <= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

            return -1
        
        def search(nums, target):
            pivot = findPivot(nums)

            if pivot == -1:
                return binary_search(nums, target, 0, len(nums)-1)
            
            elif nums[pivot] == target:
                return pivot
                
            if target >= nums[0]:
                return binary_search(nums, target, 0, pivot-1)
            
            return binary_search(nums, target, pivot+1, len(nums)-1)
        
        return search(nums, target)

