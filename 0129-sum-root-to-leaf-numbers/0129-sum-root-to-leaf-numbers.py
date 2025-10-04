# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            
            # Add this node's digit to the path string
            path += str(node.val)
            
            # If leaf node, convert path string to int
            if not node.left and not node.right:
                return int(path)
            
            # Continue down to children
            return dfs(node.left, path) + dfs(node.right, path)
        
        return dfs(root, "")