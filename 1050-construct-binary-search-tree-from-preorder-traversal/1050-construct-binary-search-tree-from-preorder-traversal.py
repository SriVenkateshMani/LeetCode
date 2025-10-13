# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        p = 0
        for i in range(1, len(preorder)):
            if preorder[i] < root.val:
                p = i
            else:
                break
        root.left = self.bstFromPreorder(preorder[1:p+1])
        root.right = self.bstFromPreorder(preorder[p+1:])

        return root
        
                
            