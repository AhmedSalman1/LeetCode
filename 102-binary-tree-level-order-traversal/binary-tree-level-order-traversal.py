# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            temp = []

            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    temp.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if temp:
                res.append(temp)
        return res