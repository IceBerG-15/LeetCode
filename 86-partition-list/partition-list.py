# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyhead = ListNode()
        dummy = dummyhead
        greater = []
        ptr = head
        while ptr:
            if ptr.val<x:
                dummy.next = ListNode(ptr.val)
                dummy = dummy.next
            else:
                greater.append(ptr.val)
            ptr = ptr.next
        for i in greater:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return dummyhead.next