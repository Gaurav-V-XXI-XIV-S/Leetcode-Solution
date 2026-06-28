# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos={v:i for i,v in enumerate(inorder)}
        i=len(postorder)-1
        def build(l,r):
            nonlocal i
            if l>r:
                return None
            val=postorder[i]
            i-=1
            root=TreeNode(val)
            mid=pos[val]
            root.right=build(mid+1,r)
            root.left=build(l,mid-1)
            return root
        return build(0,len(inorder)-1)