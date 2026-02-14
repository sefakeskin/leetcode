# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self,l1, l2):
        head = ListNode(0)
        newlist = head
        tam_kisim = 0

        while l1 is not None and l2 is not None:
            toplam = l1.val + l2.val + tam_kisim
            tam_kisim = toplam // 10

            newlist.next = ListNode(toplam % 10)
            newlist = newlist.next

            l1 = l1.next
            l2 = l2.next

        kalan = l1 if l1 else l2

        while kalan:
            toplam = kalan.val + tam_kisim
            tam_kisim = toplam // 10

            newlist.next = ListNode(toplam % 10)
            newlist = newlist.next

            kalan = kalan.next

        if tam_kisim:
            newlist.next = ListNode(tam_kisim)

        return head.next
        