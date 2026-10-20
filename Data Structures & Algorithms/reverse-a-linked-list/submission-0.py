# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            # print(f"head.next is {head.next}, head.val is {head.val}")
            next_p = curr.next
            curr.next = prev
            prev = curr
            curr = next_p

        return prev