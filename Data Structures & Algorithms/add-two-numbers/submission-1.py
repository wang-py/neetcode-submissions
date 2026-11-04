# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = ListNode()
        tail = dummy_head

        while l1 or l2:
            if not l1:
                v1 = 0
                v2 = l2.val
                l2 = l2.next
            elif not l2:
                v1 = l1.val
                v2 = 0
                l1 = l1.next
            else:
                v1 = l1.val
                v2 = l2.val
                l1 = l1.next
                l2 = l2.next

            result = v1 + v2 + carry
            if result >= 10:
                carry = 1
                result %= 10
            else:
                carry = 0
            
            sum_node = ListNode(result, None)
            tail.next = sum_node
            tail = tail.next

        if carry == 1:
            carry_node = ListNode(carry, None)
            tail.next = carry_node
        
        return dummy_head.next
