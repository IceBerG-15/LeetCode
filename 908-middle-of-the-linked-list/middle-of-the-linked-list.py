# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        count = 0
        while ptr:
            count +=1
            ptr = ptr.next
        mid = count//2
        for i in range(mid):
            head = head.next
        return head