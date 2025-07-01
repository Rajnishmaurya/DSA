# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head

        count=0
        current=head
        prev=None
        while current:
            prev=current
            current=current.next
            count+=1

        k=k%count
        if k==0:
            return head
        
        prev.next=head
        current=head
        for _ in range(count-k-1):
            current=current.next
        
        answer=current.next
        current.next=None
        return answer


        
        