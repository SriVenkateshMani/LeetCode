# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        q = deque([root])
        level = 1

        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()

                if level == depth - 1:
                    left_old = node.left
                    right_old = node.right
                    node.left = TreeNode(val, left_old)
                    node.right = TreeNode(val, None, right_old)
                
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            level += 1
        
        return root