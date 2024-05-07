# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            current_node = node

            while current_node:
                next_node = current_node.next
                current_node.next = prev
                prev = current_node
                current_node = next_node

            return prev
        
        reversed_head = reverse(head)
        carry = 0
        ptr = reversed_head
        while ptr:
            n = 2*ptr.val
            ptr.val = n%10 + carry
            carry = n//10
            if ptr.next is None:
                prev = ptr
            ptr = ptr.next
        
        if carry!=0:
            prev.next = ListNode(carry,None)
        
        return reverse(reversed_head)