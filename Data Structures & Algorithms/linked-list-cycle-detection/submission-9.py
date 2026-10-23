# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        if head.next and head.next.next:
            slow_p = head.next
            fast_p = head.next.next
        else:
            return False

        while slow_p:
            slow_p = slow_p.next
            if fast_p and fast_p.next:
                fast_p = fast_p.next.next
            else:
                return False
            if slow_p == fast_p:
                return True
        
        return False