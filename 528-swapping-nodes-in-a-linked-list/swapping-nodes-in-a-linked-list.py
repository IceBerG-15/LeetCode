# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        slow = head
        while slow:
            count +=1
            slow = slow.next
        slow = head
        for _ in range(k-1):
            slow = slow.next
        fast = head
        for _ in range(abs(count-k)):
            fast = fast.next
        temp = slow.val
        slow.val = fast.val
        fast.val = temp
        return head