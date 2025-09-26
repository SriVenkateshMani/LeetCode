class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                width = i - j
                area = h * width
                max_area = max(max_area, area)
                start = j

            else:
                stack.append((height, start))
        
        while stack:
            h, j = stack.pop()
            width = n - j
            area = h * width
            max_area = max(max_area, area)
        
        return max_area