# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        col_map = defaultdict(list)
        min_col = max_col = 0

        if root:
            q.append((root, 0))

        while q:
            for _ in range(len(q)):
                node, col = q.popleft()
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                col_map[col].append(node.val)

                if node.left:
                    q.append((node.left, col-1))
                
                if node.right:
                    q.append((node.right, col+1))
    
        return [col_map[i] for i in range(min_col, max_col + 1)]
