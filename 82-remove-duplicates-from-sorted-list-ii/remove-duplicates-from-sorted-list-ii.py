# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        curr = head
        prev = dummyHead
        while curr:
            while curr.next and curr.val==curr.next.val:
                curr = curr.next
            if prev.next==curr:
                curr = curr.next
                prev = prev.next
            else:
                prev.next = curr.next
                curr = prev.next
        return dummyHead.next