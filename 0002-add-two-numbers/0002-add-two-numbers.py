# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(-1)
        temp=dummy
        while l1 or l2 or carry:
            sum=0
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            sum+=carry
            value=sum%10
            carry=sum//10
            temp.next=ListNode(value)
            temp=temp.next
        return dummy.next
        

        