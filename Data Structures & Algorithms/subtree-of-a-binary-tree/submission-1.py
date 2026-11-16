# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root1, root2):
            if not root1 and not root2:
                return True    
            if not root1 or not root2 or root1.val != root2.val:
                return False
        
            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        
        is_same_tree = isSameTree(root, subRoot)
        if is_same_tree:
            return is_same_tree
        root_left = root.left
        root_right = root.right
        while root_left:
            is_same_tree = isSameTree(root_left, subRoot)
            if is_same_tree:
                return is_same_tree
            root_left = root_left.left
        while root_right:
            is_same_tree = isSameTree(root_right, subRoot)
            if is_same_tree:
                return is_same_tree
            root_right = root_right.right

        return False