class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(i, path):
            if i == n:
                res.append(path[:])
                return None
            
            
            # Dont pick
            backtrack(i+1, path)

            # Pick nums[i]
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
            
        backtrack(0, [])
        return res