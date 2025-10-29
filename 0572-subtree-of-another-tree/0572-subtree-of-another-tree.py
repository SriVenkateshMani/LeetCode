# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, t: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not t:
            return False
        if not s:
            return True
        
        if self.sameTree(t, s):
            return True
        
        return (self.isSubtree(t.left, s) or self.isSubtree(t.right, s))

    def sameTree(self, t, s):
        if not s and not t:
            return True
        
        if s and t and s.val == t.val:
            return (self.sameTree(t.left, s.left) and self.sameTree(t.right, s.right))
        