# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq_map = defaultdict(int)
        max_freq_sum = 0
        res = []
        def dfs(root):
            nonlocal freq_map
            if not root:
                return 0
            
            else:
                left = dfs(root.left)
                right = dfs(root.right)
                total_sum = root.val + left + right
                freq_map[total_sum] += 1
            
            return total_sum
        
        dfs(root)

        max_freq_sum = max(freq_map.values())
        for key, value in freq_map.items():
            if value == max_freq_sum:
                res.append(key)
        
        return res
        
