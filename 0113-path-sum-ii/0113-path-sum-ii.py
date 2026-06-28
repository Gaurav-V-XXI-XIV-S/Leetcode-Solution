# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, s, path):
            if not node:
                return
            path.append(node.val)
            s += node.val
            if not node.left and not node.right and s == targetSum:
                ans.append(path[:])
            dfs(node.left, s, path)
            dfs(node.right, s, path)
            path.pop()
        dfs(root, 0, [])
        return ans   