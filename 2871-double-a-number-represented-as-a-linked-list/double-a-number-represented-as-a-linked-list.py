# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = ''
        while head:
            num += str(head.val)
            head = head.next
        num = int(num)*2
        sys.set_int_max_str_digits(100000)
        num = [int(i) for i in str(num)]
        final = None
        for i in num[::-1]:
            final = ListNode(i,final)
        return final