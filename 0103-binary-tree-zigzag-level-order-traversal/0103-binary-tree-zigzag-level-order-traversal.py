# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        level = 1

        if root:
            q.append(root)
        while q:
            temp_list = []
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                temp_list.append(node.val)
            if level % 2 == 0:
                res.append(temp_list[::-1])
            else:
                res.append(temp_list)
            level += 1
        
        return res