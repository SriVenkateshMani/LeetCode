class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stack_idx, stack_val = stack.pop()
                res[stack_idx] = i - stack_idx
            
            stack.append([i,t])
        
        return res