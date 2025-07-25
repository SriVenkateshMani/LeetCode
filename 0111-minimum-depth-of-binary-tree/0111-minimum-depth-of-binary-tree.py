# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        res = 0
        if root:
            q.append(root)
            
        
        while q:
            res += 1
            for _ in range(len(q)):
                curr = q.popleft()

                if not curr.left and not curr.right:
                    return res
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            

        return res
