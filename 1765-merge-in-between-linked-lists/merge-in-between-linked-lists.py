# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list1_end = list1
        list1_start = list1
        for _ in range(b+1):
            list1_end = list1_end.next
        for _ in range(a-1):
            list1_start = list1_start.next
        ptr = list2
        while ptr.next:
            ptr = ptr.next
        list1_start.next = list2
        ptr.next = list1_end
        return list1