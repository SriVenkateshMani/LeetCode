# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_level = 0
        res = 0

        def dfs(root, level):
            nonlocal res, max_level
            if not root:
                return None
            
            if level > max_level:
                max_level = level
                res = root.val
            
            elif level == max_level:
                res += root.val
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            
        dfs(root, 0)
        return res