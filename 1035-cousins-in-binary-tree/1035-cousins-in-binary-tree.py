# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        if root:
            q.append(root)
        
        while q:
            parent = defaultdict()
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    parent[node.left.val] = node
                if node.right:
                    q.append(node.right)
                    parent[node.right.val] = node
            
            if (x in parent) and (y in parent):
                if parent[x] == parent[y]:
                    return False
                else:
                    return True
        
        return False