class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1: return list2
        if not list2: return list1

        head1 = list1
        head2 = list2
        new_list_head = ListNode()
        new_list_tail = new_list_head

        while head1 and head2:
            if head1.val < head2.val:
                new_list_tail.val = head1.val
                head1 = head1.next
            else:
                new_list_tail.val = head2.val
                head2 = head2.next
            
            if head1 or head2:
                new_list_tail.next = ListNode()
                new_list_tail = new_list_tail.next

        while head1:
            new_list_tail.val = head1.val
            head1 = head1.next
            if head1: 
                new_list_tail.next = ListNode()
                new_list_tail = new_list_tail.next

        while head2:
            new_list_tail.val = head2.val
            head2 = head2.next
            if head2: 
                new_list_tail.next = ListNode()
                new_list_tail = new_list_tail.next


        return new_list_head