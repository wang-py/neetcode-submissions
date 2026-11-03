"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_dict = {None : None}
        cur = head

        while cur:
            copy = Node(cur.val, None, None)  
            copy_dict[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = copy_dict[cur]
            copy.next = copy_dict[cur.next]
            copy_dict[cur].random = copy_dict[cur.random]

            cur = cur.next
        

        return copy_dict[head]

        
