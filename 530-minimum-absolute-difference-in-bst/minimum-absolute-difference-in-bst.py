# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = float('inf')

        def dfs(node):
            nonlocal prev, min_diff
            if not node:
                return

            dfs(node.left)

            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            
            dfs(node.right)
        
        dfs(root)
        return min_diff