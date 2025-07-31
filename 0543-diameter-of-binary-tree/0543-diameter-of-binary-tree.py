# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter
            if not node:
                return 0
            
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                diameter = left + right
                max_diameter = max(max_diameter, diameter)

            return max(left, right) + 1
        
        dfs(root)
        return max_diameter