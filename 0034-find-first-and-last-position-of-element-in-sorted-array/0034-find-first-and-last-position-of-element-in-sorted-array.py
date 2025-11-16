class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        def first(nums, target):
            nonlocal res
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    res[0] = mid
                    r = mid - 1
        
        def last(nums, target):
            nonlocal res
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    res[1] = mid
                    l = mid + 1
        
        first(nums, target)
        last(nums, target)

        return res




