# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        col_table = defaultdict(list)
        queue = deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()

            if node is not None:
                col_table[col].append((row, node.val))

                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))
            
        sorted_cols = sorted(col_table.keys())

        res = []
        for col in sorted_cols:
            col_table[col].sort(key=lambda x: (x[0], x[1]))
            res.append([val for row, val in col_table[col]])

        return res