# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(root, cur_sum):
            if not root:
                return None

            path.append(root.val)
            cur_sum += root.val
            
            if not root.left and not root.right and cur_sum == targetSum:
                res.append(path[:])
                path.pop()
                return
            
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
            path.pop()
            
        dfs(root, 0)
        return res