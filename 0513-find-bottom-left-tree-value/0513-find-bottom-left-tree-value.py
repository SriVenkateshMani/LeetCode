# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)
    
        while len(q) > 0:
            for i in range(len(q)):
                curr = q.popleft()
                if i == 0:
                    leftmost = curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return leftmost


