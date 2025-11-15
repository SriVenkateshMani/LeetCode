class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = 0
        right_max = 0
        max_left = [0] * n
        max_right = [0] * n
        res = 0

        for i in range(n):
            max_left[i] = left_max
            left_max = max(left_max, height[i])
            max_right[n-1-i] = right_max
            right_max = max(right_max, height[n-1-i])
        
        for i in range(n):
            potent = min(max_left[i], max_right[i]) - height[i]
            if potent > 0:
                res += potent
        
        return res
