# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        cur = head
        prev = None
        nth = cur
        while nth:
            for i in range(n):
                if nth.next:
                    nth = nth.next
                else:
                    if not prev:
                        return cur.next
                    prev.next = cur.next
                    return head

            prev = cur
            cur = cur.next
            nth = cur
        
        return head



        
        

