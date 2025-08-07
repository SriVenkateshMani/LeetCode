class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        curr = []

        def backtrack(i):
            if i >= n:
                res.append(curr[:])
                return None

            # Dont pick
            backtrack(i+1)

            # Pick nums[i]
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
        
        backtrack(0)
        return res