# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        list_len=0
        while temp!=None:
            temp=temp.next
            list_len+=1

        if list_len == n:
            return head.next
        
        nth=list_len-n-1
        temp=head
        for i in range(nth):
            temp=temp.next
        
        if temp.next is not None:
            temp.next = temp.next.next
            
        return head