# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        ptr = head
        while ptr is not None:
            l.append(ptr.val)
            ptr = ptr.next
        ptr = head
        for i in range(len(l)-1,-1,-1):
            ptr.val = l[i]
            ptr = ptr.next
        return head