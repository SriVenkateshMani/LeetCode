class Solution:
    def triangleType(self, nums: List[int]) -> str:
        i = 0

        if nums[i] + nums[i+1] <= nums[i+2] or nums[i+1] + nums[i+2] <= nums[i] or nums[i+2] + nums[i] <= nums[i+1]:
            return "none"
        elif nums[i] == nums[i+1] == nums[i+2]:
            return "equilateral"
        elif nums[i] == nums[i+1] or nums[i+1] == nums[i+2] or nums[i] == nums[i+2]:
            return "isosceles"
        else:
            return "scalene"