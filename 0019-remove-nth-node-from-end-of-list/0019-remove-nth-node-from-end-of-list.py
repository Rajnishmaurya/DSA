# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        node=dummy
        temp=0
        while temp<=n:
            node=node.next
            temp+=1
        temp1=dummy

        while node:
            node=node.next
            temp1=temp1.next

        temp1.next=temp1.next.next
        return dummy.next