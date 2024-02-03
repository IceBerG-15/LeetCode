# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        ptr = head
        while ptr:
            count +=1
            ptr = ptr.next
        if count==0:
            return head
        k = k%count
        ptr = head
        for _ in range(count-k-1):
            ptr = ptr.next
        second = ptr
        while second.next:
            second = second.next
        second.next = head
        head = ptr.next
        ptr.next = None
            
        return head
