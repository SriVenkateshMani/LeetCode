# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = deque()
        if root:
            q.append(root)
        
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node == u:
                    return q[0] if i < size - 1 else None
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        
            
            
                