# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node):
            prev_node = None
            current_node = node

            while current_node:
                next_node = current_node.next
                current_node.next = prev_node
                prev_node = current_node
                current_node = next_node
            
            return prev_node
        
        reversed_head = reverse(head)
        max_value = float('-inf')
        prev = None
        current = reversed_head

        while current:
            if current.val<max_value:
                prev.next = current.next
            else:
                max_value = current.val
                prev = current
            
            current = current.next
        
        return reverse(reversed_head)
            
