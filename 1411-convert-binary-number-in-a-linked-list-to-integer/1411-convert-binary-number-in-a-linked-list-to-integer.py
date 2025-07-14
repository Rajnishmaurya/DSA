# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        answer=0
        temp=head
        i=0
        while temp:
            temp=temp.next
            i+=1
        temp=head

        while temp:
            bit=temp.val
            i-=1
            answer+=bit*pow(2,i)
            temp=temp.next
        return answer
        