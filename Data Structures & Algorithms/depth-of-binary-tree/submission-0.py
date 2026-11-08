# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth_l, depth_r = 0, 0
        if not root:
            return 0
        temp = root
        root = root.left
        depth_l = self.maxDepth(root)
        root = temp.right
        depth_r = self.maxDepth(root)

        return 1 + max(depth_l, depth_r)



