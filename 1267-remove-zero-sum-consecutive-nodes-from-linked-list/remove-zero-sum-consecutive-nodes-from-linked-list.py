# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        prefix_sum = 0
        prefix_hash = {}
        while curr:
            prefix_sum += curr.val
            prefix_hash[prefix_sum] = curr
            curr = curr.next
        
        prefix_sum = 0
        curr = dummy
        while curr:
            prefix_sum += curr.val
            curr.next = prefix_hash[prefix_sum].next
            curr = curr.next

        return dummy.next