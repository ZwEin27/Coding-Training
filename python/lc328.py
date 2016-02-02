# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        odd_head = head
        even_head = head.next
        odd_cur = odd_head
        even_cur = even_head

        while even_cur and even_cur.next:
            odd_cur.next = even_cur.next
            odd_cur = odd_cur.next
            even_cur.next = odd_cur.next
            even_cur = even_cur.next
        odd_cur.next = even_head
        return head
        



