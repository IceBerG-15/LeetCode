# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ''
        while head:
            s +=str(head.val)
            head = head.next
        count=0
        ans = 0
        for i in s[::-1]:
            if i=='1':
                ans +=2**count
            count +=1
        return ans