# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []

        while q:
            level_sum = 0
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                level_sum += node.val
            
            res.append(level_sum / level_size)
        
        return res

