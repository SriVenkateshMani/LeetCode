# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return (None, 0)
            
            left, left_height = dfs(root.left)
            right, right_height = dfs(root.right)
            if left_height == right_height:
                return root, left_height + 1
            elif left_height > right_height:
                return left, left_height + 1
            else:
                return right, right_height + 1
            
        res, _ = dfs(root)
        
        return res