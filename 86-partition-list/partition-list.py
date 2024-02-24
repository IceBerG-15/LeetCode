# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyhead = ListNode()
        dummy = dummyhead
        greaterhead = ListNode()
        greater = greaterhead
        ptr = head
        while ptr:
            if ptr.val<x:
                dummy.next = ListNode(ptr.val)
                dummy = dummy.next
            else:
                greater.next = ListNode(ptr.val)
                greater = greater.next
            ptr = ptr.next
        dummy.next = greaterhead.next
        return dummyhead.next