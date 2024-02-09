# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        ptr = head
        while ptr:
            l.append(ptr.val)
            ptr = ptr.next
        l.sort()
        ptr = head
        k = 0
        while ptr:
            ptr.val = l[k]
            k+=1
            ptr = ptr.next
        return head