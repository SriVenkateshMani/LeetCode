# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        res = 0
        if root:
            q.append((root, root.val))
        while q:
            for _ in range(len(q)):
                curr, max_root = q.popleft()
                if curr.val >= max_root:
                    res += 1
                new_max = max(max_root, curr.val)
                if curr.left:
                    q.append((curr.left, new_max))
                if curr.right:
                    q.append((curr.right, new_max))
        return res