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
                elif nums[mid] == target:
                    while mid > 0 and nums[mid - 1] == target:
                        mid -= 1
                    res[0] = mid
                    break
        
        def last(nums, target):
            nonlocal res
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] == target:
                    while mid < len(nums) - 1 and nums[mid + 1] == target:
                        mid += 1
                    res[1] = mid
                    break
        
        first(nums, target)
        last(nums, target)

        return res




