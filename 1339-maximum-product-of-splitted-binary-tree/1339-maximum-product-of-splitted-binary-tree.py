# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = (10**9) + 7
        max_sum = 0

        def dfs(root):
            if not root:
                return 0
            
            return root.val + dfs(root.left) + dfs(root.right)
        
        total = dfs(root)
        
        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0
            
            subtree = root.val + dfs(root.left) + dfs(root.right)
            max_sum = max(max_sum, (total - subtree) * subtree)
            return subtree
        dfs(root)
        return max_sum % mod