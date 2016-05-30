"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        if not head or (m == n):
            return head
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        for i in range(m-1):
            if not tmp:
                return
            tmp = tmp.next

        tail, nxt = self.reverse(tmp.next, n-m+1)
        tmp.next.next = nxt
        tmp.next = tail
        return dummy.next

    def reverse(self, head, count):
        pre = None
        for i in range(count):
            if not head:
                return pre
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        nxt = None
        if head:
            nxt = head
        return pre, nxt
