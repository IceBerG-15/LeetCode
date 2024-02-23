# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow = head
        prev = head
        while slow and slow.next:
            fast = slow.next
            if slow is head:
                slow.next = fast.next
                fast.next = slow
                head = fast
            else:
                slow.next = fast.next
                fast.next = slow
                prev.next = fast
            prev = slow
            slow = slow.next
        return head