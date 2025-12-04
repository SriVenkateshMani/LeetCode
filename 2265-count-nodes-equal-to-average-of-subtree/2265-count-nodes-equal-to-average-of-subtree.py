# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return (0,0)
            
            left_sum, left_count = dfs(root.left)
            right_sum, right_count = dfs(root.right)

            total = left_sum + right_sum + root.val
            count = left_count + right_count + 1

            if floor(total / count) == root.val:
                res += 1

            return (total, count)
        dfs(root)
        return res
            
