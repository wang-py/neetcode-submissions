# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq = deque([root])
        res = []

        while dq:
            right_side = None
            q_len = len(dq)

            for i in range(q_len):
                node = dq.popleft()
                if node:
                    right_side = node
                    dq.append(node.left)
                    dq.append(node.right)
            if right_side:
                res.append(right_side.val)
            
        return res